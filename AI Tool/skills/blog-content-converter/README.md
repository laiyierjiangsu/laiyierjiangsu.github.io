# Blog Content Converter Skill

A production-ready Skill for converting DOCX documents to blog-ready Markdown with automatic image extraction and GitHub integration.

## Quick Start

1. Place this skill directory in your Skills location:
   - Claude Code: `~/.claude/skills/`
   - Codex: `~/.codex/skills/`

2. The skill will be automatically discovered and available for use.

## Structure

```
blog-content-converter-skill/
├── SKILL.md          # Core instructions (always loaded)
├── reference.md      # Technical documentation (loaded on demand)
├── examples.md       # Usage examples (loaded on demand)
├── scripts/          # Executable tools (loaded on demand)
│   ├── convert_docx_to_markdown.py
│   ├── requirements.txt
│   └── README.md
└── README.md         # This file
```

## Progressive Loading

This skill uses progressive loading to optimize context usage:

1. **SKILL.md** - Loaded first, contains essential workflow
2. **reference.md** - Loaded when technical details needed
3. **examples.md** - Loaded for specific use cases
4. **scripts/** - Loaded when execution required

## Features

- ✅ DOCX to Markdown conversion
- ✅ Automatic image extraction
- ✅ GitHub URL generation
- ✅ Math expression formatting (LaTeX)
- ✅ Table and code block conversion
- ✅ MkDocs blog plugin integration
- ✅ Progressive content loading

## License

See main project license.

