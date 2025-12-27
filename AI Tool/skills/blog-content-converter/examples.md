# Blog Content Converter - Usage Examples

## Example 1: Basic Document Conversion

**Scenario**: Convert a simple DOCX article to Markdown

**Input**:
```
Convert the DOCX file at docs/posts/tech/AI/my_article.docx to Markdown
```

**Process**:
1. Extract images from DOCX
2. Convert content to Markdown
3. Generate frontmatter
4. Save to appropriate location

**Output**:
- Markdown file: `docs/posts/tech/AI/my_article.md`
- Images: `blog_image/posts/技术/image_01.png`, etc.

## Example 2: Conversion with Custom Metadata

**Scenario**: Convert with specific category and tags

**Input**:
```
Convert article.docx with category "技术", tags "AI,机器学习,实践", title "AI原生编程入门"
```

**Process**:
1. Use custom category for image organization
2. Apply specified tags in frontmatter
3. Use custom title

**Output Frontmatter**:
```yaml
---
title: AI原生编程入门
date:
  created: 2025-12-27
  updated: 2025-12-27
categories:
  - 技术
tags:
  - AI
  - 机器学习
  - 实践
---
```

## Example 3: Full Workflow with Format Fixing

**Scenario**: Convert and optimize a technical document with math expressions

**Input Document Contains**:
- Math formulas: `y = w x + b`, `MSE = \frac{1}{n}...`
- Tables with data
- Code snippets
- Images

**Process**:
1. Extract all images
2. Convert math to LaTeX: `$$y = wx + b$$`
3. Convert tables to Markdown format
4. Format code blocks with syntax highlighting
5. Fix heading hierarchy
6. Insert images with GitHub URLs

**Output**:
- Properly formatted Markdown with:
  - LaTeX math expressions
  - Markdown tables
  - Syntax-highlighted code blocks
  - Image references with GitHub URLs

## Example 4: Batch Processing Multiple Documents

**Scenario**: Convert multiple DOCX files for a blog series

**Workflow**:
```bash
# Convert article 1
python convert_docx_to_markdown.py "article1.docx" --category "技术" --tags "AI"

# Convert article 2
python convert_docx_to_markdown.py "article2.docx" --category "技术" --tags "AI"

# Convert article 3
python convert_docx_to_markdown.py "article3.docx" --category "技术" --tags "AI"
```

**Result**:
- Three Markdown files ready for publishing
- All images organized in blog_image repository
- Consistent formatting across articles

## Example 5: Integration with CI/CD

**Scenario**: Automate blog publishing in GitHub Actions

**Workflow**:
1. Developer commits DOCX file
2. CI detects new DOCX
3. Runs conversion script
4. Commits generated Markdown
5. Builds and deploys blog

**GitHub Actions Example**:
```yaml
- name: Convert DOCX to Markdown
  run: |
    cd AI\ Tool
    python convert_docx_to_markdown.py "${{ github.workspace }}/docs/posts/tech/AI/article.docx"
  
- name: Commit Markdown
  run: |
    git add docs/posts/tech/AI/article.md
    git commit -m "Auto-convert: article" || exit 0
    git push
```

## Example 6: Handling Complex Documents

**Scenario**: Document with multiple sections, images, and math

**Challenges**:
- 10+ images scattered throughout
- Complex math expressions
- Nested lists and tables
- Code examples in multiple languages

**Solution**:
1. Extract all images sequentially
2. Match images to document positions
3. Convert math expressions systematically
4. Preserve document structure
5. Review and manually adjust if needed

**Result**:
- Well-structured Markdown
- All images properly referenced
- Math expressions correctly formatted
- Ready for blog publishing

## Example 7: Error Recovery

**Scenario**: Image extraction fails for some images

**Error**:
```
Warning: Failed to extract image rId5: '_Relationship' object has no attribute 'blob'
```

**Recovery**:
1. Script continues with available images
2. Uses sequential matching as fallback
3. Logs warnings for manual review
4. Generates Markdown with available images

**Manual Fix**:
- Review extracted images
- Manually add missing images if needed
- Update image references in Markdown

## Example 8: Progressive Content Loading

**Scenario**: Using the skill with progressive loading

**Layer 1 (SKILL.md)**:
- Load core instructions
- Understand basic workflow

**Layer 2 (reference.md)**:
- Load when technical details needed
- Understand tool architecture
- Check configuration options

**Layer 3 (examples.md)**:
- Load for specific use cases
- See real-world patterns
- Understand edge cases

**Layer 4 (scripts/)**:
- Load when execution needed
- Use helper utilities
- Run conversion tools

**Benefit**:
- Efficient context usage
- Faster response times
- Focused information retrieval

## Example 9: Format Optimization Workflow

**Scenario**: Post-conversion format improvements

**Initial Conversion**:
- Basic Markdown generated
- Some formatting issues

**Optimization Steps**:
1. Fix math expressions (add LaTeX delimiters)
2. Correct table formatting
3. Adjust heading hierarchy
4. Improve code block formatting
5. Add proper image alt text
6. Optimize list formatting

**Result**:
- Publication-ready Markdown
- Consistent formatting
- Proper structure

## Example 10: Multi-Repository Workflow

**Scenario**: Managing images in separate repository

**Setup**:
- Main repo: Blog content
- blog_image repo: Image assets

**Workflow**:
1. Convert DOCX (images extracted to blog_image)
2. Commit images to blog_image repo
3. Commit Markdown to main repo
4. Deploy both repositories

**Commands**:
```bash
# Step 1: Convert
python convert_docx_to_markdown.py article.docx

# Step 2: Commit images
cd blog_image
git add posts/技术/
git commit -m "Add images for article"
git push

# Step 3: Commit markdown
cd ..
git add docs/posts/tech/AI/article.md
git commit -m "Add new post"
git push

# Step 4: Deploy
mkdocs gh-deploy
```

