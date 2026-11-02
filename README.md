# AsenT1 — Free AI Director Skill

AsenT1 is a free, public Claude Skill for AI-video creators. It provides a structured director workflow for script reading, director design, blocking, shot/camera design, video prompt compilation, preflight and targeted repair.

**This public edition runs directly inside Claude. It does not require the private `asent1-core` repository, a remote MCP server, or a separate hosted service.**

## Public repository

`https://github.com/tonysen777/asent1`

## Use with Claude Managed Agents

Mount this public GitHub repository as a `github_repository` resource when creating a Managed Agents Session:

- Repository: `https://github.com/tonysen777/asent1`
- Branch: `main`
- Mount path: `/workspace/asent1`
- Skill entry: `.claude/skills/asent1-video-production/SKILL.md`

Managed Agents scans the repository root `.claude/skills/` directory at Session startup. It discovers each Skill at `.claude/skills/<skill-name>/SKILL.md`; no separate MCP server or entry in the Agent's `skills` array is required. The Agent's `read` tool must be enabled (enabled by default).

For a public repository, Anthropic's GitHub repository resource example uses a GitHub token with public-repository read access. Keep that token in your own secret store; never commit it here.

Start a new Session after a repository update because Skill discovery runs at Session startup and does not refresh a running Session.

Official Anthropic documentation:
- [Managed Agents — Skills](https://platform.claude.com/docs/en/managed-agents/skills)
- [Managed Agents — GitHub access](https://platform.claude.com/docs/en/managed-agents/github)
- [Claude Cookbook — Skills from a GitHub repository](https://platform.claude.com/cookbook/managed-agents-cma-use-skills-from-a-repo)

## Workflow

1. **Production reading:** identify source facts, events, dialogue, character and prop states, space, continuity, unknowns and conflicts.
2. **Director design:** analyze dramatic beats, audience information, performance, rhythm, blocking, shot function, camera, light and sound.
3. **Prompt compilation:** compile the approved design into complete, self-contained video-generation Units.
4. **Preflight:** check source fidelity, identity, spatial logic, axis, action causality, camera, light, sound and continuity.
5. **Targeted repair:** change the smallest variable responsible for a failed result while preserving dimensions that already work.

The Skill does not compile a final prompt before the user asks for it or approves the director design.

## Project separation

SSS1 remains a separate project. AsenT1 is the renamed continuation of the former KSR project; they are not merged.

## Public content and provenance

This repository contains a self-contained public Skill. It does not publish the former KSR source archive, private reference collections, raw tutorials, or unverified third-party materials. The public Skill describes an operational workflow and does not claim that private source files are remotely accessible.

The repository license applies only to files in this public repository. It does not grant rights to third-party course material, Skills, tutorials or source archives. See [NOTICE.md](NOTICE.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
