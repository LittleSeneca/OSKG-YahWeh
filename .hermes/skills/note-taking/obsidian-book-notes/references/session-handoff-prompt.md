# Session Handoff Prompt Template

When creating a prompt for the user to use in a new session to process a book, include ALL of the following:

## Required Elements

1. **Session directive**: "Start session in the [project name] ([path])."
2. **Project context**: What the project is, where the notes live, how many exist, key scholars.
3. **Skill loading**: "Load the obsidian-book-notes skill."
4. **File location**: Exact path to the extracted text.
5. **Book context**: What this book contributes, why it matters, who cites it, where it fits.
6. **Structure guidance**: Number of chapters, note granularity (one per chapter unless justified).
7. **Key focus areas**: 3-5 specific arguments or chapters to pay extra attention to, with why.
8. **Cross-reference targets**: Specific notes, scholars, and directory entries to link to.
9. **Anti-compression directive**: Explicit reminder that the default is one note per chapter, no multi-chapter combining.
10. **Commit + retrospective**: "Commit as you go. Final retrospective before declaring done."

## Template

```
Start session in the [project] ([path]). [2 sentences of project context: what, where, how many notes].

Load the obsidian-book-notes skill. Extracted text at [path].

[Book context: 2-4 sentences on why this book matters, who cites it, where it fits in the project.]

[Structure: X chapters/parts = Y notes minimum. One note per chapter. No combining.]

Pay special attention to:
- [Claim/area 1] — [why it matters]
- [Claim/area 2] — [why it matters]
- [Claim/area 3] — [what it connects to]

Cross-reference [specific notes/scholars/directory entries].

Commit as you go. Final retrospective before declaring done.
```

## Anti-Compression Boilerplate

Always include this line, verbatim: "One note per chapter — NO multi-chapter combining. If you find yourself thinking 'I can cover chapters X-Y in one note,' STOP. That's the compression instinct."

## When the Book Is a Priority

If the book fills a critical gap:
```
This is a PRIORITY book. It fills [specific gap] in the project.
```

## When the Book Has Been Compressed Before

If this is a redo:
```
Last time this book got [N] notes for [M] chapters. This time it gets [correct number].
```
