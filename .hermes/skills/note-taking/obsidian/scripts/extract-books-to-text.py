#!/usr/bin/env python3
"""Extract text from PDFs and EPUBs to plaintext files.
Usage: ~/.hermes/venv/bin/python3 extract_books.py <input_dir> <output_dir>
Requires: PyMuPDF (fitz), ebooklib, html2text (in ~/.hermes/venv)
"""
import sys, os
from pathlib import Path

def extract_pdf(filepath):
    import fitz
    doc = fitz.open(str(filepath))
    text_parts = []
    for i in range(len(doc)):
        t = doc[i].get_text("text")
        if t.strip():
            text_parts.append(f"\n--- PAGE {i+1} ---\n\n{t}")
    doc.close()
    return "\n".join(text_parts)

def extract_epub(filepath):
    from ebooklib import epub
    import html2text
    book = epub.read_epub(str(filepath))
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.body_width = 0
    text_parts = []
    for item in book.get_items():
        if item.get_type() == 9:  # ITEM_DOCUMENT
            content = item.get_content().decode('utf-8', errors='replace')
            text = h.handle(content)
            if text.strip():
                text_parts.append(text)
    return "\n\n".join(text_parts)

def main():
    if len(sys.argv) < 3:
        print("Usage: extract_books.py <input_dir> <output_dir>")
        print("  Reads all .pdf and .epub files from input_dir")
        print("  Writes .txt files to output_dir")
        sys.exit(1)
    
    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for src in sorted(input_dir.iterdir()):
        if src.suffix.lower() not in ('.pdf', '.epub'):
            continue
        
        name = src.stem[:80]  # truncate long filenames
        out_path = output_dir / f"{name}.txt"
        
        try:
            if src.suffix.lower() == '.pdf':
                text = extract_pdf(src)
            else:
                text = extract_epub(src)
            
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(f"# {name}\n\nSource: {src.name}\n\n---\n\n{text}")
            
            size_kb = out_path.stat().st_size // 1024
            print(f"✓ {name}: {size_kb} KB")
        except Exception as e:
            print(f"✗ {name}: {e}")

if __name__ == "__main__":
    main()
