# Changelog

All notable changes to the `plantuml-skill` will be documented in this file.

## [1.2.0] - 2026-04-14
### Added
- Created `evals/evals.json` with 3 complex test cases (Sequence, C4, State).
- Added professional `assets/premium-theme.puml` (Tokyonight-inspired).
- Added `references/syntax-guide.md` with verified C4 library URLs.
- Added `references/troubleshooting.md`.

### Optimized
- Hardcoded `plantuml-stdlib` URLs in syntax-guide to prevent 404 errors.
- Improved `SKILL.md` description for better triggering and specificity.
- Fixed path resilience for nested `!include` statements.

## [1.1.0] - 2026-04-14
### Added
- Integrated self-healing provisioning logic in `scripts/render.py` (winget/brew/apt support).
- Automatic `plantuml.jar` download.

## [1.0.0] - 2026-04-14
### Added
- Initial release of the `plantuml-skill`.
- Core rendering functionality via Java/CLI.
