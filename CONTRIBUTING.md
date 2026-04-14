# Contributing to PlantUML Skill

Thank you for your interest in improving the PlantUML Skill!

## Development Workflow
1.  **Edit `SKILL.md`**: Update the core instructions or contracts.
2.  **Test in `sandbox/`**: Generate a sample `.puml` and verify rendering with `python scripts/render.py`.
3.  **Run Evaluations**: Use `python scripts/evaluate_skill.py` to ensure no regressions in common Use Case or C4 patterns.
4.  **Update `docs/`**: Ensure the syntax guide or troubleshooting notes reflect your changes.

## Quality Standards
- All diagrams should support **both SVG and PNG**.
- Diagrams should use the **premium-theme.puml** by default.
- C4 diagrams must use **verified stdlib URLs**.
