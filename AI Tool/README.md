# AI Tool - Skills Collection

This directory contains AI Skills that can be used with Claude Code and Codex.

## Directory Structure

```
AI Tool/
└── skills/
    ├── blog-content-converter/    # Blog content conversion skill
    └── [future-skills]/           # Additional skills will be added here
```

## Available Skills

### blog-content-converter

Converts DOCX files to Markdown for blog publishing with automatic image extraction and GitHub URL generation.

**Installation**: See `skills/blog-content-converter/INSTALLATION.md`

**Usage**: See `skills/blog-content-converter/SKILL.md`

## Adding New Skills

When adding a new skill:

1. Create a new directory under `skills/`
2. Follow the standard skill structure:
   - `SKILL.md` - Core skill definition
   - `reference.md` - Technical documentation
   - `examples.md` - Usage examples
   - `scripts/` - Executable tools (if needed)
   - `README.md` - Skill overview
   - `INSTALLATION.md` - Installation guide

3. Use progressive loading design:
   - Layer 1: SKILL.md (always loaded)
   - Layer 2: reference.md (loaded on demand)
   - Layer 3: examples.md (loaded on demand)
   - Layer 4: scripts/ (loaded when execution needed)

## Installation

Each skill has its own installation instructions. See the skill's `INSTALLATION.md` file.

## License

See main project license.

