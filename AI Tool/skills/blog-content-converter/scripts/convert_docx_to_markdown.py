#!/usr/bin/env python3
"""
Convert DOCX to Markdown and handle images for blog publishing
Usage: python convert_docx_to_markdown.py <docx_file> [--category <category>] [--tags <tag1,tag2>]
"""

import os
import sys
import re
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Tuple, Optional

try:
    from docx import Document
    from docx.document import Document as DocumentType
    from docx.oxml.text.paragraph import CT_P
    from docx.oxml.table import CT_Tbl
    from docx.table import Table, _Row, _Cell
    from docx.text.paragraph import Paragraph
except ImportError:
    print("Error: python-docx is required. Install it with: pip install python-docx")
    sys.exit(1)

# Configuration - adjust paths relative to project root
PROJECT_ROOT = Path(__file__).parent.parent
BLOG_IMAGE_REPO = "laiyierjiangsu/blog_image"
BLOG_IMAGE_BASE_URL = f"https://raw.githubusercontent.com/{BLOG_IMAGE_REPO}/refs/heads/master"
DOCS_POSTS_DIR = PROJECT_ROOT / "docs" / "posts"
BLOG_IMAGE_DIR = PROJECT_ROOT / "blog_image" / "posts"


def extract_images_from_docx(docx_path: Path, output_dir: Path) -> dict:
    """
    Extract images from DOCX file and save them to output directory
    Returns a mapping of relationship IDs to file paths
    """
    image_map = {}
    doc = Document(str(docx_path))
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Extract images using a more reliable method
    # DOCX files store images in word/media/ directory
    # We need to access the package directly
    from zipfile import ZipFile
    
    image_count = 0
    try:
        with ZipFile(docx_path, 'r') as docx_zip:
            # List all files in the archive
            file_list = docx_zip.namelist()
            
            # Find all image files in word/media/ or media/
            image_files = [f for f in file_list if (f.startswith('word/media/') or f.startswith('media/')) and 
                          f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp'))]
            
            # Extract and save images
            for image_file in sorted(image_files):
                try:
                    # Read image data
                    image_data = docx_zip.read(image_file)
                    
                    # Get file extension
                    ext = Path(image_file).suffix.lower()
                    if not ext:
                        ext = '.png'  # Default
                    
                    # Generate filename
                    image_count += 1
                    image_filename = f"image_{image_count:02d}{ext}"
                    image_path = output_dir / image_filename
                    
                    # Save image
                    with open(image_path, 'wb') as f:
                        f.write(image_data)
                    
                    # Map the original filename to our saved path
                    # We'll need to match this with relationship IDs later
                    image_map[image_file] = image_path
                    print(f"  Extracted image: {image_path.name} (from {image_file})")
                except Exception as e:
                    print(f"  Warning: Failed to extract {image_file}: {e}")
    except Exception as e:
        print(f"  Warning: Failed to open DOCX as ZIP: {e}")
        # Fallback: try to use python-docx relationships
        try:
            for rel in doc.part.rels.values():
                target_ref = getattr(rel, 'target_ref', '')
                if target_ref and ('image' in target_ref.lower() or 
                                  target_ref.endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))):
                    try:
                        # Try to get image part
                        image_part = rel.target_part
                        if hasattr(image_part, 'blob'):
                            image_data = image_part.blob
                            
                            # Determine extension
                            ext = Path(target_ref).suffix or '.png'
                            
                            image_count += 1
                            image_filename = f"image_{image_count:02d}{ext}"
                            image_path = output_dir / image_filename
                            
                            with open(image_path, 'wb') as f:
                                f.write(image_data)
                            
                            image_map[rel.rId] = image_path
                            print(f"  Extracted image: {image_path.name} (rel_id: {rel.rId})")
                    except Exception as e2:
                        print(f"  Warning: Failed to extract image via relationship: {e2}")
        except Exception as e2:
            print(f"  Warning: Fallback method also failed: {e2}")
    
    return image_map


def convert_paragraph_to_markdown(paragraph: Paragraph, image_map: dict, category: str, image_list: List[Path] = None, image_counter: int = 0) -> Tuple[str, bool]:
    """Convert a paragraph to markdown format"""
    # Check for images first (images might be in runs)
    image_markdown = ""
    has_image = False
    
    # Check all runs for images
    for run in paragraph.runs:
        drawing_elements = run.element.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}drawing')
        if drawing_elements:
            # Found an image in this run
            # Use sequential image list as fallback
            if image_list and image_counter < len(image_list):
                image_path = image_list[image_counter]
                # Generate GitHub raw URL
                relative_path = image_path.relative_to(PROJECT_ROOT / "blog_image")
                image_url = f"{BLOG_IMAGE_BASE_URL}/{relative_path.as_posix()}"
                alt_text = paragraph.text.strip() if paragraph.text.strip() else "image"
                image_markdown = f"![{alt_text}]({image_url})\n\n"
                has_image = True
                break
            
            # Try to find the image reference from drawing element
            for drawing in drawing_elements:
                # Look for blip element which contains image reference
                blips = drawing.findall('.//{http://schemas.openxmlformats.org/drawingml/2006/main}blip')
                for blip in blips:
                    embed_id = blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                    if embed_id:
                        # Try to find image by relationship ID
                        image_path = None
                        if embed_id in image_map:
                            image_path = image_map[embed_id]
                        elif image_list and image_counter < len(image_list):
                            image_path = image_list[image_counter]
                        
                        if image_path and isinstance(image_path, Path):
                            # Generate GitHub raw URL
                            relative_path = image_path.relative_to(PROJECT_ROOT / "blog_image")
                            image_url = f"{BLOG_IMAGE_BASE_URL}/{relative_path.as_posix()}"
                            alt_text = paragraph.text.strip() if paragraph.text.strip() else "image"
                            image_markdown = f"![{alt_text}]({image_url})\n\n"
                            has_image = True
                            break
                if has_image:
                    break
            if has_image:
                break
    
    # Get text content
    text = paragraph.text.strip()
    
    # Check if paragraph has runs with formatting
    runs = paragraph.runs
    if runs and not has_image:
        result = ""
        for run in runs:
            run_text = run.text
            if run.bold:
                run_text = f"**{run_text}**"
            if run.italic:
                run_text = f"*{run_text}*"
            if run.underline:
                run_text = f"<u>{run_text}</u>"
            result += run_text
        text = result
    
    # Handle heading styles
    style = paragraph.style.name
    if 'Heading 1' in style or 'Title' in style:
        return f"# {text}\n\n" + image_markdown, has_image
    elif 'Heading 2' in style:
        return f"## {text}\n\n" + image_markdown, has_image
    elif 'Heading 3' in style:
        return f"### {text}\n\n" + image_markdown, has_image
    elif 'Heading 4' in style:
        return f"#### {text}\n\n" + image_markdown, has_image
    elif 'List Bullet' in style or 'List Paragraph' in style:
        return f"- {text}\n" + image_markdown, has_image
    elif 'List Number' in style:
        return f"1. {text}\n" + image_markdown, has_image
    
    # If we have an image, return it (with or without text)
    if has_image:
        return image_markdown + (f"{text}\n\n" if text else ""), True
    
    # Regular paragraph
    if not text:
        return "", False
    return f"{text}\n\n", False


def convert_table_to_markdown(table: Table) -> str:
    """Convert a table to markdown format"""
    markdown = []
    
    # Get header row
    if table.rows:
        header_row = table.rows[0]
        headers = [cell.text.strip() for cell in header_row.cells]
        markdown.append("| " + " | ".join(headers) + " |")
        markdown.append("| " + " | ".join(["---"] * len(headers)) + " |")
        
        # Get data rows
        for row in table.rows[1:]:
            cells = [cell.text.strip() for cell in row.cells]
            markdown.append("| " + " | ".join(cells) + " |")
    
    return "\n".join(markdown) + "\n\n"


def convert_docx_to_markdown(docx_path: Path, category: str = "技术", tags: List[str] = None) -> Tuple[str, dict]:
    """
    Convert DOCX file to markdown format
    Returns markdown content and image mapping
    """
    print(f"Reading DOCX file: {docx_path}")
    doc = Document(str(docx_path))
    
    # Extract images first
    category_dir = BLOG_IMAGE_DIR / category
    print(f"Extracting images to: {category_dir}")
    image_map = extract_images_from_docx(docx_path, category_dir)
    
    # Build a better mapping: create mapping from relationship IDs to image paths
    # Also create a sequential list of images for fallback
    image_list = sorted([path for path in image_map.values() if isinstance(path, Path)])
    rel_to_image = {}
    
    # Try to map relationship IDs to images by examining document structure
    from zipfile import ZipFile
    with ZipFile(docx_path, 'r') as docx_zip:
        # Read document.xml to find image relationships
        try:
            from xml.etree import ElementTree as ET
            doc_xml = docx_zip.read('word/document.xml')
            root = ET.fromstring(doc_xml)
            
            # Find all image references
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
                  'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
                  'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
            
            image_refs = []
            for blip in root.findall('.//a:blip', ns):
                embed_id = blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                if embed_id:
                    image_refs.append(embed_id)
            
            # Map relationship IDs to images in order
            for i, rel_id in enumerate(image_refs):
                if i < len(image_list):
                    rel_to_image[rel_id] = image_list[i]
        except Exception as e:
            print(f"  Warning: Could not parse document.xml for image mapping: {e}")
            # Fallback: use sequential mapping
            for i, rel in enumerate(doc.part.rels.values()):
                if i < len(image_list):
                    rel_to_image[rel.rId] = image_list[i]
    
    # Merge mappings
    image_map.update(rel_to_image)
    
    # Convert document content
    markdown_lines = []
    image_counter = 0  # Track images in document order
    
    # Process document elements
    for element in doc.element.body:
        if isinstance(element, CT_P):
            paragraph = Paragraph(element, doc)
            md, img_used = convert_paragraph_to_markdown(paragraph, image_map, category, image_list, image_counter)
            if img_used:
                image_counter += 1
            if md:
                markdown_lines.append(md)
        elif isinstance(element, CT_Tbl):
            table = Table(element, doc)
            md = convert_table_to_markdown(table)
            if md:
                markdown_lines.append(md)
    
    markdown_content = "".join(markdown_lines)
    
    # Clean up extra newlines
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
    
    return markdown_content, image_map


def generate_frontmatter(title: str, category: str, tags: List[str] = None) -> str:
    """Generate YAML frontmatter for the blog post"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    frontmatter = f"""---
title: {title}
date:
  created: {today}
  updated: {today}
categories:
  - {category}
"""
    
    if tags:
        frontmatter += "tags:\n"
        for tag in tags:
            frontmatter += f"  - {tag}\n"
    
    frontmatter += "---\n\n"
    return frontmatter


def find_excerpt_separator_position(content: str) -> int:
    """Find a good position to insert excerpt separator"""
    lines = content.split("\n")
    
    # Look for first heading after frontmatter
    for i, line in enumerate(lines[:30]):  # Check first 30 lines
        if line.startswith("#"):
            return i + 2
    
    # Look for first paragraph break
    for i, line in enumerate(lines[:20]):
        if line.strip() == "" and i > 5:
            return i + 1
    
    # Default: after 10 lines
    return min(10, len(lines) - 1)


def main():
    parser = argparse.ArgumentParser(
        description="Convert DOCX to Markdown for blog publishing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  python convert_docx_to_markdown.py "../docs/posts/tech/AI/AI原生编程入门及其实践 副本.docx"
  
  # With custom category and tags
  python convert_docx_to_markdown.py "../docs/posts/tech/AI/file.docx" --category "技术" --tags "AI,编程,实践"
  
  # With custom title and output path
  python convert_docx_to_markdown.py "../docs/posts/tech/AI/file.docx" --title "My Article" --output "../docs/posts/tech/AI/MyArticle.md"
        """
    )
    parser.add_argument("docx_file", type=str, help="Path to DOCX file (relative to project root or absolute)")
    parser.add_argument("--category", type=str, default="技术", help="Blog category (default: 技术)")
    parser.add_argument("--tags", type=str, help="Comma-separated tags (e.g., AI,Python)")
    parser.add_argument("--title", type=str, help="Blog post title (default: filename)")
    parser.add_argument("--output", type=str, help="Output markdown file path (default: auto-generated)")
    parser.add_argument("--no-excerpt", action="store_true", help="Don't add excerpt separator")
    
    args = parser.parse_args()
    
    # Parse arguments
    docx_path = Path(args.docx_file)
    if not docx_path.is_absolute():
        # Try relative to project root first
        docx_path = PROJECT_ROOT / docx_path
        if not docx_path.exists():
            # Try relative to current directory
            docx_path = Path(args.docx_file)
    
    if not docx_path.exists():
        print(f"Error: File not found: {docx_path}")
        sys.exit(1)
    
    category = args.category
    tags = [tag.strip() for tag in args.tags.split(",")] if args.tags else []
    title = args.title or docx_path.stem
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
        if not output_path.is_absolute():
            output_path = PROJECT_ROOT / output_path
    else:
        # Auto-generate output path based on category
        # Map category to directory
        category_map = {
            "技术": "tech",
            "生活": "life"
        }
        category_dir = category_map.get(category, "tech")
        
        # Try to infer subcategory from docx location
        docx_parent = docx_path.parent
        if "AI" in str(docx_parent) or "ai" in str(docx_parent).lower():
            subcategory = "AI"
        elif "Native" in str(docx_parent):
            subcategory = "Native"
        elif "Web" in str(docx_parent):
            subcategory = "Web"
        elif "Misc" in str(docx_parent):
            subcategory = "Misc"
        else:
            subcategory = category_dir
        
        output_path = DOCS_POSTS_DIR / category_dir / subcategory / f"{docx_path.stem}.md"
    
    # Create output directory
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print("DOCX to Markdown Converter")
    print("=" * 60)
    print(f"Input file: {docx_path}")
    print(f"Category: {category}")
    print(f"Tags: {tags if tags else 'None'}")
    print(f"Title: {title}")
    print(f"Output: {output_path}")
    print("=" * 60)
    print()
    
    # Convert DOCX to markdown
    try:
        markdown_content, image_map = convert_docx_to_markdown(docx_path, category, tags)
        
        # Generate frontmatter
        frontmatter = generate_frontmatter(title, category, tags)
        
        # Combine frontmatter and content
        full_content = frontmatter + markdown_content
        
        # Add excerpt separator if not present and not disabled
        if not args.no_excerpt and "<!-- more -->" not in full_content:
            # Try to find a good place to insert excerpt separator
            lines = full_content.split("\n")
            insert_pos = find_excerpt_separator_position(full_content)
            lines.insert(insert_pos, "\n<!-- more -->\n")
            full_content = "\n".join(lines)
        
        # Write markdown file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_content)
        
        print()
        print("=" * 60)
        print("✓ Conversion completed successfully!")
        print("=" * 60)
        print(f"✓ Markdown file: {output_path}")
        print(f"✓ Extracted {len(image_map)} images to: {BLOG_IMAGE_DIR / category}")
        print()
        print("Next steps:")
        print("1. Review and edit the markdown file if needed")
        print("2. Commit and push images to blog_image repository:")
        print(f"   cd blog_image && git add posts/{category} && git commit -m 'Add images' && git push")
        print("3. Commit and push the markdown file:")
        print(f"   git add {output_path.relative_to(PROJECT_ROOT)} && git commit -m 'Add new post' && git push")
        print("4. Build and deploy:")
        print("   mkdocs build && mkdocs gh-deploy")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Error during conversion: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

