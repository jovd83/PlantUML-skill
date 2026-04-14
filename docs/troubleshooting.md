# PlantUML Troubleshooting

### 1. "dot" Not Found
- **Symptom:** You can render sequence diagrams, but Class or State diagrams throw a "Graphviz error".
- **Fix:** Ensure Graphviz is installed and the `dot` command works in terminal. Run `python scripts/render.py --setup` or manually add Graphviz to your system PATH.

### 2. Java Heap Space Error
- **Symptom:** Rendering a massive diagram fails with memory errors.
- **Fix:** Modify `scripts/render.py` to add `-Xmx2g` to the Java command:
  `cmd = ["java", "-Xmx2g", "-jar", JAR_PATH ...]`

### 3. Syntax Error at line X
- **Symptom:** PlantUML outputs a local file with a red error marker.
- **Fix:** Check for missing `@startuml` or `@enduml` wrappers. Ensure there are no reserved characters in labels without quotes (e.g., use `"Label (with brackets)"`).

### 4. Broken Images in VS Code/Markdown
- **Symptom:** SVG renders but icons/colors are missing.
- **Fix:** Ensure `!include assets/premium-theme.puml` is using a correct relative path from your `.puml` file.
