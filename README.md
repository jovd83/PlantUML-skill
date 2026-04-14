# PlantUML Professional Skill (v2.0)

[![Validate Skill](https://github.com/jovd83/PlantUML-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/jovd83/PlantUML-skill/actions/workflows/ci.yml)
[![version](https://img.shields.io/badge/version-2.0.0-orange)](CHANGELOG.md)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Maintenance](https://img.shields.io/badge/maintenance-v2.0--flagship-blueviolet)](CONTRIBUTING.md)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jovd83)

## 📖 Overview
`plantuml-skill` is an enterprise-grade agentic engine for rendering professional PlantUML and C4 diagrams. It enables high-fidelity "Diagrams as Code" with modern aesthetics and autonomous dependency management.

## 🌟 Key Features (v2.0)
- **Contract-Driven**: Explicit Input/Output JSON schemas in [SKILL.md](SKILL.md).
- **Self-Healing**: Autonomous provisioning via [scripts/render.py](scripts/render.py).
- **Premium Aesthetics**: Built-in "Tokyonight" theme for consistent output.
- **CI Validated**: Automated structural checks via GitHub Actions.

## 🛠 Prerequisites
The skill features a **self-healing setup script**, but generally requires:
1.  **Java (JRE 8+):** Required to run the PlantUML core.
2.  **Graphviz (dot):** Required for all structural diagrams (Class, Use Case, etc.).

## 📥 Installation
```bash
npx skills add https://github.com/jovd83/PlantUML-skill --skill plantuml-skill
```

## 🎨 Visual UML Gallery

### 1. Sequence Diagram
<img src="sandbox/output/sequence.png" width="600" alt="Sequence">

### 2. Use Case Diagram
<img src="sandbox/output/use_case.png" width="600" alt="Use Case">

### 3. Class Diagram (Domain Model)
<img src="sandbox/output/class_model.png" width="600" alt="Class">

### 4. Activity Diagram
<img src="sandbox/output/activity.png" width="600" alt="Activity">

### 5. C4 Container Diagram
<img src="evals/iteration-1/eval-2/with_skill/outputs/banking_c4.png" width="600" alt="C4 Architecture">

### 6. State Machine
<img src="sandbox/output/order_state.png" width="600" alt="State">

### 7. Deployment Diagram
<img src="sandbox/output/deployment.png" width="600" alt="Deployment">

### 8. Component Diagram
<img src="sandbox/output/architecture.png" width="600" alt="Component">

### 9. Object Diagram
<img src="sandbox/output/object.png" width="600" alt="Object">

### 10. Timing Diagram
<img src="sandbox/output/timing.png" width="600" alt="Timing">

---

## 📚 Documentation & Support
- [Syntax Guide](docs/syntax-guide.md): Standard notation and C4 library URLs.
- [Troubleshooting](docs/troubleshooting.md): Recovery steps for environment issues.
- [Changelog](CHANGELOG.md): Project evolution and version history.
- [Contributing](CONTRIBUTING.md): Guidelines for extending the skill.

---

**Developed for the AgentSkills.io Ecosystem.**
