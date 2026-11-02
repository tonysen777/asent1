from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / ".claude" / "skills" / "asent1-video-production" / "SKILL.md"
assert ENTRY.exists(), "Missing AsenT1 public Skill entry"
text = ENTRY.read_text(encoding="utf-8")
assert "name: asent1-video-production" in text
assert "asent1_production_reading" in text
assert "asent1_compile_clip" in text

# Public gateway must not contain private-core payload directories.
for forbidden in ("references", "source_archive", "private-core", "core-prompts"):
    assert not any(p.name.lower() == forbidden for p in ROOT.rglob("*")), f"Forbidden directory: {forbidden}"

readme = (ROOT / "README.md").read_text(encoding="utf-8")
assert "尚未部署" in readme
print("AsenT1 public gateway validation: PASS")
