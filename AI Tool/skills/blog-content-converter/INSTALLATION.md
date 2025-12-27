# Installation Guide

## For Claude Code

1. Copy the skill directory to Claude Code skills location:
   ```bash
   cp -r skills/blog-content-converter ~/.claude/skills/
   ```

2. Verify installation:
   ```bash
   ls ~/.claude/skills/blog-content-converter
   ```

3. The skill will be automatically discovered. You can use it by referencing:
   ```
   Use the blog-content-converter skill to convert [docx_file]
   ```

## For Codex

1. Copy the skill directory to Codex skills location:
   ```bash
   cp -r skills/blog-content-converter ~/.codex/skills/
   ```

2. Verify installation:
   ```bash
   ls ~/.codex/skills/blog-content-converter
   ```

3. Check available skills:
   ```bash
   codex skills list
   ```

4. Use the skill:
   ```
   Use blog-content-converter to convert [docx_file] to Markdown
   ```

## Skill Structure Verification

After installation, the skill directory should contain:

```
blog-content-converter/
├── SKILL.md                    # ✅ Core skill definition
├── reference.md                 # ✅ Technical documentation
├── examples.md                  # ✅ Usage examples
├── scripts/                     # ✅ Executable tools
│   ├── convert_docx_to_markdown.py
│   ├── requirements.txt
│   └── README.md
├── README.md                    # ✅ Overview
├── INSTALLATION.md              # ✅ This file
└── CONVERSATION_SUMMARY.md      # ✅ Development history
```

## Dependencies

The skill requires Python 3.9+ and the following package:

```bash
pip install python-docx>=1.1.0
```

Install from the scripts directory:
```bash
cd scripts
pip install -r requirements.txt
```

## Testing

Test the skill with a sample DOCX file:

```bash
cd scripts
python convert_docx_to_markdown.py --help
```

## Progressive Loading Verification

The skill uses progressive loading. Verify each layer:

1. **Layer 1 (SKILL.md)**: Loaded automatically when skill is referenced
2. **Layer 2 (reference.md)**: Loaded when technical details are needed
3. **Layer 3 (examples.md)**: Loaded for specific use cases
4. **Layer 4 (scripts/)**: Loaded when execution is required

## Troubleshooting

### Skill Not Discovered

- Check directory name matches exactly: `blog-content-converter`
- Verify SKILL.md exists and has proper YAML frontmatter
- Check skills directory path is correct

### Script Execution Fails

- Verify Python 3.9+ is installed
- Install dependencies: `pip install -r scripts/requirements.txt`
- Check file permissions on scripts

### Image Extraction Issues

- Ensure DOCX file is not corrupted
- Check images are embedded (not linked)
- Verify write permissions for blog_image directory

## Next Steps

After installation:
1. Read `SKILL.md` for core capabilities
2. Review `examples.md` for usage patterns
3. Check `reference.md` for technical details
4. Test with a sample DOCX file

