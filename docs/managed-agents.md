# Claude Managed Agents — Direct Public AsenT1 Skill

This guide mounts the public AsenT1 Skill from GitHub. It does **not** use the private `asent1-core` repository and does **not** require an AsenT1 MCP server.

## 1. Create a Session with the public repository

Use the GitHub repository resource when creating the Managed Agents Session:

```python
resources = [{
    "type": "github_repository",
    "url": "https://github.com/tonysen777/asent1",
    "authorization_token": GITHUB_READ_TOKEN,
    "mount_path": "/workspace/asent1",
    "checkout": {"type": "branch", "name": "main"},
}]
```

Anthropic's documented example uses a GitHub token with public-repository read access. Store the token in your own environment or secret store. Never paste it into chat or commit it to GitHub.

## 2. Skill discovery

At Session startup, Managed Agents scans the repository root at this exact pattern:

```text
.claude/skills/<skill-name>/SKILL.md
```

AsenT1's entry point is:

```text
.claude/skills/asent1-video-production/SKILL.md
```

No MCP server is needed. No separate entry in the Agent's `skills` array is needed. The Agent's built-in `read` tool must remain enabled; it is enabled by default.

## 3. Start a new Session after updates

Repository skill discovery runs once at Session startup. Commits pushed during an existing Session are not picked up by that Session. Start a new Session to load the latest `main` branch.

## 4. First-use instruction

After the Session starts, send Claude a task that clearly invokes the Skill, for example:

```text
Use the AsenT1 video-production Skill. First perform production reading only; do not compile the final video prompt yet.
```

For director design:

```text
Use AsenT1 to provide the director design, including dramatic beats, blocking, shot design, camera, lighting and sound. Do not compile the final prompt yet.
```

For compilation:

```text
Compile the approved AsenT1 director design into complete, self-contained Seedance video-generation Units.
```

## 5. Scope and limitations

The public Skill provides directing methodology and prompt-workflow instructions inside Claude. It does not itself call Seedance, generate video, provide a hosted API, or expose private AsenT1 core files. Video generation still takes place in the user's chosen video platform.
