# Source access limitations — promotion remains partial

The authenticated GitHub connection supports commits and branch updates; these have been used. Direct Git clone failed because no shell credential was available. No permission denial or operator-choice blocker occurred.

- `code/D-Maestro/maestro-ai-music-system-main/Today.txt` (184731 bytes; Git blob `dab487853a34922d3798e0b38c1c640e6207f2b7`): Connector UTF-8 decoding fails or normalized text cannot match original blob bytes; historical object preserved unchanged remotely. No exact full-occurrence audit claimed.
- `untracked/SYSTEM_GRAPH_IMPROVED.json` (7435400 bytes; Git blob `7d93baa89c17f3f3eff3e642dbe86a8e86baf0fa`): Connector UTF-8 decoding fails or normalized text cannot match original blob bytes; historical object preserved unchanged remotely. No exact full-occurrence audit claimed.

For Today.txt, the connector returned normalized text, including non-UTF-8 replacement characters; its encoded bytes did not match the pinned blob. For SYSTEM_GRAPH_IMPROVED.json, the content API returned an empty body and the blob endpoint failed UTF-8 decoding; a ranged/base64 retry also returned no content. Both remain historical-only for current authority, but unseen text cannot be exhaustively occurrence-classified.

Other opaque historical assets, preserved remotely and listed in SOURCE_LIMITATIONS.json, include PDFs/OXPS/drawing content and the unrelated external gitlink. Their presence is not evidence that O-12 cover assets were recovered. The 60 MB legacy/context.md was recovered separately and verified byte-exact, so it is not a remaining blocker.

V1 full-corpus coverage cannot PASS. The current bundle repair, source-template synchronization, arithmetic regressions, reference integrity and deterministic rebuild do PASS. No merge to main is permitted under this run’s all-blocking-checks rule. Next required mechanical work is raw-byte retrieval and audit completion; no new architectural decision is requested.
