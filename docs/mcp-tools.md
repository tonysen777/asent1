# AsenT1 Remote MCP Tool Contract (Draft)

Status: draft; tools are not live until a hosted MCP endpoint is deployed.

The public Skill expects these remote MCP tools. Names are stable API identifiers; schemas must be finalized before service release.

## `asent1_status`

Returns service version, availability, authentication state and remaining free quota. Must not return private repository details.

## `asent1_production_reading`

Input: user-provided script, relevant context, optional asset descriptions and project settings.
Output: production facts, character/scene/prop state, dialogue classification, chronology, unknowns and conflicts.

## `asent1_director_design`

Input: source material plus approved production-reading result.
Output: director proposal, dramatic beats, subject/information priorities, blocking, shot design, camera approach, sound and continuity handoffs.

## `asent1_compile_clip`

Input: approved director plan, target video model, duration/format constraints and reference-asset roles.
Output: self-contained generation-unit prompt(s), each with START STATE → EVENT → END STATE.

## `asent1_preflight`

Input: one or more compiled units.
Output: structured checks for source fidelity, spatial consistency, blocking, axis, dialogue ownership, asset responsibility, sound, continuity and model constraints.

## `asent1_repair`

Input: failed unit, observed failure, dimensions already passing.
Output: minimum necessary patch, preserving all passing dimensions.

## Contract requirements

- Each task must carry a request/session identifier so a multi-step workflow can preserve state.
- The server must not expose raw private prompt files or repository contents through tool results.
- Tool output should contain the task result and a concise explanation, not private chain-of-thought or internal source text.
- Apply authentication, rate limits, request-size limits and quota checks server-side.
- Never log user scripts or assets by default; if operational logs are needed, redact sensitive payloads.
- The server must disclose that it is a hosted service and explain retention/deletion behavior before public launch.
