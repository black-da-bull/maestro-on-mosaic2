#!/usr/bin/env python3
"""Reproduce reached-source threshold search without rewriting repository files.
Usage: scan_occurrences.py REPO OUTDIR
Uses the pinned baseline inventory plus current bundle sources. Dispositions are evidence
strata, not endorsement of historical claims. New/unreadable evidence requires human review.
"""
import pathlib,sys,csv,re,json,hashlib
PAT=re.compile(r'97\.5%?|release[ _-](?:floor|threshold)|PASS_THRESHOLD(?:_PCT)?|composite|G\s*(?:>=|≥)\s*7|G-Card',re.I)

def run(repo,out):
    r=pathlib.Path(repo);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
    inventory=list(csv.DictReader((r/'_PROVENANCE/promotion_2026-09-06/REPOSITORY_INVENTORY.csv').open()))
    paths={x['path']:x for x in inventory if x['type']=='blob'}
    for f in (r/'maestro-current').rglob('*'):
        if f.is_file():paths.setdefault(str(f.relative_to(r)),{})
    missing=[];rows=[];read=0
    opaque={'.pdf','.oxps','.paint','.docx','.xlsx','.pptx','.ico','.lnk','.cinr'}
    for p,meta in sorted(paths.items()):
        f=r/p
        if f.suffix.lower() in opaque:continue
        if not f.is_file():missing.append({'path':p,'reason':'not materialized'});continue
        raw=f.read_bytes();text=None
        for enc in ('utf-8-sig','utf-16'):
            try:text=raw.decode(enc);break
            except UnicodeError:pass
        if text is None:missing.append({'path':p,'reason':'undecodable raw bytes'});continue
        read+=1
        current=p.startswith('maestro-current/') or p=='drafts/EXECUTABLE_APP_DESIGN_v0_1.md'
        for i,line in enumerate(text.splitlines(),1):
            for m in PAT.finditer(line):
                status='CURRENT_VALID_REVIEW_REQUIRED' if current else 'HISTORICAL_VALID'
                reason='Review current applicability against DEC-PROMO-01/02; test negatives are not defaults.' if current else 'Preserved historical text only; universal interpretation superseded for current use.'
                if 'song.excellence.matrix.iterative.design.session.txt' in p and 3598<=i<=3925 and m.group().startswith('97.5'):
                    status='RUN_LOCAL_VALID';reason='Identified song-local correction and recalculation.'
                rows.append([p,i,m.group(),status,line[max(0,m.start()-70):m.end()+100],reason])
    with (out/'occurrences.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['path','line','term','disposition','context','reason']);w.writerows(rows)
    (out/'coverage.json').write_text(json.dumps({'read_files':read,'occurrences':len(rows),'missing_or_undecodable':missing,'note':'No automatic promotion verdict; resolve/review every new match and compare impacts before merging.'},indent=2)+'\n')
    print(json.dumps({'read_files':read,'occurrences':len(rows),'coverage_gaps':len(missing)}))
    return 2 if missing else 0

if __name__=='__main__':sys.exit(run(sys.argv[1],sys.argv[2]))
