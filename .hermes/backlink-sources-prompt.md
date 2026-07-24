# Session Prompt: Backlink Primary Source References

You are working in the Truth Project at `~/Projects/Personal/OSKG-YahWeh`. This session is ONE task: find every note that references a primary source and add Obsidian wikilinks back to the corresponding source note.

## The Source Notes (targets for wikilinks)

These 7 files live in `sources/primary-sources/`. You will link TO them FROM other notes.

| Source note file | Wikilink target |
|-----------------|-----------------|
| `ugaritic-baal-cycle.md` | `[[ugaritic-baal-cycle]]` |
| `elephantine-papyri.md` | `[[elephantine-papyri]]` |
| `key-inscriptions.md` | `[[key-inscriptions]]` |
| `lachish-ostraca.md` | `[[lachish-ostraca]]` |
| `mesha-stele.md` | `[[mesha-stele]]` |
| `tel-dan-stele.md` | `[[tel-dan-stele]]` |
| `ketef-hinnom.md` | `[[ketef-hinnom]]` |

## What to do

For each source note above, search ALL **chapter notes** (`notes/theology/`) AND **claim notes** (`notes/claims/`) for references to that source. When you find a clear reference, add the wikilink to the FIRST substantive mention of that source in each note.

Key principles:
- **Surgical, not rewrite.** Add `[[source-name]]` around the first mention. Do not change anything else in the note.
- **Use piped links where the text already names the source.** If the note says "the Mesha Stele" make it `[[mesha-stele|the Mesha Stele]]`. If it says "Kuntillet Ajrud" make it `[[key-inscriptions|Kuntillet Ajrud]]` (since Ajrud lives in key-inscriptions.md).
- **One wikilink per note per source.** Don't link every mention. First substantive reference only.
- **Skip vague references.** "Ugaritic texts" or "Elephantine community" is good. "as we saw previously" is not.

## Search terms for each source

### [[ugaritic-baal-cycle]]
Search for: `Ugarit`, `Ugaritic`, `Baal Cycle`, `KTU`, `Ras Shamra`, `Baal and`, `Canaanite pantheon`, `El and Baal`, `Rider of the Clouds`

### [[elephantine-papyri]]
Search for: `Elephantine`, `Yeb`, `Anat-Yahu`, `Anat-Bethel`, `Passover Letter`, `temple.*Elephantine`, `Jedaniah`, `Yedoniah`, `Cowley 21`, `Cowley 30`

### [[key-inscriptions]]
Search for: `Kuntillet Ajrud`, `Khirbet el-Qom`, `Deut 32:8`, `4QDeut`, `Soleb`, `Merneptah`, `Shasu`, `sons of God.*Deut`, `Elyon.*nations`

### [[lachish-ostraca]]
Search for: `Lachish`, `Lachish letters`, `Lachish ostraca`, `Hoshaiah`, `Azekah`, `fire signals`

### [[mesha-stele]]
Search for: `Mesha`, `Moabite Stone`, `Mesha Stele`, `Chemosh`, `vessels of YHWH`, `Moabite`

### [[tel-dan-stele]]
Search for: `Tel Dan`, `House of David`, `bytdwd`, `Hazael.*stele`, `Biran.*Naveh`

### [[ketef-hinnom]]
Search for: `Ketef Hinnom`, `silver amulet`, `Priestly Blessing.*amulet`, `Barkay.*silver`, `oldest biblical`

## Method

1. Load the `obsidian` skill first.
2. For each source note, load it briefly to understand what it covers.
3. Run `search_files` with `target="content"` on `~/Projects/Personal/OSKG-YahWeh/notes/theology/` AND `~/Projects/Personal/OSKG-YahWeh/notes/claims/` using the search terms above. Treat both directories with equal priority — a claim referencing "Elephantine" is just as important to link as a chapter note referencing it.
4. For each note that matches, read the relevant section, and add the wikilink via `patch` to the first substantive mention.
5. Track your work — keep a running count of notes modified per source.

## Do NOT

- Do NOT modify the source notes themselves (they already have their own cross-links)
- Do NOT add wikilinks to `missing-sources-audit.md` (that's an internal project doc)
- Do NOT rewrite or restructure notes — just add the wikilink
- Do NOT link every mention — first substantive reference only
- Do NOT guess — if a note mentions "Lachish" but it's about the archaeological site generally, not the ostraca, skip it

## Success looks like

After this session, a reader who opens any chapter note or claim note that references "the Elephantine papyri" can click through to `[[elephantine-papyri]]` and see the actual text of the Temple Petition and Passover Letter. The knowledge graph gains bidirectional links between primary sources and the claims built on them.
