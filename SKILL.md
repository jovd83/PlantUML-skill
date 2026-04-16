---
name: plantuml-skill
description: "Enterprise-grade engine for rendering professional PlantUML and C4 diagrams. Optimized for system architecture visualization, sequence flow modeling, and high-fidelity project documentation."
metadata:
    dispatcher-layer: execution
    dispatcher-lifecycle: active
  version: "2.2.0"
  author: "jovd83"
  dispatcher-output-artifacts: [plantuml_source, diagram_svg, diagram_png]
  dispatcher-input-artifacts: [architecture_notes, requirement_spec, code_context]
  dispatcher-capabilities: [puml-generation, architecture-visualization, automated-rendering]
  dispatcher-risk: low
  dispatcher-writes-files: true
  dispatcher-stack-tags: [documentation, plantuml, architecture, automation]
  dispatcher-accepted-intents: [generate_plantuml_diagram, visualize_puml_architecture, render_puml_source]
  dispatcher-category: documentation
---

# PlantUML Skill (v2.0)

## Mission
To transform unstructured engineering concepts into grounded, syntactically correct, and visually premium diagrams while managing all underlying infrastructure (Java, Graphviz) autonomously.

## 🧠 Cognitive Process (Think-Act-Verify)

### 1. Think
- **Grounding**: Extract actors, states, and relationships from the provided context.
- **Selection**: Choose the optimal diagram type (Sequence for logic, C4 for architecture, State for lifecycles).
- **Theme**: Always target the `assets/premium-theme.puml` for professional aesthetics.

### 2. Act (Generate & Render)
- **Drafting**: Write the `.puml` code. Use absolute paths for the `!include` if possible, or relative paths if the root is known.
- **Rendering**: Execute the renderer script:
  `python scripts/render.py --input <file>.puml --output <dir> --format svg,png`

### 3. Verify
- **Syntax Check**: Ensure no 404s for C4 libraries.
- **Visual Check**: Confirm the premium theme is active.
- **Artifact Check**: Verify both SVG (scalable) and PNG (compatible) files are produced.

## 📋 Input Contract (JSON)
```json
{
  "source_context": "string",
  "diagram_type": "sequence | c4 | state | class | activity",
  "output_name": "string (basename)",
  "use_premium_theme": true
}
```

## 📋 Output Contract (JSON)
```json
{
  "puml_file": "path/to/source.puml",
  "svg_file": "path/to/diagram.svg",
  "png_file": "path/to/diagram.png",
  "render_status": "success | failure"
}
```

## 🛡 Safeguards & Guardrails
- **Complexity Limit**: For diagrams exceeding 50 lines, suggest splitting into sub-diagrams.
- **C4 Library**: Only use `plantuml-stdlib/C4-PlantUML/master/` URLs.
- **Environment**: If rendering fails, run `python scripts/render.py --setup` once before retrying.

## 📚 Documentation
Refer to:
- `docs/syntax-guide.md`: UML and C4 syntax best practices.
- `docs/troubleshooting.md`: Recovery steps for Java/Graphviz issues.
- `CHANGELOG.md`: Version history and migration notes.
