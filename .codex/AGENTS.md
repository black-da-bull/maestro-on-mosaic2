# Maestro developer tooling

Current repository guidance: `.agents/skills/maestro-on-mosaic2/SKILL.md`;
Claude companion: `.claude/skills/maestro-on-mosaic2/SKILL.md`.
Start with root README.md and `_PROVENANCE/STATE.md` to locate current authority.

`.codex/config.toml` only declares optional read-only role files. It does not configure
MCP servers, select a model, change approval/sandbox policy, or enable delegation.
Use already-authorized tools; any additional reviewed MCP connections belong in the
user's configuration. Credentials must not be committed.

`.claude/commands/feature-development.md` is an optional workflow scaffold.
The generated instincts file is retired; do not import its unsupported inferred rules.
