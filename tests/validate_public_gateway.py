from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / ".claude" / "skills" / "asent1-video-production" / "SKILL.md"

def require(condition: bool, message: str) -> None:
    if not condition:
        print(f"FAIL: {message}", file=sys.stderr)
        raise SystemExit(1)

require(ENTRY.is_file(), "missing AsenT1 Skill entry")
skill = ENTRY.read_text(encoding="utf-8")

required_phrases = [
    "name: asent1-video-production",
    "version: 1.0.0",
    "Stage A — Production reading",
    "Stage B — Director analysis and design",
    "Stage C — Prompt compilation",
    "Independent Generation Unit rule",
    "Preflight before generation",
    "Targeted repair after generation",
    "No formal background music (BGM)",
]
for phrase in required_phrases:
    require(phrase.lower() in skill.lower(), f"missing Skill requirement: {phrase}")

require("does not require an AsenT1 MCP server" in skill,
        "Skill must state that public direct use does not require MCP")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
require("https://github.com/tonysen777/asent1" in readme,
        "README missing public repository URL")
require("does not require the private" in readme.lower(),
        "README must clarify that private core access is not required")
require("does not require an AsenT1 MCP server" in readme,
        "README must clarify that MCP is not required")

# The public repository must not contain private-core or quarantined source payloads.
for forbidden in ("source_archive", "private-core", "core-prompts",
                  "05_master_cases", "11_cinematography_language_database"):
    matches = [
        p for p in ROOT.rglob("*")
        if forbidden.lower() in p.as_posix().lower()
        and ".git" not in p.parts
    ]
    require(not matches, f"forbidden public path/content marker found: {forbidden}")

print("AsenT1 public Claude Skill validation: PASS")
