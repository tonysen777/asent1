# Claude Managed Agents Setup (Gateway)

This guide describes the intended integration. The AsenT1 MCP endpoint is not yet deployed; replace the placeholder only after the maintainer publishes the real URL.

## 1. Mount the public gateway repository

```python
resources = [{
    "type": "github_repository",
    "url": "https://github.com/tonysen777/asent1",
    "authorization_token": GITHUB_READ_TOKEN,
    "mount_path": "/workspace/asent1",
    "checkout": {"type": "branch", "name": "main"},
}]
```

The repository mount allows Managed Agents to discover `.claude/skills/asent1-video-production/SKILL.md`. A GitHub token with read-only access is sufficient for the public repository; do not put tokens in the repository.

## 2. Register the remote MCP server

Managed Agents declares the MCP URL on the Agent and attaches credentials through a Vault at Session creation. The exact URL and authentication scheme will be published after the service is deployed.

Illustrative Agent configuration (not executable until the endpoint is known):

```json
{
  "mcp_servers": [
    {"type": "url", "name": "asent1", "url": "https://ASENT1_MCP_ENDPOINT/mcp"}
  ],
  "tools": [
    {"type": "mcp_toolset", "mcp_server_name": "asent1"}
  ]
}
```

The service's authentication credential belongs in an Anthropic Vault, not in the Agent definition, Skill file or GitHub repository.

## 3. Create a new Session after updates

GitHub repository resources are resolved at Session initialization. A running Session does not automatically reload a later commit. Create a new Session to use updated gateway files.

## 4. Important distinction

The GitHub mount exposes only this public gateway repository. It does not grant users access to the private AsenT1 core repository. The hosted service accesses the core using server-side credentials that are never returned to clients.
