#!/usr/bin/env python3
"""Convert Markdown paper to EPUB using EbookLib. Clean rebuild."""
import re
import markdown
from ebooklib import epub
from pathlib import Path

INPUT = Path.home() / "Projects/Personal/OSKG-YahWeh/writing/el-yahweh-invention-of-monotheism.md"
OUTPUT = Path.home() / "Projects/Personal/OSKG-YahWeh/writing/el-yahweh-invention-of-monotheism.epub"

TITLE = "El, Yahweh, and the Invention of Monotheism"
AUTHOR = "Graham Brooks"

def read_markdown(path):
    with open(path, "r") as f:
        return f.read()

def split_sections(md_text):
    """Split at ## boundaries. First section (before any ##) is title/intro."""
    lines = md_text.split("\n")
    sections = []
    current_title = None
    current_lines = []
    first_section_done = False
    
    for line in lines:
        if line.startswith("## ") and not line.startswith("### "):
            if not first_section_done:
                # First ## found — everything before it is the intro
                if current_lines:
                    sections.append((None, "\n".join(current_lines).strip()))
                first_section_done = True
                current_title = line[3:].strip()
                current_lines = []
            else:
                if current_lines:
                    sections.append((current_title, "\n".join(current_lines).strip()))
                current_title = line[3:].strip()
                current_lines = []
        else:
            current_lines.append(line)
    
    if current_lines:
        sections.append((current_title, "\n".join(current_lines).strip()))
    
    return sections

def md_to_html(md_text):
    """Convert markdown to HTML. Strip the H1 title (it goes in the title page)."""
    # Remove the first H1 line, we'll handle it separately
    lines = md_text.split("\n")
    filtered = []
    skipped_h1 = False
    for line in lines:
        if not skipped_h1 and line.startswith("# ") and not line.startswith("## "):
            skipped_h1 = True
            continue
        filtered.append(line)
    
    html = markdown.markdown(
        "\n".join(filtered),
        extensions=["footnotes", "tables", "fenced_code", "codehilite"]
    )
    return html

def build_epub(input_path, output_path):
    md_text = read_markdown(input_path)
    sections = split_sections(md_text)
    
    book = epub.EpubBook()
    book.set_identifier("oskg-yahweh-paper-001")
    book.set_title(TITLE)
    book.set_language("en")
    book.add_author(AUTHOR)
    
    # CSS
    style = """
    body { font-family: Georgia, serif; line-height: 1.6; margin: 1em 2em; }
    h1 { font-size: 1.8em; margin-top: 1.5em; text-align: center; }
    h2 { font-size: 1.4em; margin-top: 2em; }
    h3 { font-size: 1.15em; margin-top: 1.5em; }
    p { margin: 0.8em 0; text-indent: 0; }
    blockquote { margin: 1em 2em; font-style: italic; color: #333; border-left: 3px solid #ccc; padding-left: 1em; }
    table { border-collapse: collapse; margin: 1em 0; width: 100%; }
    th, td { border: 1px solid #ccc; padding: 0.4em 0.8em; text-align: left; }
    th { background: #f0f0f0; }
    sup { font-size: 0.8em; }
    em { font-style: italic; }
    strong { font-weight: bold; }
    hr { border: none; border-top: 1px solid #ccc; margin: 2em 0; }
    .footnote { font-size: 0.9em; color: #555; }
    .titlepage { text-align: center; margin-top: 4em; }
    .titlepage h1 { font-size: 2em; margin-bottom: 0.5em; }
    .titlepage .author { font-size: 1.2em; color: #555; margin-top: 2em; }
    """
    
    css = epub.EpubItem(
        uid="style",
        file_name="style/default.css",
        media_type="text/css",
        content=style.encode("utf-8")
    )
    book.add_item(css)
    
    chapters = []
    spine = ["nav"]
    
    for i, (title, content) in enumerate(sections):
        if title is None:
            # Title page / intro
            html_body = md_to_html(content)
            chapter = epub.EpubHtml(
                title="Introduction",
                file_name=f"chapter_00.xhtml",
                lang="en"
            )
            chapter.content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Introduction</title>
    <link rel="stylesheet" type="text/css" href="style/default.css"/>
</head>
<body>
    <div class="titlepage">
        <h1>{TITLE}</h1>
        <p class="author">{AUTHOR}</p>
    </div>
    {html_body}
</body>
</html>""".encode("utf-8")
        else:
            html_body = md_to_html(content)
            safe_name = re.sub(r'[^a-zA-Z0-9]+', '_', title).strip('_').lower()
            chapter = epub.EpubHtml(
                title=title,
                file_name=f"chapter_{i:02d}.xhtml",
                lang="en"
            )
            chapter.content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href="style/default.css"/>
</head>
<body>
    <h2>{title}</h2>
    {html_body}
</body>
</html>""".encode("utf-8")
        
        chapter.add_item(css)
        book.add_item(chapter)
        chapters.append(chapter)
        spine.append(chapter)
    
    # TOC
    book.toc = [(epub.Section(TITLE), chapters)]
    
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = spine
    
    epub.write_epub(str(output_path), book, {})
    print(f"EPUB written to {output_path}")
    print(f"Sections: {len(sections)} (+ nav)")
    print(f"Size: {output_path.stat().st_size:,} bytes")

if __name__ == "__main__":
    build_epub(INPUT, OUTPUT)
