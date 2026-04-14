# PlantUML Professional Skill (v2.0)

[![Maintainability](https://img.shields.io/badge/maintainability-high-brightgreen)](CONTRIBUTING.md)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Standards](https://img.shields.io/badge/standards-agentskills.io-blueviolet)](SKILL.md)
[![PlantUML v2.0](https://img.shields.io/badge/version-2.0.0-orange)](CHANGELOG.md)

`plantuml-skill` is an enterprise-grade agentic engine designed to transform unstructured engineering context into high-fidelity, syntactically grounded, and visually premium diagrams. 

## 🌟 Why v2.0?
The v2.0 release transitions this repository from a simple rendering script to a robust **Diagramming-as-Code Framework**. 
- **Contract-Driven**: Explicit Input/Output JSON schemas for pipeline integration.
- **Self-Healing Provisioning**: Autonomous detection and installation of Java and Graphviz.
- **Premium Aesthetics**: Built-in "Tokyonight" theme for consistent, professional output.
- **C4 Architecture Expertise**: Hardened support for C4 Model diagrams with verified standard libraries.
- **Automated Validation**: Integrated evaluation framework for regression testing.

## 🛠 Prerequisites & Installation
The skill operates via a Python wrapper that manages all underlying dependencies.

### Automated Setup
```bash
npx skills add https://github.com/jovd83/plantuml-skill --skill plantuml-skill
# Provision Java/PlantUML/Graphviz automatically
python scripts/render.py --setup
```

## 🎨 Professional Visual Gallery
Explore the full capabilities of the engine in the [Visual Portfolio](sandbox/output/).

| Sequence | Architecture (C4) | State Machine |
|---|---|---|
| ![Sequence](sandbox/output/sequence.png) | ![C4](evals/iteration-1/eval-2/with_skill/outputs/banking_c4.png) | ![State](sandbox/output/order_state.png) |

> [Full Gallery available in docs/gallery.md](docs/gallery.md)

## 🏗 Repository Structure
```text
scripts/
  render.py          Professional CLI for rendering and provisioning
  evaluate_skill.py  Automated regression testing and reporting
docs/
  syntax-guide.md    Grounded UML and C4 syntax guardrails
  troubleshooting.md Recovery protocols for environment issues
evals/
  evals.json         Structured benchmark prompts
assets/
  plantuml.jar       The rendering engine
  premium-theme.puml Style definitions (Tokyonight)
SKILL.md             The Agent-facing instruction contract (v2.0)
```

## 🤝 Contributing
We welcome contributions to the syntax templates and theme definitions. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

**Developed for the AgentSkills.io Ecosystem.**
