# triad-validator — MOVED

This slice has been moved into the **rebirth** monorepo.

- **New home**: `rebirth/apps/triad-validator/`
- **Branch (at time of move)**: `claude/2026-05-20-day-1-rebirth-prep`
- **Commit**: `a9bdeb7` — feat(apps/triad-validator): import first productization slice
- **Date**: 2026-05-20

## Structural changes during the move

- Restructured to PyPA src-layout: `triad_validator/` → `src/triad_validator/`.
- `pyproject.toml` updated for src-layout (`[tool.setuptools.packages.find].where = ["src"]`,
  `[tool.pytest.ini_options].pythonpath = ["src"]`).
- Python build artifacts (`__pycache__/`, `.pytest_cache/`) are git-ignored at the
  rebirth root; they are not present in the canonical source.

## Status of this folder

This OneDrive folder is preserved as an archived snapshot. The authoritative
source is now the rebirth repository. Do not edit files here — edits will
not propagate.

If you need to refresh this archive from the canonical source:

```
# from the rebirth worktree root
rsync -av --delete apps/triad-validator/ \
  /mnt/c/Users/gamer/OneDrive/Maestro/maestro-ai-music-system-main/maestro/triad-validator/
```
