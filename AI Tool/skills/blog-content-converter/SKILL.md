---
name: blog-content-converter
description: Convert DOCX files to Markdown for blog publishing with automatic image extraction and GitHub URL generation. Supports MkDocs blog format with proper frontmatter, LaTeX math expressions, and progressive content loading.
---

# Blog Content Converter Skill

I am a skill that helps convert DOCX documents to well-formatted Markdown for blog publishing. I handle the complete workflow from document conversion to image management and blog deployment.

## Core Capabilities

- **Document Conversion**: Convert DOCX files to Markdown with proper formatting
- **Image Extraction**: Automatically extract images from DOCX and organize them for blog_image repository
- **Format Optimization**: Fix math expressions (LaTeX), tables, code blocks, and content structure
- **Blog Integration**: Generate proper frontmatter (YAML) for MkDocs blog plugin
- **GitHub Integration**: Generate GitHub raw URLs for images automatically
- **Progressive Loading**: Use layered documentation structure for efficient context management

## When to Use Me

Use this skill when you need to:
- Convert Word documents (DOCX) to blog-ready Markdown
- Publish technical articles with images and math expressions
- Maintain consistent blog formatting and structure
- Automate the blog publishing workflow

## Quick Start

1. **Basic Conversion**:
   ```
   Convert the DOCX file at [path] to Markdown for blog publishing
   ```

2. **With Custom Options**:
   ```
   Convert [docx_path] with category "技术", tags "AI,编程", title "My Article"
   ```

3. **Full Workflow**:
   ```
   Convert [docx_path], extract images, fix formatting, and prepare for deployment
   ```

## Progressive Loading Strategy

I use a layered approach to manage context efficiently:

### Layer 1: Core Instructions (SKILL.md)
- Essential workflow and capabilities
- Quick reference for common tasks
- This file - always loaded first

### Layer 2: Reference Documentation (reference.md)
- Detailed tool documentation
- Technical specifications
- API and configuration details
- Loaded when technical details are needed

### Layer 3: Examples (examples.md)
- Real-world usage scenarios
- Step-by-step workflows
- Common patterns and solutions
- Loaded for specific use cases

### Layer 4: Scripts and Tools (scripts/)
- Executable utilities
- Helper functions
- Loaded on-demand when execution is needed

## Key Principles

1. **Format Preservation**: Maintain document structure, headings, lists, and tables
2. **Math Expression Support**: Convert math formulas to proper LaTeX format ($$ for block, $ for inline)
3. **Image Management**: Extract images, organize by category, generate GitHub URLs
4. **Blog Standards**: Follow MkDocs Material theme conventions
5. **Error Handling**: Provide clear error messages and recovery suggestions

## Output Format

I generate Markdown files with:
- YAML frontmatter (title, date, categories, tags)
- Proper heading hierarchy
- LaTeX math expressions
- Code blocks with syntax highlighting
- Image references with GitHub raw URLs
- Excerpt separator (`<!-- more -->`)

## Integration Points

- **MkDocs**: Generates compatible Markdown for MkDocs Material theme
- **GitHub**: Creates image URLs pointing to blog_image repository
- **Blog Plugin**: Supports MkDocs blog plugin frontmatter format

For detailed technical information, see `reference.md`.
For usage examples, see `examples.md`.

