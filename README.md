# PlantUML Professional Skill (v2.0)

[![Validate Skills](https://github.com/jovd83/plantuml-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/jovd83/plantuml-skill/actions/workflows/ci.yml)
[![version](https://img.shields.io/badge/version-2.0.0-orange)](CHANGELOG.md)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Maintainability](https://img.shields.io/badge/maintainability-high-brightgreen)](CONTRIBUTING.md)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jovd83)

## 📖 Overview
`plantuml-skill` is an enterprise-grade agentic engine for rendering professional PlantUML and C4 diagrams. It enables high-fidelity "Diagrams as Code" with modern aesthetics and autonomous dependency management.

## 🌟 Key Features (v2.0)
- **Contract-Driven**: Explicit Input/Output JSON schemas for pipeline integration.
- **Self-Healing**: Autonomous detection and installation of Java and Graphviz.
- **Premium Aesthetics**: Built-in "Tokyonight" theme for consistent, professional output.
- **C4 Expertise**: Hardened support for C4 Model diagrams with verified stdlib URLs.

## 🛠 Prerequisites
The skill features a **self-healing setup script** (Python 3.x), but generally requires:
1.  **Java (JRE 8+):** Required to run the PlantUML core.
2.  **Graphviz (dot):** Required for all structural diagrams (Class, Use Case, etc.).

## 📥 Installation
```bash
npx skills add https://github.com/jovd83/plantuml-skill --skill plantuml-skill
# Provision dependencies automatically
python scripts/render.py --setup
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
Best for: Dynamic snapshots of system states at a specific point in time.
![Object](sandbox/output/object.png)

### 10. Timing Diagram
Best for: Real-time signal processing and hardware timing.
![Timing](sandbox/output/timing.png)

---

Developed for the **AgentSkills.io** ecosystem by **Antigravity**.
