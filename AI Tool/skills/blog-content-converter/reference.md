# Blog Content Converter - Technical Reference

## Tool Architecture

### Main Script: `convert_docx_to_markdown.py`

Location: `AI Tool/convert_docx_to_markdown.py`

**Dependencies**:
- `python-docx>=1.1.0` - For DOCX parsing
- Python 3.9+ recommended

**Key Functions**:

1. **`extract_images_from_docx(docx_path, output_dir)`**
   - Extracts images from DOCX using ZIP file access
   - Supports images in `word/media/` or `media/` directories
   - Returns mapping of image paths to relationship IDs
   - Automatically determines image extensions

2. **`convert_paragraph_to_markdown(paragraph, image_map, category, image_list, image_counter)`**
   - Converts Word paragraphs to Markdown
   - Handles formatting (bold, italic, underline)
   - Processes headings (H1-H4)
   - Inserts images with GitHub URLs
   - Returns tuple: (markdown_string, image_used_boolean)

3. **`convert_table_to_markdown(table)`**
   - Converts Word tables to Markdown table format
   - Handles header rows and data rows

4. **`generate_frontmatter(title, category, tags)`**
   - Generates YAML frontmatter for MkDocs blog plugin
   - Includes creation and update dates
   - Supports categories and tags

5. **`convert_docx_to_markdown(docx_path, category, tags)`**
   - Main conversion function
   - Orchestrates image extraction and content conversion
   - Returns markdown content and image mapping

## Configuration

### Project Structure

```
project_root/
├── docs/posts/          # Blog posts directory
│   └── tech/AI/         # Category-based organization
├── blog_image/          # Image repository (separate git repo)
│   └── posts/
│       └── 技术/        # Category-based image organization
└── AI Tool/             # Tool directory
    ├── convert_docx_to_markdown.py
    └── blog-content-converter-skill/
```

### Environment Variables

- `MKDOCS_GIT_COMMITTERS_APIKEY` - Optional, for git-committers plugin

### Path Configuration

The script uses relative paths from project root:
- `DOCS_POSTS_DIR = docs/posts`
- `BLOG_IMAGE_DIR = blog_image/posts`
- `BLOG_IMAGE_BASE_URL = https://raw.githubusercontent.com/{repo}/refs/heads/master`

## Image Handling

### Extraction Method

1. Opens DOCX as ZIP file
2. Finds images in `word/media/` or `media/` directories
3. Extracts images with sequential naming: `image_01.png`, `image_02.jpg`, etc.
4. Saves to `blog_image/posts/{category}/`

### URL Generation

Images are referenced using GitHub raw URLs:
```
https://raw.githubusercontent.com/{repo}/refs/heads/master/posts/{category}/{filename}
```

### Image Matching

The script uses multiple strategies to match images:
1. Relationship ID mapping from document XML
2. Sequential matching based on image order
3. Filename matching from media paths

## Markdown Formatting Rules

### Math Expressions

- Block math: `$$formula$$`
- Inline math: `$formula$`
- Common conversions:
  - `y = w x + b` → `$$y = wx + b$$`
  - `MSE = \frac{1}{n}...` → `$$MSE = \frac{1}{n}...$$`

### Code Blocks

- YAML: ` ```yaml ... ``` `
- JSON: ` ```json ... ``` `
- Python: ` ```python ... ``` `
- Generic code: ` ``` ... ``` `

### Tables

- Converts Word tables to Markdown pipe tables
- Handles header rows with `---` separator
- Preserves cell content

### Headings

- Title → `# Heading`
- Heading 1 → `# Heading`
- Heading 2 → `## Heading`
- Heading 3 → `### Heading`
- Heading 4 → `#### Heading`

## Frontmatter Format

```yaml
---
title: Article Title
date:
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
categories:
  - 技术
tags:
  - AI
  - 编程
---
```

## Error Handling

### Common Issues

1. **Image Extraction Failures**
   - Warning messages for failed extractions
   - Continues with available images
   - Falls back to sequential matching

2. **Format Conversion Issues**
   - Preserves original text when format conversion fails
   - Logs warnings for debugging

3. **Path Resolution**
   - Handles both absolute and relative paths
   - Validates file existence before processing

## Command Line Interface

### Basic Usage

```bash
python convert_docx_to_markdown.py <docx_file> [options]
```

### Options

- `--category`: Blog category (default: "技术")
- `--tags`: Comma-separated tags
- `--title`: Custom article title
- `--output`: Custom output path
- `--no-excerpt`: Disable excerpt separator

### Examples

```bash
# Basic conversion
python convert_docx_to_markdown.py "../docs/posts/tech/AI/article.docx"

# With options
python convert_docx_to_markdown.py "article.docx" \
    --category "技术" \
    --tags "AI,编程,实践" \
    --title "My Article Title"
```

## Integration with Blog Workflow

### Deployment Steps

1. Convert DOCX to Markdown
2. Commit images to blog_image repository
3. Commit markdown to main repository
4. Build with `mkdocs build`
5. Deploy with `mkdocs gh-deploy`

### Git Workflow

```bash
# Images
cd blog_image
git add posts/{category}/
git commit -m "Add images for article"
git push

# Markdown
git add docs/posts/tech/AI/article.md
git commit -m "Add new post: Article Title"
git push
```

## Performance Considerations

- Image extraction: O(n) where n is number of images
- Document parsing: O(m) where m is document size
- Typical conversion time: 1-5 seconds for standard documents

## Limitations

- Complex Word formatting may not convert perfectly
- Embedded objects (not images) are not extracted
- Some advanced Word features may be lost
- Requires manual review for complex documents

