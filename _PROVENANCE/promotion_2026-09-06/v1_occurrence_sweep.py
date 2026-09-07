#!/usr/bin/env python3
"""V1 — full-corpus threshold-occurrence sweep (promotion 2026-09-06).

Closes the V1 coverage obligation recorded in LEDGER PROMOTION-2026-09-06 by
enumerating EVERY occurrence of the two disputed threshold token families across
every object the commit tracks, and classifying each by the surface it sits on.

Question V1 answers: does any occurrence anywhere in the corpus assert a CURRENT
universal numeric release floor, contradicting DEC-PROMO-01/02?

It is a corpus audit, not a runtime gate. It asserts nothing about deployed song
runtime. Historical occurrences are evidence and are never edited — only counted.

Coverage discipline (M16: absence is never assumed, only recorded):
  Layer A  raw-byte scan (latin-1 never fails) — catches every literal ASCII form.
  Layer B  decoded / container-extracted scan — catches forms Layer A cannot see
           (UTF-16 text, deflate-compressed OOXML/OXPS parts, PDF content streams).
An object is COVERED when Layer A ran and, where Layer B was required, it succeeded.

Usage: v1_occurrence_sweep.py [REPO_ROOT] [--out DIR]
Exit 0 = V1 PASS. Deterministic: same commit in, same bytes out.
"""
import sys, os, re, csv, json, zipfile, hashlib, subprocess, importlib.abc
import xml.etree.ElementTree as ET

# ---------------------------------------------------------------- token families
# DEC-PROMO-01 song-local 97.5 target, and DEC-PROMO-02 historical G-Card >=7.0
# scalar. Regex-escaped forms ("97\.5") are matched too so validator/test sources
# that carry the pattern as source code are audited like any other occurrence.
# Boundaries matter: unbounded "97[.,]5\d*" also matches PDF font-BBox coordinates
# such as 997.55859. Only the bare value (97.5 / 97,5 / 97.50) is the disputed target.
TOKENS = (
    ('T97', re.compile(r'(?<![\d.,])97\\?[.,]50?(?![\d])')),
    ('TG7', re.compile(r'(?:G[-‑ ]?Card|\bG)\s*[≥>]=?\s*7(?:\.0)?\b'
                       r'|[≥]\s*7\.0\b|>=\s*7\.0\b')),
)

# ------------------------------------------------------------- surface classes
# Current-authority surfaces carry the promoted interpretation and are constrained.
# Everything else is preserved record and is counted, never constrained.
CURRENT_PREFIXES = ('maestro-current/',)
RECORD_PREFIXES = ('_PROVENANCE/',)

# The audit's own workspace is excluded from the corpus it audits. V1_OCCURRENCES.csv
# quotes 3,000+ threshold snippets verbatim, so scanning it would count this check's
# output as corpus evidence and the result would grow on every run. Excluding the whole
# packet directory (not just the machine outputs) keeps the figures stable across the
# commits that write the packet's own prose. Everything in here is provenance record,
# which the check never constrains — nothing constrained is skipped by this exclusion.
EXCLUDED_PREFIXES = ('_PROVENANCE/promotion_2026-09-06/',)

# A current-surface occurrence must sit inside a context window that marks it as
# historical, run-local, or as a deliberately rejected regression. Absent any
# marker it reads as a live universal floor -> V1 violation.
QUALIFIERS = (
    'historical', 'era history', 'era gate', 'its own era', 'own era',
    'run_local_valid', 'does not reinstate', 'not a current',
    'neither universally supersedes', 'identified song interaction',
    'stratum', 'reject', 'superseded global threshold semantics',
    'scope', 'authority_ref', 'fixture', 'never a current default',
)
WINDOW = 2  # lines of context each side

# Superseded phrasings that must never appear on a current surface. Mirrors
# validate_bundle.py check A5 so the corpus sweep and the bundle gate agree.
SUPERSEDED = re.compile(
    r'composite\s*[≥]\s*97\.5|release floor\s*\*\*97\.5'
    r'|locked operator values \(97\.5\)|floor 97\.5 terminal|97\.5 floor present')

# Non-textual assets: raster images, icons, a Windows shell link. Raw-scanned;
# no text extractor applies. Recorded by hash so the waiver is auditable, not tacit.
# Sniffed by magic bytes as well as extension: one asset here is a browser-cache
# blob with no extension at all.
ASSET_EXT = ('.ico', '.paint', '.lnk', '.png', '.jpg', '.jpeg', '.gif', '.webp')
ASSET_MAGIC = (b'\x89PNG\r\n\x1a\n', b'\xff\xd8\xff', b'GIF87a', b'GIF89a',
               b'\x00\x00\x01\x00', b'RIFF', b'L\x00\x00\x00\x01\x14\x02\x00')

# Objects that carry no auditable bytes in this commit. Waiving one is a recorded
# operator-visible act, never a silent pass: each names why V1 cannot reach it and
# why it is not a threshold-authority source. Residue rides OPEN, not this verdict.
WAIVED = {
    'untracked/momoneystudios-Exporting to Vercel':
        'Gitlink f13aa940e6649ddb2b539f501a4750a94ee10f7e with no .gitmodules and no '
        'checked-out bytes: a deployment-export pointer, not a Maestro doctrine source. '
        'No bytes exist in this commit to audit. Recorded in OPEN as V1 residue.',
}
ZIP_TEXT_EXT = ('.docx', '.pptx', '.xlsx')
TEXT_ENCODINGS = ('utf-8', 'utf-8-sig', 'utf-16', 'cp1252')


def block_broken_cryptography():
    """pypdf imports cryptography for encrypted PDFs; the rust bindings panic in
    some sandboxes and a panic is not an ImportError, so pypdf cannot fall back.
    Force the ImportError it already handles. No PDF here is encrypted."""
    class Block(importlib.abc.MetaPathFinder):
        def find_spec(self, name, path=None, target=None):
            if name == 'cryptography' or name.startswith('cryptography.'):
                raise ImportError('cryptography blocked: broken rust bindings')
            return None
    sys.meta_path.insert(0, Block())


def tracked_objects(root):
    out = subprocess.run(['git', '-C', root, 'ls-files', '-sz'],
                         capture_output=True, check=True).stdout
    for entry in out.split(b'\0'):
        if not entry:
            continue
        meta, path = entry.split(b'\t', 1)
        mode = meta.split(b' ', 1)[0].decode()
        yield mode, path.decode('utf-8')


def decode_text(raw):
    """UTF-16 is accepted only behind a BOM: without one it decodes arbitrary
    even-length bytes into plausible-looking garbage and would mask real content."""
    for enc in TEXT_ENCODINGS:
        if enc == 'utf-16' and not raw.startswith((b'\xff\xfe', b'\xfe\xff')):
            continue
        try:
            return raw.decode(enc), enc
        except UnicodeDecodeError:
            continue
    return None, None


def container_kind(raw, ext):
    """Format is decided by magic bytes first, extension second. Two PDFs in this
    corpus decode cleanly as cp1252/utf-16 by coincidence; routing them to a text
    scan would read their compressed streams as noise and miss their actual text."""
    if raw.startswith(b'%PDF'):
        return 'pdf'
    if raw.startswith(b'PK\x03\x04'):
        if ext == '.oxps':
            return 'oxps'
        if ext in ZIP_TEXT_EXT:
            return 'ooxml'
    if ext in ASSET_EXT or raw.startswith(ASSET_MAGIC):
        return 'asset'
    return None


def pdf_pages(path):
    import pypdf
    reader = pypdf.PdfReader(path)
    for i, page in enumerate(reader.pages, 1):
        yield 'page %d' % i, page.extract_text() or ''


def oxps_pages(path):
    with zipfile.ZipFile(path) as z:
        pages = [n for n in z.namelist() if n.lower().endswith('.fpage')]
        pages.sort(key=lambda n: [int(p) for p in re.findall(r'(\d+)', n)])
        for i, name in enumerate(pages, 1):
            root = ET.fromstring(z.read(name))
            text = ' '.join(g.get('UnicodeString', '')
                            for g in root.iter() if g.tag.endswith('Glyphs'))
            yield 'fpage %d (%s)' % (i, name), text


def ooxml_parts(path):
    with zipfile.ZipFile(path) as z:
        for name in sorted(z.namelist()):
            if not name.lower().endswith('.xml'):
                continue
            try:
                root = ET.fromstring(z.read(name))
            except ET.ParseError:
                continue
            yield 'part %s' % name, ' '.join(t for t in root.itertext())


def surface_of(rel):
    if rel.startswith(CURRENT_PREFIXES):
        return 'current'
    if rel.startswith(RECORD_PREFIXES):
        return 'record'
    return 'historical'


def find(text, layer, locator, rel, surface, lines=None):
    """Yield one record per token occurrence. `lines` enables line/window context
    for whole-file text; extracted container parts use the part as the window."""
    for family, pattern in TOKENS:
        for m in pattern.finditer(text):
            if lines is not None:
                line_no = text.count('\n', 0, m.start()) + 1
                lo, hi = max(0, line_no - 1 - WINDOW), line_no + WINDOW
                window = '\n'.join(lines[lo:hi])
                where = 'line %d col %d' % (line_no, m.start() - (text.rfind('\n', 0, m.start()) + 1) + 1)
            else:
                window = text
                where = locator
            snippet = ' '.join(text[max(0, m.start() - 60):m.start() + 60].split())
            qualified = any(q in window.lower() for q in QUALIFIERS)
            if surface == 'current':
                disposition = 'scoped' if qualified else 'VIOLATION_unqualified'
            else:
                disposition = 'historical_record' if surface == 'historical' else 'provenance_record'
            yield {'object': rel, 'surface': surface, 'layer': layer,
                   'locator': where, 'offset': m.start(), 'family': family,
                   'token': m.group(0), 'disposition': disposition,
                   'snippet': snippet}


def sweep(root, out_dir):
    block_broken_cryptography()
    occurrences, objects, unresolved, waived = [], [], [], []
    excluded = []
    for mode, rel in sorted(tracked_objects(root), key=lambda x: x[1]):
        if rel.startswith(EXCLUDED_PREFIXES):
            excluded.append(rel)
            continue
        path = os.path.join(root, rel)
        if mode == '160000':
            gitlink = subprocess.run(['git', '-C', root, 'ls-files', '-s', '--', rel],
                                     capture_output=True, text=True).stdout.split()[1]
            entry = {'object': rel, 'gitlink': gitlink}
            if rel in WAIVED:
                entry['waiver'] = WAIVED[rel]
                waived.append(entry)
            else:
                entry['reason'] = ('unresolvable gitlink: submodule pointer with no '
                                   '.gitmodules and no checked-out bytes')
                unresolved.append(entry)
            continue
        raw = open(path, 'rb').read()
        digest = hashlib.sha256(raw).hexdigest()
        ext = os.path.splitext(rel)[1].lower()
        surface = surface_of(rel)
        record = {'object': rel, 'sha256': digest, 'bytes': len(raw),
                  'surface': surface, 'layer_b': None, 'encoding': None}

        # Layer A — raw bytes. latin-1 is total: every literal ASCII token is seen.
        raw_text = raw.decode('latin-1')
        raw_hits = sum(1 for _ in find(raw_text, 'A', 'raw', rel, surface))

        kind = container_kind(raw, ext)
        text, encoding = (None, None) if kind else decode_text(raw)
        if kind == 'pdf':
            record['layer_b'] = 'pdf-extract'
            for locator, page in pdf_pages(path):
                occurrences.extend(find(page, 'B-pdf', locator, rel, surface))
        elif kind == 'oxps':
            record['layer_b'] = 'oxps-extract'
            for locator, page in oxps_pages(path):
                occurrences.extend(find(page, 'B-oxps', locator, rel, surface))
        elif kind == 'ooxml':
            record['layer_b'] = 'ooxml-extract'
            for locator, part in ooxml_parts(path):
                occurrences.extend(find(part, 'B-ooxml', locator, rel, surface))
        elif kind == 'asset':
            # Raster/shortcut asset: no text layer exists to extract. Layer A stands.
            record['layer_b'] = 'none-nontextual-asset'
        elif text is not None:
            record['encoding'] = encoding
            record['layer_b'] = 'text'
            lines = text.split('\n')
            occurrences.extend(find(text, 'B-text', 'text', rel, surface, lines))
        elif os.path.basename(rel).startswith('~$'):
            # Microsoft Office owner/lock file: holds the editing user's name and
            # uninitialized padding, never document text. Layer A stands.
            record['layer_b'] = 'none-office-owner-file'
        else:
            record['layer_b'] = 'none-opaque'
            entry = {'object': rel, 'sha256': digest}
            if rel in WAIVED:
                entry['waiver'] = WAIVED[rel]
                waived.append(entry)
            else:
                entry['reason'] = 'no decoder and no extractor for this byte format'
                unresolved.append(entry)
        record['raw_layer_a_hits'] = raw_hits
        objects.append(record)

    # Layer A backstop: any raw hit in an object whose Layer B found nothing is a
    # coverage discrepancy worth surfacing rather than silently trusting Layer B.
    by_object = {}
    for occ in occurrences:
        by_object.setdefault(occ['object'], 0)
        by_object[occ['object']] += 1
    discrepancies = [o['object'] for o in objects
                     if o['raw_layer_a_hits'] and not by_object.get(o['object'])
                     and o['layer_b'] not in ('none-nontextual-asset', 'none-opaque',
                                              'none-office-owner-file')]

    # Same scope as validate_bundle.py check A5: the bundle's documentation surface.
    # Build tooling is excluded because its regression test must contain the rejected
    # string in order to prove the gate rejects it.
    superseded_on_current = []
    for o in objects:
        if o['surface'] != 'current' or not o['object'].endswith('.md'):
            continue
        text = open(os.path.join(root, o['object']), 'rb').read().decode(o['encoding'])
        for m in SUPERSEDED.finditer(text):
            superseded_on_current.append({'object': o['object'], 'match': m.group(0)})

    violations = [o for o in occurrences if o['disposition'].startswith('VIOLATION')]
    verdict = ('PASS' if not violations and not unresolved
               and not superseded_on_current and not discrepancies else 'FAIL')

    os.makedirs(out_dir, exist_ok=True)
    occ_path = os.path.join(out_dir, 'V1_OCCURRENCES.csv')
    with open(occ_path, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=['object', 'surface', 'layer', 'locator',
                                           'offset', 'family', 'token',
                                           'disposition', 'snippet'])
        w.writeheader()
        for occ in sorted(occurrences, key=lambda o: (o['object'], o['offset'], o['family'])):
            w.writerow(occ)

    # Object register: every object V1 could not read as plain UTF-8 text, i.e. the
    # set whose coverage rests on a fallback encoding, a container extractor or a
    # declared waiver. These are the objects an auditor must be able to re-check.
    register = [o for o in objects
                if o['encoding'] not in ('utf-8', 'utf-8-sig')
                or o['layer_b'] != 'text']
    with open(os.path.join(out_dir, 'V1_OBJECTS.csv'), 'w', newline='',
              encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=['object', 'sha256', 'bytes', 'surface',
                                           'encoding', 'layer_b', 'raw_layer_a_hits'])
        w.writeheader()
        for o in sorted(register, key=lambda o: o['object']):
            w.writerow(o)

    counts = {}
    for occ in occurrences:
        counts[occ['disposition']] = counts.get(occ['disposition'], 0) + 1
    summary = {
        'check': 'V1 full-corpus threshold-occurrence coverage',
        'authority': 'DEC-PROMO-01, DEC-PROMO-02, DEC-PROMO-03',
        'verdict': verdict,
        'objects_scanned': len(objects),
        'objects_excluded_as_audit_workspace': sorted(excluded),
        'objects_needing_fallback_or_extraction': len(register),
        'objects_unresolved': unresolved,
        'objects_waived': waived,
        'occurrences_total': len(occurrences),
        'occurrences_by_disposition': dict(sorted(counts.items())),
        'occurrences_on_current_surfaces': sum(
            1 for o in occurrences if o['surface'] == 'current'),
        'superseded_phrasing_on_current_surfaces': superseded_on_current,
        'layer_a_vs_layer_b_discrepancies': discrepancies,
        'nontextual_assets_waived': sorted(
            o['object'] for o in objects
            if o['layer_b'] in ('none-nontextual-asset', 'none-office-owner-file')),
        'encodings_used': dict(sorted(
            (e, sum(1 for o in objects if o['encoding'] == e))
            for e in {o['encoding'] for o in objects if o['encoding']})),
    }
    with open(os.path.join(out_dir, 'V1_COVERAGE.json'), 'w', encoding='utf-8') as fh:
        json.dump(summary, fh, indent=2, sort_keys=True)
        fh.write('\n')
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if verdict == 'PASS' else 1


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    root = os.path.abspath(args[0]) if args else os.getcwd()
    out = os.path.join(root, '_PROVENANCE', 'promotion_2026-09-06')
    if '--out' in sys.argv:
        out = sys.argv[sys.argv.index('--out') + 1]
    sys.exit(sweep(root, out))
