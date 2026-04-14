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
- **CI Validated**: Automated structural and documentation checks via GitHub Actions.

## 🛠 Prerequisites
The skill features a **self-healing setup script**, but generally requires:
1.  **Java (JRE 8+):** Required to run the PlantUML core.
2.  **Graphviz (dot):** Required for all structural diagrams (Class, Use Case, etc.).
3.  **Python 3.x:** To run the automation wrapper.

_Note: The skill will attempt to install these automatically via `winget`, `brew`, or `apt` if they are missing._

## 📥 Installation
```bash
npx skills add https://github.com/jovd83/PlantUML-skill --skill plantuml-skill
```

## 🎨 Visual UML Gallery

### 1. Sequence Diagram
Best for: API flows, user interactions, and message passing.
![Sequence](sandbox/output/sequence.png)

### 2. Use Case Diagram
Best for: Mapping system boundaries and actor responsibilities.
![Use Case](sandbox/output/use_case.png)

### 3. Class Diagram (Domain Model)
Best for: Structural data modeling and object relationships.
![Class](sandbox/output/class_model.png)

### 4. Activity Diagram
Best for: Business processes and complex logic flows with swimlanes.
![Activity](sandbox/output/activity.png)

### 5. C4 Container Diagram
Best for: High-level software architecture and container boundaries.
![C4 Architecture](evals/iteration-1/eval-2/with_skill/outputs/banking_c4.png)

### 6. State Machine
Best for: Object lifecycles and application state management.
![State](sandbox/output/order_state.png)

### 7. Deployment Diagram
Best for: Physical infrastructure and network topology.
![Deployment](sandbox/output/deployment.png)

### 8. Component Diagram
Best for: Microservices architecture and internal system modules.
![Component](sandbox/output/architecture.png)

### 9. Object Diagram
Best for: Dynamic snapshots of system states.
![Object](sandbox/output/object.png)

### 10. Timing Diagram
Best for: Real-time signal processing and hardware timing.
![Timing](sandbox/output/timing.png)

## 📚 Documentation & Support
- [Syntax Guide](docs/syntax-guide.md): Standard notation and C4 library URLs.
- [Troubleshooting](docs/troubleshooting.md): Recovery steps for environment issues.
- [Changelog](CHANGELOG.md): Project evolution and version history.
- [Contributing](CONTRIBUTING.md): Guidelines for extending the skill.

---

**Developed for the AgentSkills.io Ecosystem.**
