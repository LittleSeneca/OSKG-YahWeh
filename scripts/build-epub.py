#!/usr/bin/env python3
"""Convert Markdown paper to EPUB. Single-pass markdown conversion for footnote resolution."""
import re
import markdown
from ebooklib import epub
from pathlib import Path

INPUT = Path.home() / "Projects/Personal/OSKG-YahWeh/writing/el-yahweh-invention-of-monotheism.md"
OUTPUT = Path.home() / "Projects/Personal/OSKG-YahWeh/writing/el-yahweh-invention-of-monotheism.epub"

TITLE = "El, Yahweh, and the Invention of Monotheism"
AUTHOR = "Graham Brooks"

CSS = """
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
sup a { text-decoration: none; color: #0a66c2; }
em { font-style: italic; }
strong { font-weight: bold; }
hr { border: none; border-top: 1px solid #ccc; margin: 2em 0; }
.footnote { font-size: 0.9em; color: #555; }
.footnote ol { padding-left: 1.5em; }
.footnote li { margin: 0.4em 0; }
.footnote a { text-decoration: none; color: #0a66c2; }
.titlepage { text-align: center; margin-top: 4em; }
.titlepage h1 { font-size: 2em; margin-bottom: 0.5em; }
.titlepage .author { font-size: 1.2em; color: #555; margin-top: 2em; }
.footnotes-section { border-top: 1px solid #ccc; margin-top: 3em; padding-top: 1em; }
"""

def build_epub():
    md_text = INPUT.read_text()
    
    # Convert ENTIRE document at once so footnotes resolve
    html_full = markdown.markdown(
        md_text,
        extensions=["footnotes", "tables", "fenced_code"]
    )
    
    # Split HTML by H2 sections
    # Each <h2> starts a new section. Everything before first <h2> is title/intro.
    sections = re.split(r'(?=<h2>)', html_full)
    
    # Separate the title/intro from the H2 sections
    # First chunk is H1 title + intro text before first H2
    intro_html = sections[0]
    h2_sections = sections[1:]
    
    book = epub.EpubBook()
    book.set_identifier("oskg-yahweh-paper-001")
    book.set_title(TITLE)
    book.set_language("en")
    book.add_author(AUTHOR)
    
    css_item = epub.EpubItem(
        uid="style",
        file_name="style/default.css",
        media_type="text/css",
        content=CSS.encode("utf-8")
    )
    book.add_item(css_item)
    
    chapters = []
    spine = ["nav"]
    
    # Title page / intro chapter
    intro_chapter = epub.EpubHtml(
        title="Introduction",
        file_name="chapter_00.xhtml",
        lang="en"
    )
    intro_chapter.content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>{TITLE}</title>
    <link rel="stylesheet" type="text/css" href="style/default.css"/>
</head>
<body>
    <div class="titlepage">
        <h1>{TITLE}</h1>
        <p class="author">{AUTHOR}</p>
    </div>
    {intro_html}
</body>
</html>""".encode("utf-8")
    intro_chapter.add_item(css_item)
    book.add_item(intro_chapter)
    chapters.append(intro_chapter)
    spine.append(intro_chapter)
    
    # Process H2 sections
    for i, section_html in enumerate(h2_sections):
        # Extract the H2 title from the HTML
        title_match = re.search(r'<h2>(.*?)</h2>', section_html)
        section_title = title_match.group(1) if title_match else f"Section {i+1}"
        
        # Remove the H2 tag from body since we'll add it in the template
        body_html = re.sub(r'<h2>.*?</h2>\s*', '', section_html, count=1)
        
        # Check if this is the Notes section
        is_notes = 'Notes' in section_title
        
        chapter = epub.EpubHtml(
            title=section_title,
            file_name=f"chapter_{i+1:02d}.xhtml",
            lang="en"
        )
        
        notes_class = ' class="footnotes-section"' if is_notes else ''
        
        chapter.content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>{section_title}</title>
    <link rel="stylesheet" type="text/css" href="style/default.css"/>
</head>
<body>
    <h2>{section_title}</h2>
    <div{notes_class}>
    {body_html}
    </div>
</body>
</html>""".encode("utf-8")
        chapter.add_item(css_item)
        book.add_item(chapter)
        chapters.append(chapter)
        spine.append(chapter)
    
    # TOC
    book.toc = [(epub.Section(TITLE), chapters)]
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = spine
    
    epub.write_epub(str(OUTPUT), book, {})
    print(f"EPUB written to {OUTPUT}")
    print(f"Sections: {len(chapters)} (+ nav)")
    print(f"Size: {OUTPUT.stat().st_size:,} bytes")

if __name__ == "__main__":
    build_epub()
