#!/usr/bin/env python3
"""Minimal executable Technical UST interpretation/runtime layer for Maestro P0.3.

This layer consumes the materialized ownership/dependency overlay and the bounded
workforce registry. It performs address dispatch, change impact propagation, lawful
peer-objection blocking, lyric-lock enforcement, and MAP.K3 reference invalidation.
It does not invoke models or make creative decisions.
"""
from __future__ import annotations
import copy
import os
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional

try:
    import yaml
except ImportError as exc:
    raise RuntimeError("PyYAML is required for technical_ust_runtime.py; install runtime/maestro-workforce/requirements.txt") from exc

import workforce_runtime as workforce

ROOT=os.path.dirname(os.path.abspath(__file__))
OVERLAY_NAME='technical_ust_ownership_dependency_overlay.yaml'
MAP_REF_SLOT={'THY':'MAP.K3.S1','VOC':'MAP.K3.S2','TIM':'MAP.K3.S3','PER':'MAP.K3.S4','POST':'MAP.K3.S5'}

class RuntimeAuthorityError(RuntimeError): pass
class RuntimeBlockError(RuntimeError): pass


def load_overlay(path: Optional[str]=None) -> Dict[str,Any]:
    p=path or os.path.join(ROOT,OVERLAY_NAME)
    with open(p,encoding='utf-8') as f:
        data=yaml.safe_load(f)
    if not isinstance(data,dict) or 'axis_bindings' not in data or 'crossstream_dependencies' not in data:
        raise ValueError('invalid Technical UST ownership/dependency overlay')
    return data


def _parts(address:str):
    p=address.split('.')
    axis=p[0] if p else None
    key='.'.join(p[:2]) if len(p)>=2 else None
    subkey='.'.join(p[:3]) if len(p)>=3 else None
    return axis,key,subkey


def _overlap(a:str,b:str)->bool:
    return a==b or a.startswith(b+'.') or b.startswith(a+'.')


def _uniq(xs:Iterable[str])->List[str]:
    out=[]
    for x in xs:
        if x and x not in out: out.append(x)
    return out


def binding_for(address:str, overlay:Optional[Dict[str,Any]]=None)->Dict[str,Any]:
    ov=overlay or load_overlay(); axis,key,subkey=_parts(address)
    ad=(ov.get('axis_bindings') or {}).get(axis)
    if not ad: raise RuntimeAuthorityError(f'no axis binding for {address}')
    kb=(ad.get('key_bindings') or {}).get(key,{}) if key else {}
    sb=(kb.get('subkey_bindings') or {}).get(subkey,{}) if subkey else {}
    owner=sb.get('primary_owner') or kb.get('primary_owner') or ad.get('primary_owner')
    if not owner:
        raise RuntimeAuthorityError(f'no unambiguous primary owner for {address}; abstain_and_route')
    reviewers=[]
    reviewers.extend(ad.get('required_reviewers') or ad.get('reviewers') or [])
    reviewers.extend(kb.get('required_reviewers') or [])
    reviewers.extend(sb.get('required_reviewers') or [])
    subreview=(kb.get('subkey_reviewers') or {}).get(subkey,[]) if subkey else []
    reviewers.extend(subreview or [])
    reviewers=[r for r in _uniq(reviewers) if r!=owner]
    return {'address':address,'axis':axis,'key':key,'subkey':subkey,'primary_owner':owner,'required_reviewers':reviewers,'axis_binding':ad,'key_binding':kb,'subkey_binding':sb}


def dispatch_address(address:str,task:str,context_refs:Optional[List[str]]=None,requested_output='employee_work_note')->Dict[str,Any]:
    b=binding_for(address)
    worker=workforce.resolve(b['primary_owner'])
    if not worker: raise RuntimeAuthorityError('overlay owner is not a materialized worker: '+b['primary_owner'])
    pkt=workforce.envelope(worker,task,context_refs or [],requested_output,address_ownership=address,required_reviewers=b['required_reviewers'])
    pkt['technical_ust']={'address':address,'primary_owner':b['primary_owner'],'required_reviewers':b['required_reviewers']}
    return pkt

@dataclass
class Objection:
    worker_id:str
    address:str
    reason:str
    active:bool=True

class TechnicalUSTRuntime:
    def __init__(self,values:Optional[Dict[str,Any]]=None,lyrics_locked:bool=False,overlay:Optional[Dict[str,Any]]=None):
        self.overlay=overlay or load_overlay()
        self.values=copy.deepcopy(values or {})
        self.lyrics_locked=bool(lyrics_locked)
        self.status={k:'current' for k in self.values}
        self.objections:List[Objection]=[]
        self.events:List[Dict[str,Any]]=[]

    def dispatch(self,address:str,task:str,requested_output='employee_work_note'):
        return dispatch_address(address,task,['technical.ust',OVERLAY_NAME],requested_output)

    def _hard_impacts(self,changed:str)->List[Dict[str,Any]]:
        out=[]; axis,_,_=_parts(changed)
        for edge in (self.overlay.get('crossstream_dependencies',{}).get('hard_schema_edges') or []):
            src=str(edge.get('from',''))
            if not src or not _overlap(src,changed): continue
            target=edge.get('to')
            out.append({'kind':'hard_schema','from':src,'target':target,'relation':edge.get('relation')})
            slot=MAP_REF_SLOT.get(axis)
            if slot and target=='MAP.K3':
                refs=self.values.get(slot,{})
                if isinstance(refs,dict):
                    for section,ids in refs.items():
                        seq=ids if isinstance(ids,list) else [ids]
                        hits=[r for r in seq if isinstance(r,str) and _overlap(r,changed)]
                        if hits:
                            out.append({'kind':'map_k3_reference','from':changed,'target':f'{slot}@{section}','relation':'referenced_upstream_address_changed','references':hits})
        return out

    def _labor_impacts(self,changed:str)->List[Dict[str,Any]]:
        out=[]
        for edge in (self.overlay.get('crossstream_dependencies',{}).get('supported_labor_edges') or []):
            src=str(edge.get('from',''))
            if src and _overlap(src,changed):
                out.append({'kind':'labor_review','from':src,'target':edge.get('to'),'relation':edge.get('relation'),'effect':edge.get('effect'),'owner_to':edge.get('owner_to'),'reviewer_to':edge.get('reviewer_to'),'reviewers_to':edge.get('reviewers_to') or []})
        return out

    def dependency_impacts(self,changed:str)->List[Dict[str,Any]]:
        return self._hard_impacts(changed)+self._labor_impacts(changed)

    def apply_change(self,worker_id:str,address:str,value:Any,operator_authorized_lyric_change:bool=False)->Dict[str,Any]:
        b=binding_for(address,self.overlay)
        if worker_id!=b['primary_owner']:
            raise RuntimeAuthorityError(f'{worker_id} does not own {address}; owner is {b["primary_owner"]}')
        if address.startswith('LYR.') and self.lyrics_locked and not operator_authorized_lyric_change:
            self.events.append({'event':'lyric_mutation_blocked','worker_id':worker_id,'address':address,'reason':'lyrics_locked'})
            raise RuntimeBlockError('locked lyrics are immutable without explicit operator authorization')
        before=copy.deepcopy(self.values.get(address))
        self.values[address]=copy.deepcopy(value); self.status[address]='changed_pending_review'
        impacts=self.dependency_impacts(address)
        for impact in impacts:
            tgt=impact.get('target')
            if tgt: self.status[tgt]='reopened_dependency'
        ev={'event':'change_applied','worker_id':worker_id,'address':address,'before':before,'after':copy.deepcopy(value),'impacts':impacts}
        self.events.append(ev); return ev

    def raise_peer_objection(self,worker_id:str,address:str,reason:str)->Dict[str,Any]:
        b=binding_for(address,self.overlay)
        if worker_id not in b['required_reviewers']:
            raise RuntimeAuthorityError(f'{worker_id} is not a lawful reviewer for {address}')
        obj=Objection(worker_id,address,reason,True); self.objections.append(obj)
        ev={'event':'peer_objection_raised','worker_id':worker_id,'address':address,'reason':reason,'blocking':True}
        self.events.append(ev); return ev

    def unresolved_objections(self,address:str)->List[Objection]:
        return [o for o in self.objections if o.address==address and o.active]

    def finalize(self,address:str)->Dict[str,Any]:
        active=self.unresolved_objections(address)
        if active:
            self.events.append({'event':'finalize_blocked','address':address,'blockers':[o.worker_id for o in active]})
            raise RuntimeBlockError('unresolved lawful peer objection blocks final acceptance')
        self.status[address]='accepted'
        ev={'event':'finalized','address':address}; self.events.append(ev); return ev

    def resolve_objection(self,worker_id:str,address:str)->None:
        matched=False
        for o in self.objections:
            if o.address==address and o.worker_id==worker_id and o.active:
                o.active=False; matched=True
        if not matched: raise RuntimeAuthorityError('no active objection owned by that reviewer')
        self.events.append({'event':'peer_objection_resolved','worker_id':worker_id,'address':address})
