# AsenS1 Video Production Skill

**AsenS1 v1.0.0-rc.1** · Claude Managed Agents · GitHub-mounted Skill

AsenS1 is an independent AI video directing and execution-compilation workflow.

`Original script → Fact preprocessing (when needed) → AsenS1 Director → Blocking / Shot / Camera → AsenS1 Compiler → Preflight → Video generation → Targeted repair`

This repository is the canonical runtime source for AsenS1. Claude Managed Agents can mount this repository and discover `.claude/skills/asens1-video-production/SKILL.md` at session startup.

## Scope

- AsenS1 runs independently; it does not merge SSS1 or other independent directing systems.
- It does not include an MJ / ksrmj art-direction pipeline or character turnaround-sheet workflow.
- Heuristics and candidate resources are not unconditional rules.
- Internal source archives, third-party course PDFs, and unverified case/cinematography databases are excluded from this public candidate.

## Status

This is a public release candidate, not a stable release. See `docs/provenance-audit.md` for excluded materials and the remaining provenance/release gates. Do not treat this candidate as a final stable release until rights review and semantic regression testing are complete.

## Claude Managed Agents

Mount this repository as a `github_repository` resource. Ensure the Agent has the `read` tool enabled. At session startup, Managed Agents scans `.claude/skills/` and discovers `asens1-video-production`.

See [`docs/managed-agents.md`](docs/managed-agents.md) for mounting details, permissions, and update behavior.

## Validation

Run:

```bash
python tests/validate_repo.py
```

Then review `tests/regression_cases.md` against a live Managed Agents session.

## License

Original AsenS1 text materials for which the maintainer has the necessary rights are intended to be licensed under CC BY 4.0 (`LICENSE`). Validation and workflow code are licensed under MIT (`LICENSE-CODE`). See `NOTICE.md` and `docs/provenance-audit.md`. These licenses do not grant rights to third-party works.
