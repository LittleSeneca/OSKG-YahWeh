# Google Books Scraper (gbscraper)

Install via Homebrew: `brew install shloop/tap/google-book-scraper`
Binary: `gbscraper`

## Usage

```
gbscraper -f pdf -o ./output_dir "https://books.google.com/books?id=BOOK_ID"
```

### Key options

- `-f pdf` — output format (must come BEFORE URL; positional args error otherwise)
- `-o <dir>` — output directory
- `-t .com` — TLD override (try `.com` if `.us` default fails with "No downloadable pages found")
- `-m full` — download all available pages (vs. `single` default)

## Limitations

- **Authentication required for full previews.** Books the user can see when signed into Google may NOT be accessible to the scraper. "No downloadable pages found" often means the book requires auth.
- **Limited preview books.** Google Books "snippet view" or "selected pages only" books will only yield what's publicly available — typically TOC, index, and a few pages.
- **Bot detection.** Direct curl to `books.google.com` returns "We're sorry... your computer or network may be sending automated queries." Use the scraper (which manages rate limiting) or Camofox browser.

## When to give up

If the scraper returns "No downloadable pages found" even with `-t .com` and `-m full`, the book is not scrapeable. Fall back to:
1. Library Genesis / Anna's Archive
2. Internet Archive
3. User finding a downloadable PDF

## Example: Zevit's The Religions of Ancient Israel

- URL: `https://books.google.com/books?id=db4hr55j0yYC`
- Google Books shows: "No eBook available" + "Selected pages" only
- Scraper result: "No downloadable pages found" — FAILED
- Resolution: Book not available via Google Books preview; need alternate source
