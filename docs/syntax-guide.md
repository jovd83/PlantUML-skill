# PlantUML Syntax Hallucination Prevention

Follow these rules to ensure diagrams render correctly. DO NOT mix with Mermaid syntax.

## 1. Sequence Diagrams (The "Mermaid Trap")
- **Arrows:** Use `->` or `->>` for requests. Use `-->>` for returns. 
  - *Mermaid uses `-->` but PlantUML treats `--` as a dotted line!*
- **Activation:** Use `activate` and `deactivate` explicitly for cleaner lifelines.

## 2. Relationships (Class & Component)
- **Inheritance:** `Child <|-- Parent` (The triangle points to the Parent).
- **Composition:** `Whole *-- Part`
- **Aggregation:** `Whole o-- Part`

## 3. C4 Model Syntax
To use C4 architecture patterns, you **must** use these verified library URLs:
```plantuml
' For Container Diagrams
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

' For Component Diagrams
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml
```

> [!TIP]
> If you are working in a deeply nested directory, use an absolute path for the premium theme or simply copy `assets/premium-theme.puml` to your current folder to avoid `!include` path errors.

## 4. Common Formatting
- **Multi-line Notes:** `note right of User: This is a \n multi-line note \n end note`
- **Stereotypes:** Use `<< ... >>` to define node types (e.g., `participant Service << Cloud >>`).
