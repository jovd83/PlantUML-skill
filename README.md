# PlantUML Skill

[![Validate Skills](https://github.com/jovd83/plantuml-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/jovd83/plantuml-skill/actions/workflows/ci.yml)
[![version](https://img.shields.io/badge/version-2.2.0-blue)](CHANGELOG.md)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jovd83)

## 📖 Overview

`plantuml-skill` is a professional "Diagrams as Code" tool for AI agents and developers. It allows you to write, render, and export high-fidelity PlantUML diagrams with a curated, modern aesthetic.

Unlike basic diagram tools, this skill is optimized for **Software Architecture (C4 Model)**, complex system flows, and state machines, ensuring your documentation looks premium and technically accurate.

## 🚀 When to use this skill

- **System Design:** Visualizing microservices, database schemas, and infrastructure.
- **Process Mapping:** Documenting complex business logic, user journeys, or API authentication flows.
- **Architecture Reviews:** Creating C4 diagrams for technical design documents.
- **Legacy Documentation:** Turning source code or logs into readable sequence diagrams.
- **Education:** Generating clean visual aids for complex algorithms or lifecycles.

## 🛠 Prerequisites

The skill features a **self-healing setup script**, but generally requires:

1.  **Java (JRE 8+):** Required to run the PlantUML engine.
2.  **Graphviz (dot):** Required for all structural diagrams (Class, Use Case, etc.).
3.  **Python 3.x:** To run the `render.py` automation wrapper.

_Note: The skill will attempt to install these automatically via `winget`, `brew`, or `apt` if they are missing._

## 📥 Installation

```bash
npx skills add https://github.com/jovd83/plantuml-skill --skill plantuml-skill
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

## 📚 Documentation & Resources

For detailed guides, please refer to:

- [Syntax Guide](docs/syntax-guide.md): High-fidelity UML and C4 syntax patterns.
- [Troubleshooting Guide](docs/troubleshooting.md): Common fixes for Java and Graphviz environments.
