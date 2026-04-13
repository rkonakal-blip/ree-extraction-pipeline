import os
import shutil
from pathlib import Path

def install_skills():
    # Paths
    project_root = Path(__file__).parent
    skills_source = project_root / "prompts"
    claude_dir = Path.home() / ".claude" / "commands"
    
    # Create .claude/commands if it doesn't exist
    claude_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy all .md files
    skill_files = list(skills_source.glob("*.md"))
    
    if not skill_files:
        print("No skill files found in prompts/")
        return
    
    print(f"Installing {len(skill_files)} skill files to {claude_dir}\n")
    
    for skill in skill_files:
        dest = claude_dir / skill.name
        shutil.copy2(skill, dest)
        print(f"  ✓ {skill.name}")
    
    print(f"\nDone! Run /orchestrate in Claude Code to start the pipeline.")

if __name__ == "__main__":
    install_skills()
