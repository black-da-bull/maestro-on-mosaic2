"""Role-detector repair (skill python, v0.5) — coverage-before-projection (M4).
Fixes: (1) the `You said:\\b` word-boundary bug that dropped ROOT turns in session-typed
exports; (2) the operator/AI marker family the v0.4 detector never covered
(##### You said:, numbered-mirror '001 | You said:', ## 👤 You, **You, Human:, and AI
persona 'X said:' e.g. 'Clarity Architect said:'). Splits a transcript into role-tagged
turns; nothing else in the pipeline changes."""
import re
# operator (ROOT) turn openers — any leading numbered-mirror prefix + optional heading hashes
OP = re.compile(r'(?m)^(?:\d+\s*\|\s*)?#{0,6}\s*(?:👤\s*)?(?:You said:|You:|Human:|\[You\]|\*\*You\b|👤\s*You\b)')
# AI (PROPOSAL) turn openers — ChatGPT/Assistant OR any 'Name said:' persona (incl. 'Clarity Architect said:')
AI = re.compile(r'(?m)^(?:\d+\s*\|\s*)?#{0,6}\s*(?:🎛️?\s*)?(?:ChatGPT said:|Assistant:|[A-Z][\w .()\-]{0,34} said:|\*\*(?:Assistant|AI|ChatGPT))')

def split_roles(t):
    marks=[]
    for m in OP.finditer(t): marks.append((m.start(),'human_root'))
    for m in AI.finditer(t): marks.append((m.start(),'ai_proposal'))
    marks.sort()
    # dedup identical offsets (OP wins over AI if both matched same pos)
    seen=set(); clean=[]
    for off,role in marks:
        if off in seen: continue
        seen.add(off); clean.append((off,role))
    if not clean:
        return [('segment',t.strip())] if t.strip() else []
    out=[]
    if clean[0][0]>0 and t[:clean[0][0]].strip():
        out.append(('context', t[:clean[0][0]].strip()))
    for i,(off,role) in enumerate(clean):
        end=clean[i+1][0] if i+1<len(clean) else len(t)
        body=t[off:end].strip()
        if body: out.append((role, body))
    return out
