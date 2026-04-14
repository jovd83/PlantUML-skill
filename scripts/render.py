"""
PlantUML Professional Renderer & Provisioner (v2.0.0)
Standard: agentskills.io
"""
import os
import sys
import subprocess
import argparse
import logging
from pathlib import Path
from typing import Optional, List

# Configuration
PLANTUML_JAR_NAME = "plantuml.jar"
DEFAULT_ASSETS_DIR = Path(__file__).parent.parent / "assets"
DEFAULT_THEME_PATH = DEFAULT_ASSETS_DIR / "premium-theme.puml"

# Logging setup
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger("plantuml-manager")

class PlantUMLManager:
    def __init__(self, jar_path: Path):
        self.jar_path = jar_path
        self._check_java()

    def _check_java(self):
        try:
            subprocess.run(["java", "-version"], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            logger.error("Java (JRE) not found in system PATH.")
            sys.exit(1)

    def _check_graphviz(self) -> bool:
        dot_path = os.environ.get("GRAPHVIZ_DOT")
        if not dot_path:
            # Common paths check
            common_paths = [
                r"C:\Program Files\Graphviz\bin\dot.exe",
                "/usr/bin/dot",
                "/usr/local/bin/dot"
            ]
            for p in common_paths:
                if Path(p).exists():
                    os.environ["GRAPHVIZ_DOT"] = p
                    return True
            return False
        return Path(dot_path).exists()

    def setup(self):
        """Download JAR and verify environment."""
        logger.info("Verifying environment...")
        self.jar_path.parent.mkdir(parents=True, exist_ok=True)
        
        if not self.jar_path.exists():
            import urllib.request
            url = f"https://github.com/plantuml/plantuml/releases/latest/download/{PLANTUML_JAR_NAME}"
            logger.info(f"Downloading PlantUML from {url}...")
            urllib.request.urlretrieve(url, self.jar_path)
            logger.info("Download complete.")

        if not self._check_graphviz():
            logger.warning("Graphviz 'dot' not found. Structural diagrams may fail.")
            logger.info("Recommendation: Install via 'winget install graphviz' or 'brew install graphviz'.")

    def render(self, input_file: Path, output_dir: Path, formats: List[str]):
        """Render a .puml file to specified formats."""
        if not input_file.exists():
            logger.error(f"Input file not found: {input_file}")
            return

        output_dir.mkdir(parents=True, exist_ok=True)

        for fmt in formats:
            cmd = ["java", "-jar", str(self.jar_path), f"-t{fmt}", "-o", str(output_dir), str(input_file)]
            logger.info(f"Rendering {fmt.upper()}: {input_file.name}...")
            
            try:
                subprocess.run(cmd, check=True, capture_output=True)
                logger.info(f"Successfully rendered {input_file.name} to {output_dir}")
            except subprocess.CalledProcessError as e:
                logger.error(f"Rendering failed for {fmt}:\n{e.stderr.decode()}")

def main():
    parser = argparse.ArgumentParser(description="PlantUML Professional Renderer CLI")
    parser.add_argument("--setup", action="store_true", help="Provision dependencies")
    parser.add_argument("--input", type=str, help="Source .puml file")
    parser.add_argument("--output", type=str, default=".", help="Output directory")
    parser.add_argument("--format", type=str, default="svg", help="Comma-separated formats (svg,png)")
    parser.add_argument("--theme", action="store_true", help="Inject premium theme (conceptual)")

    args = parser.parse_args()
    
    jar_path = DEFAULT_ASSETS_DIR / PLANTUML_JAR_NAME
    manager = PlantUMLManager(jar_path)

    if args.setup:
        manager.setup()
        return

    if args.input:
        formats = args.format.split(",")
        manager.render(Path(args.input), Path(args.output), formats)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
