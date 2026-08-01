# El, Yahweh, and the Invention of Monotheism


## Preface: How This Was Built

This essay was not written by reading seventeen books and forming an impression. It is the capstone of an Open Source Knowledge Graph (OSKG) project. The methodology comes from the Open Research Knowledge Graph (ORKG) at Leibniz University Hannover, where researchers have spent years building infrastructure to decompose scholarly literature into structured claims, connect them through typed relationships, and analyze the resulting graph for convergence and contradiction. The approach has been validated across biomedicine, computer science, and engineering. Cimino et al. (2025) recently extended it to cultural heritage texts, demonstrating that the pattern works for humanities domains. This project applies it to biblical studies and ancient Near Eastern religion for the first time.

The process used to take a scholar months of manual cross-referencing. It is now a data management workflow. Large language models handle the mechanical work: extracting claims from structured notes, proposing edges between related claims, identifying contradiction pairs across a corpus. A human evaluates every proposal, resolves ambiguities, and determines what the graph actually shows. Human-directed, LLM-accelerated. Every claim, every edge, and every synthesis conclusion was reviewed by a human before inclusion.

The project spent a month decomposing seventeen scholarly monographs into 723 discrete claims. The methodology matters because the conclusions carry exactly as much weight as the process that produced them.

### The Corpus

Seventeen books spanning the full ideological spectrum:

**The evolutionary consensus:** Mark S. Smith, *The Early History of God* (1990, rev. 2002) and *The Origins of Biblical Monotheism* (2001); Thomas Römer, *The Invention of God* (2015); John Day, *Yahweh and the Gods and Goddesses of Canaan* (2000); William G. Dever, *Did God Have a Wife?* (2005); Frank Moore Cross, *Canaanite Myth and Hebrew Epic* (1973); Daniel E. Fleming, *Yahweh Before Israel* (2021); Theodore J. Lewis, *The Origin and Character of God* (2020); Rainer Albertz, *A History of Israelite Religion in the Old Testament Period* (1994, 2 vols.); Othmar Keel and Christoph Uehlinger, *Gods, Goddesses, and Images of God in Ancient Israel* (1998); Francesca Stavrakopoulou, *God: An Anatomy* (2021).

**The early monotheism position:** Yehezkel Kaufmann, *The Religion of Israel* (1960); Philip D. Stern, "When Did Monotheism Emerge in Ancient Israel?" (*Biblical Archaeology Review*, 2025).

**The divine council position:** Michael S. Heiser, *The Unseen Realm* (2015) and "Are Yahweh and El Distinct Deities in Deut 32:8-9 and Psalm 82?" (*Hiphil* 3, 2006).

**The methodological counter-weight:** Jeffrey H. Tigay, *You Shall Have No Other Gods* (1986).

**The fluidity reframing:** Benjamin D. Sommer, *The Bodies of God and the World of Ancient Israel* (2009).

**The maximal skepticism position:** Konrad Schmid, *A Historical Theology of the Hebrew Bible* (2019).

Each book was read chapter by chapter, producing 149 structured notes. Those notes are the extraction substrate.

### How Claims Were Extracted

Each chapter note was decomposed into five to ten discrete claims. A claim, in this methodology, is one atomic, falsifiable assertion. "El was the original god of Israel." Not "Smith argues that Israelite religion developed from polytheism." The claim is what the scholar asserts to be true about the world.

Each claim became a standalone file with YAML frontmatter recording the scholar, source work, confidence rating (very-high to low), evidence type (biblical-text, archaeological, inscriptional, comparative-ANE, iconographic, onomastic), and topic tags. Total: 723 claims.

Confidence ratings are the scholar's own. If Mark Smith qualifies a conclusion with "it seems likely that," the claim is tagged MEDIUM. If he states it as "the evidence demonstrates," the claim is tagged HIGH. The ratings track the strength of the scholar's assertion. They are not an external evaluation of its truth.

### How Claims Were Connected

Claims were connected through typed edges in two passes. First pass: within a single scholar's body of work. What depends on what. What supports what. This captured the internal logic of each scholar's argument. Second pass: across scholars. Who contradicts whom. Where independent scholars converge on the same finding from different evidence. Where one argument logically depends on a claim made by another. The graph uses four edge types: supports, contradicts, depends on, and challenged by.

The conclusions in this essay are what the graph structure reports. They are not my reading of the literature.

### How the Graph Was Analyzed

Four structural passes over the completed graph:

**Hinge inventory.** Which claims are load-bearing? If a claim has sixty-five other claims depending on it, its truth value matters disproportionately. The hinge inventory identified the top twenty-five claims by dependency count.

**Cascade trees.** If a hinge claim were falsified, what collapses? The cascade analysis traced full collapse radii for the top five hinges using breadth-first search to four levels deep, identifying critical children: claims deep in the dependency chain that also face active scholarly contradiction.

**Counter-position stress tests.** The graph was tested against four major counter-positions. The question was not "are these positions correct?" It was "if they were, what claims in the graph would survive?" Survival rates: Heiser 72 percent, Tigay 85 percent, Kaufmann 58 percent, Schmid 41 percent. The Schmid test was the most devastating. His position, that the Pentateuchal sources date to the Persian period rather than the pre-exilic period, undercuts 59 percent of the graph's evidential foundation.

**Unknowns and convergence.** The graph was queried for settled convergences (five or more HIGH-confidence support edges with zero MEDIUM-confidence contradictions) and genuine unknowns (bidirectional HIGH-confidence contradictions where both sides are confident and the evidence does not resolve the dispute). This produced the evidence-density map that drives the conclusions in this essay.

### What This Essay Is and Is Not

This essay is an evidence-forward report of what the graph structure shows. It is not a neutral survey. The graph's structural verdict is clear: the evolutionary consensus accounts for more evidence, with fewer anomalies, than any competing model. This essay argues that verdict.

Every claim in this essay is traceable to a specific claim file in the OSKG-YahWeh project. Every citation is to a specific passage in a specific scholarly work. The full graph, including all 723 claims, all edges, and all four synthesis phases, is open-source at github.com/LittleSeneca/OSKG-YahWeh.

The project does not claim to be objective. The humanities domain resists objectivity: evidence is textual, archaeological, and comparative, different evidence types that do not all point the same direction. Disagreement is nuanced. Scholars rarely say "Smith is wrong." They say "Smith's reading is possible but the archaeological evidence favors an alternative." Capturing this in typed edges requires judgment. The methodology makes that judgment explicit and auditable. Every edge is documented. Anyone with the same sources can reproduce, audit, or extend the graph.

What follows is what the graph shows.

## Introduction

I grew up with a God who introduced himself. Genesis 12. God speaks to Abram. No preamble, no genealogy of deities, no cosmic backstory. Just a voice telling a man to go. The implication was clean: God was God. Always had been. The Israelites were the first people to figure it out, and the first five books of the Old Testament were the record of that revelation.

That was the story I got from Sunday school. God revealed himself to Abraham, then to Moses, as the one true God. The surrounding nations worshipped false gods, deities of wood and stone with elaborate mythologies, and Israel was called out from among them to bear witness to the truth. Monotheism was the original position, given by revelation. Polytheism was the later corruption. The Old Testament, read through this lens, is the story of a people who kept forgetting what they had been told, chasing after Canaanite gods, and being called back by prophets to the pure faith they had abandoned.

It is a coherent story. It has an internal logic. And millions of sincere people believe it because their pastors and theologians have presented it as the plain reading of the text. Those pastors are not lying. They are reading the Bible the way they were taught to read it, through a theological framework that assumes monotheism from Genesis 1 onward and interprets every apparent contradiction as something else: metaphor, rhetoric, or the stubborn waywardness of Israel. They want it to be true. So do I. The desire for it to be true shapes how you read.

What I am doing in this essay is different. I am reading the same texts with as open a mind as I can manage. Not assuming monotheism. Not assuming anything. Asking what the evidence actually shows, and letting the chips fall. The methodology, which I detailed in the preface, is built to resist confirmation bias: decompose the scholarship into discrete claims, connect them through typed relationships, and let the graph structure report what converges and what contradicts. This is the OSKG approach. It does not guarantee objectivity. Nothing does. But it makes the path from evidence to conclusion visible and auditable, which is more than most theological frameworks offer.

I am going to tell you why that Sunday school story is probably wrong. I am not certain. Nobody who works honestly with fragmentary evidence from three thousand years ago should be. But I am persuaded, and I am going to show you what persuaded me.

This is not a deconversion story. I remain a person of faith. But the faith I have now has looked at the evidence and adjusted. The faith I had before had never been asked to. That is what I am inviting you to do: look at the evidence, and let it ask what it asks.

## 1. The Name "Israel" and What It Tells Us

Start with the name. The name of the people. The name of the nation. The name God himself gave to Jacob after wrestling him through the night.

*Israel.* In Hebrew, *yiśrā-'ēl*.

It means "May El rule" or "El strives." The divine element is *'ēl*. Not *yāh*. Not *yahweh*. El. The high god of the Canaanite pantheon.

This is not a contested etymology. Mark S. Smith, Skirball Professor of Bible and Ancient Near Eastern Studies at NYU, calls this evidence of "El as the original god of Israel."[^1] Smith is the keystone scholar in this field. His two books, *The Early History of God* and *The Origins of Biblical Monotheism*, are the foundation on which most subsequent research rests. He did much of the primary translation and analysis of the Ugaritic texts that revealed the Canaanite pantheon in detail. He is also a practicing Roman Catholic. This matters. Smith's conclusions about Israel's polytheistic origins do not come from a skeptic trying to dismantle the Bible. They come from a believer reading the evidence with as much honesty as he can bring to it. When a scholar of Smith's stature, working from within the tradition, concludes that El predates Yahweh in Israel, that conclusion carries weight. Theodore J. Lewis, in his 2020 magnum opus *The Origin and Character of God*, confirms that El was a family/clan deity with a fundamentally different profile from the warrior Yahweh who would later absorb his identity.[^2] Thomas Römer, professor at the Collège de France, notes that "the name 'Israel' is a name constructed with the divine name El and ought normally to be translated as 'May El show his strength.'"[^3]

If Yahweh had been Israel's original god, we would expect a name like *yiśrâ-yāh* or *yiśrâ-yahweh*. Instead, the people's name invokes a different god entirely. The Israelites named themselves after El. Not Yahweh. That is not a trivial detail. It is the first piece of converging evidence that Yahweh was not always Israel's god. He became Israel's god.

The Merneptah Stele, an Egyptian inscription from approximately 1208 BCE, is the earliest extrabiblical mention of "Israel." The hieroglyphic determinative classifies Israel as a people group, not a settled state. The pharaoh Merneptah boasts: "Israel is laid waste, its seed is no more." The critical datum: the stele names "Israel" but does not name "Yahweh." By 1208 BCE, a people called Israel existed in Canaan. Nothing in this earliest reference connects them to the god who would later become their national deity.[^4]

## 2. Deuteronomy 32:8-9: The Text-Critical Smoking Gun

There is a passage in Deuteronomy that the scribes who transmitted the Hebrew Bible found so theologically dangerous that they changed it. We know they changed it because the Dead Sea Scrolls preserve the original reading. We know why they changed it because the original reading unambiguously describes a world where Yahweh was not the supreme god.

Here is the passage as it appears in the Masoretic Text, the standard Hebrew Bible used by Jews and Protestants:

> When the Most High apportioned the nations,
> when he divided humankind,
> he fixed the boundaries of the peoples
> according to the number of the **sons of Israel**.
> For Yahweh's portion is his people,
> Jacob his allotted inheritance.

"According to the number of the sons of Israel." This makes no contextual sense. How do the sons of Israel determine the boundaries of all the nations of the world? Israel does not exist yet at the time the passage describes.

Here is the original reading, preserved in 4QDeut-j from the Dead Sea Scrolls and reflected in the Septuagint:

> ...according to the number of the **sons of God**.

The Most High (Elyon, a title of the Canaanite high god El) divides the nations among his divine sons. And Yahweh, one of those sons, receives Israel as his portion.

This is not the monotheism I learned in Sunday school. This is a divine pantheon with a hierarchical structure. Elyon presides. Yahweh is a subordinate deity, one of approximately seventy divine sons, receiving his allotted nation. The text was changed because the original described something the later tradition could not accept.[^5]

Michael Heiser, an evangelical scholar with a PhD in Hebrew Bible and Semitic Languages from the University of Wisconsin-Madison, agrees that "sons of God" is the original reading. He disagrees with what it means, arguing that Elyon IS Yahweh and the passage describes one God performing one action with two titles. But he cannot dispute the text-critical fact: the Masoretic Text was altered. The Dead Sea Scrolls preserve the older, theologically embarrassing reading.[^6]

Smith is more direct: "In early Israel the god of Israel apparently belonged to the second tier of the pantheon; he was not the presider god but one of his sons."[^7] This passage "presents a cosmic order in which each deity received its own nation. Israel was the nation which Yahweh received, yet El was the head of this pantheon and Yahweh only one of its members."[^8]

## 3. El Was Israel's Original God

Deuteronomy 32:8-9 is the single most important piece of evidence, but it does not stand alone. The case for El as Israel's original god is built on converging lines of evidence from onomastics, biblical text, sanctuary archaeology, and comparative ancient Near Eastern studies.

### The Biblical Text Admits It

Exodus 6:2-3. God speaks to Moses:

> I am Yahweh. I appeared to Abraham, Isaac, and Jacob as El Shadday, but by my name Yahweh I did not make myself known to them.

The Priestly writer of the Pentateuch explicitly acknowledges that the patriarchs knew God as El Shadday, not as Yahweh. The biblical text itself preserves the memory of a time when Yahweh was not known to Israel's founding figures. Frank Moore Cross, Hancock Professor of Hebrew and Other Oriental Languages at Harvard, argued that Yahweh originated as a shortened form of *ˀel ḏū yahwī ṣabaˀôt* ("El who creates the hosts"), one of El's cultic titles that eventually broke free and became an independent deity.[^9]

### The Sanctuary Evidence

Major Israelite sanctuaries show evidence of prior El worship that was later absorbed into the Yahwistic cult. Shechem's temple was dedicated to *'ēl bĕrît* ("El of the Covenant"), a title that parallels Ugaritic *'ilbrt*. Jerusalem's traditions include El Elyon ("God Most High"), the deity Melchizedek serves in Genesis 14. Shiloh's tent tradition aligns with El's dwelling at the cosmic mountains. These were not originally Yahwistic sites. They were El's sanctuaries, later claimed by Yahweh when the two deities were identified.[^10]

### The Name Pattern

Day observes a striking pattern: the Hebrew Bible refers to divine beings as "sons of God" (*bĕnê 'ēl*, *bĕnê hā'ĕlōhîm*) but never "sons of Yahweh." The name pattern "finds a ready explanation in their origin in the sons of the Canaanite god El."[^11] If the council had always been Yahweh's, we would expect "sons of Yahweh." The consistent use of El-language preserves the older theology.

### The Balaam Oracles

Numbers 23-24, among the oldest poetry in the Bible, refer to "El who freed them from Egypt," using El-language roughly three times as often as Yahweh-language. This may preserve an older tradition in which El, not Yahweh, was the god of the Exodus. The oracles are framed as the words of a non-Israelite seer, which may explain why they were preserved when so much else was edited.[^12]

## 4. Where Did Yahweh Come From?

If El was Israel's original god, where did Yahweh come from? The evidence points south.

The earliest extrabiblical reference to Yahweh comes from the Soleb inscription in Nubia, approximately 1370 BCE. An Egyptian topographical list mentions "the land of the Shasu of Yhw." The Shasu were nomadic pastoralists from the Edom/Midian/Seir region south of Canaan. The hieroglyphic rendering "corresponds very precisely to the Hebrew Tetragrammaton YHWH" according to Michael Astour, and antedates the next oldest occurrence, the Mesha Stele, by over five hundred years.[^13]

Four biblical poems independently preserve a tradition of Yahweh coming from the south:

| Poem | Text | Direction |
|------|------|-----------|
| Deuteronomy 33:2 | "Yhwh came from Sinai, and dawned from Seir upon us" | South |
| Judges 5:4-5 | "Yhwh, when you went forth from Seir, when you marched from the region of Edom" | South |
| Habakkuk 3:3 | "God came from Teman, and the Holy One from Mount Paran" | South |
| Psalm 68:8-9 | "The earth quaked before God, the One of Sinai" | South |

Four independent combat hymns, composed across different periods, all pointing to the same geography. Seir. Edom. Teman. Paran. Sinai. This is not one text; it is a consistent tradition embedded in Israel's oldest poetry.[^14]

The Kuntillet Ajrud inscriptions from approximately 800 BCE confirm a localized Yahweh: "Yahweh of Samaria" (northern manifestation) and "Yahweh of Teman" (southern manifestation). A god with multiple local embodiments, not yet the universal deity of later theology.[^15]

The consensus among critical scholars is strong: Yahweh originated outside Canaan, specifically in the southern deserts of Edom/Midian/Teman/Seir. Smith, Römer, Day, Cross, Lewis, and Daniel Fleming all hold this. They disagree on details (was Yahweh a storm god? a war god? a volcanic god?) but agree on geography.[^16]

The mechanism by which Yahweh entered Israel is debated. The Kenite/Midianite hypothesis proposes that the Midianites, among whom Moses lived according to the biblical narrative (his father-in-law Jethro was a "priest of Midian" who already worshipped Yahweh in Exodus 18), transmitted the deity to Israel. This hypothesis is plausible but unprovable. Moses has no extra-biblical attestation. The Exodus narrative is, as Römer honestly acknowledges, "fashioned with great artifice in the manner of a romance."[^17]

Fleming mounts a significant recent challenge in *Yahweh Before Israel* (2021), arguing through physical measurement of the Soleb column that Seir was probably not in the original Amenhotep III list but was added in the 13th-century Ramesses II copy. Without Seir, the geographical anchor for Yahweh's southern origin weakens. He further argues the old poetry is mythological theophany, not historical memory: "Yahweh is no more originally 'from' Sinai and Seir than Zeus is 'from' Olympus."[^18] This challenge has not been systematically rebutted.

What is firm: El was Israel's original god. Yahweh arrived later. Where exactly from, and by what mechanism, remains partially contested.

## 5. The Wife He Wasn't Supposed to Have

The Kuntillet Ajrud inscriptions do more than confirm localized Yahwehs. They confirm Yahweh had a consort.

The site, a caravanserai in the Sinai desert from approximately 800 BCE, produced two pithos (storage jar) inscriptions:

- "I bless you by Yahweh of Samaria and by his Asherah"
- "I bless you by Yahweh of Teman and by his Asherah"

The Khirbet el-Qom inscription from approximately 700 BCE, a burial inscription from Judah, follows the same pattern: "Blessed is Uriyahu by Yahweh... and by his Asherah he has saved him from his enemies."[^19]

The debate centers on the Hebrew phrase *wl'šrth*. The possessive suffix *-h* can be read as referring to a personal name (the goddess Asherah) or a cult object (the wooden pole known as an asherah). The goddess interpretation is the majority position. William Dever, archaeologist at the University of Arizona, Römer, and Day all read it as a goddess. Dever calls the inscriptions "the smoking gun" for Asherah worship alongside Yahweh.[^20]

Smith is the most prominent dissenter, arguing that Hebrew grammar forbids a possessive suffix on a personal name. You cannot say "his Mary" in Hebrew. The *-h* forces a common noun reading: "his asherah" meaning "his cult symbol."[^21] Othmar Keel and Christoph Uehlinger, in their exhaustive catalog of Iron Age iconography *Gods, Goddesses, and Images of God in Ancient Israel* (1998), argue the asherah was a stylized tree that functioned as a mediating entity bringing Yahweh's blessing, not a goddess consort on equal footing.[^22]

The archaeological evidence beyond the inscriptions tilts the field. Over three thousand Judean Pillar Figurines have been excavated. Nude female figures with emphasized breasts, mass-produced from molds, found overwhelmingly in domestic contexts, dating to the 8th through 6th centuries BCE. Dever calls them "prayers in clay," votive offerings for fertility, conception, and safe childbirth. They were "found in almost every excavated 8th-6th century house in Judah."[^23]

And the Bible itself provides evidence through its polemics. You do not rail against something nobody is doing:

- **1 Kings 15:13:** King Asa removed his mother Maacah from being queen mother "because she had made an abominable image for Asherah."
- **1 Kings 18:19:** "The 400 prophets of Asherah" listed alongside the 450 prophets of Baal. If Baal is a deity, so is Asherah.
- **2 Kings 23:6-7:** Josiah "brought out the Asherah from the house of Yahweh" and burned it. Women were "weaving garments for Asherah" in the Temple itself.

The Deuteronomistic cover-up is Römer's key insight. The Bible deliberately obscures the Yahweh-Asherah link by associating her with Baal. But extra-biblical texts never pair Baal with Asherah. They pair Yahweh with Asherah. The inscriptions reveal what the biblical editors worked to hide.[^24]

The goddess was not a late pagan corruption of a pure original. She was there from the beginning, or at least from the moment Yahweh absorbed El's identity. At Ugarit, Asherah was El's consort, the mother of the seventy gods.[^45] When El and Yahweh merged, Asherah came with the package. The transfer was structurally expected. The biblical editors spent centuries trying to edit her out. They failed.

## 6. What Israelite Religion Actually Was

Dever provides the single most important conceptual tool for understanding the evidence: the distinction between book religion and folk religion.

**Book religion** was the religion of the Jerusalem priesthood, the Deuteronomistic reformers, and the biblical authors. Centralized, aniconic, exclusivist, text-based. Yahweh alone, worshipped at the Jerusalem Temple alone. This is the religion the Bible prescribes. Dever estimates this was the religion of perhaps five percent of Israelites.[^25]

**Folk religion** was the religion of ordinary Israelites. What they actually did. Regional, diverse, iconic, syncretistic. Yahweh alongside other deities (Asherah, Baal, the Queen of Heaven, astral powers), worshipped at local shrines, with figurines, standing stones, and household cult. This is the religion archaeology reveals.

The evidence converges on a clear conclusion. For most of Israel's history, folk religion was the norm. Book religion was the minority position of a zealous elite. The Bible preserves the perspective of the Yahweh-alone party that eventually won. The archaeological record shows the other side was the majority.[^46]

Jeffrey Tigay's onomastic study *You Shall Have No Other Gods* (1986) provides the strongest empirical challenge to this picture. His data shows that 94 percent or more of Israelite personal names from the 8th through 6th centuries BCE are Yahwistic. The epigraphic onomasticon is more Yahwistic than the Bible's. If polytheism was widespread, why did nobody name their kid after Baal?[^26]

The resolution is more interesting than either position alone. Names reflect public identity, not private practice. A person named Yohanan ("Yahweh is gracious") might still pray to Asherah for fertility. At Ugarit, few personal names contain "Asherah" despite her being the high goddess. Naming conventions and cultic devotion are different things. Tigay himself acknowledges this: "the absence of other gods from the onomasticon would not by itself tell us whether that society denied the existence or divinity of those gods."[^27]

Keel and Uehlinger document three simultaneous religious currents in 7th-century Judah: astralization under Assyrian influence (the Moon God of Haran identified with El/Yahweh), goddess revival in domestic piety (the three thousand pillar figurines), and aniconic orthodoxy among the Jerusalem elite (70 percent of Hebrew name seals are image-free by the late 7th century). All three coexisted. The "monotheistic reform" narrative describes one of three currents, and the one that was initially the weakest. It won because its adherents survived the exile and wrote the history.[^28]

Israelite religion was not a monolith. It was not the "pure Mosaic monotheism" of traditional theology. But neither was it "rampant Canaanite polytheism." Yahweh was always central in public identity. The religion was a hierarchical polytheism with Yahweh as the supreme national god, a suite of subordinate divine beings mediating specific domains (fertility, weather, protection, ancestors), and a growing minority of exclusivists who eventually denied the subordinate beings existed at all. It was diverse, contested, and changing. The Pentateuch's tidy narrative of pure origins, corruption, and reform is exactly backward.

## 7. When Monotheism Actually Arrived

The First Commandment is not monotheistic. "You shall have no other gods before me." This prohibits worshipping other gods. It does not deny they exist. It is a statement of cultic exclusion, not ontological exclusivity. The Shema ("Hear O Israel, Yahweh is our God, Yahweh is one") declares exclusivity of relationship. Not that other gods are nonexistent. That Yahweh is Israel's only god. This is monolatry, not monotheism.[^29]

True monotheism, the denial that other gods exist, does not appear in the Bible until Second Isaiah, approximately 540 BCE:

> "I am Yahweh, and there is no other; besides me there is no god." (Isaiah 45:5)
> "Before me no god was formed, nor shall there be any after me." (Isaiah 43:10)
> "I am Yahweh, who made all things, who stretched out the heavens alone." (Isaiah 44:24)

These are not monolatrous statements. They do not say "you shall not worship other gods." They do not say "who is like you among the gods?" (Exodus 15:11, a rhetorical question that presupposes other gods exist, even if it asserts Yahweh's superiority). They say other gods do not exist. This is a categorical shift.

Roughly seven hundred years after the traditional date of Moses. Monotheism was not revealed on Sinai. It was invented in Babylon by displaced priests trying to make sense of catastrophe.[^47]

The mechanism is straightforward. Ancient gods were geographically bound. Yahweh "lived" in the Jerusalem Temple. When the Babylonians destroyed the Temple in 586 BCE and deported the elite to Babylon, the Judeans faced an existential theological crisis. Option A: abandon Yahweh for the gods of Babylon, where they now lived. Option B: radically reconceive Yahweh as a god not bound to geography, whose power extended to Babylon and beyond. Judean theologians chose Option B.[^30]

Rainer Albertz, in his monumental two-volume history of Israelite religion, notes that Deutero-Isaiah "was the first to formulate consistent monotheism, as a consequence of proclaiming Yahweh's universal power in history." He adds a crucial observation: "Given the later campaigns of conquest under Christian auspices which were justified by the absolutist claim of monotheism, it is all the more important to point to the sociological fact that Israel made the breakthrough to monotheism in a situation of absolute political helplessness." Monotheism was formulated by the powerless, not the powerful.[^31]

Smith provides the most sophisticated refinement. Monotheism was not a "new stage of religion." It was a new rhetoric serving monolatry. The monotheistic declarations in Second Isaiah function as inner-community discourse. They use the language of Yahweh's exclusive divinity to absolutize his claim on Israel under extreme pressure. "Monotheism is not a new stage of religion but a new stage of rhetoric in a situation never known prior to the threat of exile. It represents not a change of religious policy but a new formulation or interpretation of religious reality delineating along cosmic lines what was no longer well delineated in the human, political lines."[^32]

The rhetoric eventually hardened into doctrine. Later Judaism, Christianity, and Islam all take it as ontology. But the original context was pastoral and polemical, not metaphysical. The catastrophe produced the claim. The claim became orthodoxy. And the messy, gradual, contested process was retrospectively narrated as a clean break. The Bible itself participates in this retrojection, projecting later monotheism backward onto earlier texts and earlier figures who did not hold it.

## 8. Israel in Canaanite Context

The most important reframing in the scholarly literature is also the simplest. Israel was not an alien intrusion into Canaan. Israel was a Canaanite subculture.

Smith opens *The Early History of God* with this observation: "The Israelite culture was largely Canaanite in origin. The Iron I period (1200-1000 BCE) highland settlers who would become 'Israel' were essentially Canaanites who moved from the lowlands to the highlands. Their material culture, language, and religious practices were continuous with the Canaanite world from which they emerged."[^33]

Keel and Uehlinger's exhaustive iconographic catalog demonstrates this continuity in visual culture. The seals, cult stands, and figurines of Iron Age Israel are indistinguishable from their Canaanite predecessors until the late monarchic period. The break, when it comes, is not a return to original purity. It is an innovation.[^34]

The Ugaritic texts, discovered in 1928 at Ras Shamra on the Syrian coast, reveal the Canaanite pantheon in detail. El is the aged high god, "Father of Years," enthroned at the cosmic mountains. Baal is the young storm warrior who defeats Sea and Death. Asherah is El's consort, "Creatress of the Gods," mother of the seventy divine sons. The parallels between Ugaritic literature and the Hebrew Bible are so extensive that direct borrowing is the only plausible explanation.[^48]

Psalm 29 is widely regarded by scholars as a hymn originally composed for Baal, with Yahweh's name substituted. The sevenfold voice of Yahweh thundering over the waters, shaking the wilderness, enthroned over the flood. Every element has a Baal parallel. The psalm is a Baal hymn with the name changed.[^35]

This is not a scandal. It is how ancient religion worked. Deities absorbed the characteristics of rival deities. Hymns were repurposed. Mythological frameworks were inherited and transformed. The Pentateuch and the historical books did not emerge from a vacuum. They emerged from a shared cultural matrix that included Ugaritic epic, Mesopotamian creation mythology, Egyptian wisdom literature, and Persian imperial theology.

The Genesis 1 creation account does not describe creation ex nihilo as later theology would insist. It describes God bringing order to a preexistent watery chaos (*tehom*, cognate with the Babylonian Tiamat). The great sea monsters (*tanninim*) appear not as pre-creation enemies to be battled but as created beings (Genesis 1:21). The sun and moon are depersonalized as "the greater light" and "the lesser light," stripped of their divine names (Shemesh and Yareah) and thus of their divine status.[^36] This is not the rejection of Canaanite mythology. It is its creative transformation. The same elements appear, reconfigured to serve a new theological program.

The Pentateuch is not a book of revealed monotheism. It is a compilation of mythic stories, folk and family religion, legal codes, and early history writing, stitched together over centuries by multiple authors with competing theological agendas, later edited by the winners into a narrative of purity, corruption, and reform that is the reverse of what actually happened.

## 9. But What About...? The Counter-Positions

I have presented the evolutionary consensus as though it were unopposed. It is not. There are serious scholars who reject it, and their arguments deserve a fair hearing. Dismissing them without engagement is not scholarship. It is tribalism. So here are the strongest counter-positions, stated in their own strongest form, followed by my reasons for finding them insufficient.

### Kaufmann: Monotheism Was Original

Yehezkel Kaufmann's *The Religion of Israel* (1960) is the most sophisticated defense of original Israelite monotheism ever written. His argument, stripped to its essentials:

First, the Bible is "utterly ignorant" of the nature of pagan religion. Across centuries of polemic, biblical writers consistently misrepresent paganism as mere fetishism, the worship of wood and stone, rather than engaging with living gods, myths, and cosmic dramas. If Israelite religion evolved out of polytheism, its polemics would show familiarity with polytheistic theology. They do not. They treat idols as dead objects. This, Kaufmann argues, is not a rhetorical strategy. It is evidence that the biblical authors genuinely did not understand what polytheists actually believed.[^38]

Second, the absence of theogony is radical and unique. "The store of biblical legends lacks the fundamental myth of paganism: the theogony. All theogonic motifs are similarly absent. Israel's god has no pedigree, fathers no generations; he neither inherits nor bequeaths his authority. He does not die and is not resurrected."[^39] If the biblical editors had systematically purged mythology, they did a terrible job. They preserved God walking in the garden, smelling sacrifices, wrestling Jacob, trying to kill Moses, the sons of God mating with human women. What is missing, Kaufmann argues, must have never been there.

Third, the prophets did not create monotheism. They inherited it. Amos, Hosea, Isaiah, Micah, Jeremiah, and Ezekiel all worked within an already-existing monotheistic framework. They were calling Israel back to covenant faithfulness, not to a new religious consciousness. The exile intensified monotheism but did not create it.[^40]

Kaufmann is not easy to dismiss. The absence of theogony in the Hebrew Bible is a genuine feature that the evolutionary model struggles to explain. The consistency of the fetishism polemic across centuries and sources is a real pattern. The candor of the biblical text about embarrassing material is a genuine methodological challenge. If the editors were systematic censors, they were incompetent ones.

But Kaufmann has a problem, and the problem is the ground. The archaeological evidence discovered after his death in 1963 directly contradicts his central claim. Kuntillet Ajrud. Khirbet el-Qom. Three thousand pillar figurines. Elephantine. These are not fetishes. These are evidence of actual polytheistic practice. Israelites blessing by "Yahweh and his Asherah" in the 8th century BCE. A Jewish temple in 5th-century Egypt where Anat is worshipped alongside Yahweh. You cannot read these as "vestigial fetishism" without stretching the term past breaking point.

Kaufmann's definition of "genuine polytheism" is also circular. He defines it as requiring theogony, mythology, and a metadivine realm. Israelite religion, by his definition, lacks these features. Therefore Israelite religion was never polytheistic. This proves nothing except that Kaufmann defined polytheism in a way that excluded Israel by definition. It is a tautology, not an argument.

His treatment of counter-evidence is revealing. When Ezekiel 8:14 describes women "weeping for Tammuz" at the Jerusalem Temple, a direct attestation of a Mesopotamian dying-and-rising god ritual, Kaufmann's response is that maybe these weren't Israelites, or maybe they didn't understand the myth. This is special pleading. When the evidence contradicts the theory, the theory should adjust. Kaufmann adjusts the evidence.

The absence of theogony is a real datum. But it is more plausibly an achievement than an inheritance. The biblical editors did not need to purge what was never there. They needed to purge what was, and in many cases they succeeded. The absence of theogony is not evidence of original monotheism. It is evidence of successful editing.

### Heiser: Yahweh Was Always Supreme

Michael Heiser's *The Unseen Realm* (2015) represents the most sophisticated attempt to reconcile the divine council data with monotheism. His core argument: the "other gods" mentioned in the Hebrew Bible are real beings, but they are created, subordinate divine beings, not co-eternal rivals to Yahweh. The word *elohim* refers to any being whose proper domain is the spiritual realm. It does not mean "deity worthy of worship."

Heiser agrees with critical scholars on the textual data. Deuteronomy 32:8 originally read "sons of God," not "sons of Israel." Psalm 82 describes God judging other *elohim*. The divine council is pervasive. Where he breaks from the consensus is on what this means.[^41]

Heiser argues that Elyon in Deuteronomy 32:8-9 IS Yahweh. The passage describes one God performing one action with two titles. Yahweh, as the Most High, apportions the nations to the members of his divine council. Israel is unique because Yahweh keeps them for himself as his direct portion. The other nations get lesser beings. There is no hint in the passage that Israel's God is a lesser being.

On Psalm 82, Heiser argues that the "gods" being judged are corrupt members of the divine council who failed to rule the nations justly. They are sentenced to die "like men," which proves they are not eternal, co-equal deities. They are created beings who rebelled.

The strength of Heiser's position is that it takes the biblical data seriously. He does not dismiss the divine council as mythological baggage. He does not explain it away as rhetoric. He treats it as a real feature of the biblical worldview and asks what it meant to the people who wrote it. This is a more honest approach than either the liberal dismissal or the conservative denial.

But Heiser has three problems.

First, the archaeological evidence. Heiser cannot adequately explain Kuntillet Ajrud, Khirbet el-Qom, or the three thousand pillar figurines. If Israel was never polytheistic, what does it mean that Israelites in the 8th century BCE were blessing each other by "Yahweh and his Asherah"? What does it mean that a Jewish temple in 5th-century Elephantine worshipped Anat alongside Yahweh? These are not acknowledgments of a divine council of subordinate beings. These are polytheistic practices. Heiser's framework has no place for them.

Second, the distinction between "acknowledging subordinate divine beings" and "polytheism" may be a distinction without a difference. Most ancient Near Eastern polytheistic systems had hierarchies where a high god ruled over lesser gods. The Ugaritic pantheon had El presiding over seventy divine sons. Heiser's divine council looks structurally identical to a polytheistic pantheon. He simply redefines the terminology so it does not count. This is taxonomy, not argument.

Third, Heiser's reading of Deuteronomy 32:8-9 is strained. If Elyon IS Yahweh, why does the text use two different names for one action? The most natural reading of the text distinguishes two actors: one who apportions (Elyon), and one who receives (Yahweh). Heiser's reading requires collapsing a distinction the text explicitly makes. His argument that "to a biblical writer, the Most High was the God of Israel" assumes what it needs to prove, namely that the biblical writer was a monotheist who would have identified the two. But if the poem predates monotheism, the writer may have intended the distinction Heiser denies.

None of this means Heiser is wrong about everything. He is right that the divine council is real and pervasive. He is right that *elohim* has a wider semantic range than "God." He is right that Second Temple Jewish literature develops the divine council concept within a monotheistic framework. But these observations do not add up to the conclusion that Israel was never polytheistic. They add up to the conclusion that Israelite theology was diverse and evolving, and that monotheism was one trajectory among several.

### Stern: The Oldest Poetry Is Monotheistic

Philip D. Stern, writing in *Biblical Archaeology Review* in 2025, mounts a more limited but targeted counter-argument. He does not claim Israel was always monotheistic. He claims the idea of monotheism appears in Israel's oldest poems, far earlier than the exile.

His evidence: Exodus 15:11 ("Who is like you among the gods, O Yahweh?"), 2 Samuel 22:32 ("Who is a god besides Yahweh?"), and Deuteronomy 32:39 ("See now that I, I am He, and there is no god besides Me"). Stern argues these are rhetorical questions whose implied answer is "no one." The other "gods" lack divine attributes. They are "non-gods." The questions are not acknowledgments of other deities. They are denials of their existence. Jeffrey Tigay dates the Song of Moses (Deut 32) to the 12th to 11th centuries BCE. If Stern is right, monotheism was "afoot" far earlier than the consensus allows.[^42]

Stern is careful to qualify his conclusion. He acknowledges that monotheism did not "reach the point of consensus in Israel until late in the biblical period." He acknowledges that Psalm 29, which addresses "sons of gods," is compatible with polytheism. He is not making the Kaufmann argument. He is making a more modest claim: monotheistic ideas existed early, alongside polytheistic ones, as part of Israel's diverse religious world.

This is the strongest of the counter-positions because it is the most modest. Stern does not need to explain away the archaeological evidence. He only needs to show that some Israelites, at some early point, articulated something like monotheism.

But even this modest claim has problems. Rhetorical questions that assert incomparability are not the same as denying existence. "Who is like you among the gods?" can mean "You are the greatest among the gods" (henotheism), not "There are no other gods" (monotheism). Ancient Near Eastern literature is full of hymns that praise one god as supreme without denying other gods exist. The Babylonian *Enuma Elish* exalts Marduk above all gods, yet Marduk rules a pantheon. Rhetorical elevation is not ontological denial.

Stern's reading of Deuteronomy 32:39 is stronger, but it sits uneasily alongside Deuteronomy 32:8-9. If the same poem describes Elyon dividing the nations among his divine sons and Yahweh receiving Israel as his portion (verse 8-9), the monotheism of verse 39 reads less like a consistent theology and more like a contradiction within the poem itself. Which is exactly what we would expect from a text that was composed, edited, and re-edited over centuries by authors with different theologies.

The dating is also disputed. Tigay's 12th to 11th century date for Deuteronomy 32 is at the early end of scholarly estimates. Many scholars date the poem substantially later. Even if the core is archaic, the version we have has been edited. Stern acknowledges this uncertainty but leans on the early end of the range to make his case.

Stern's evidence is real. The poems he cites do exist, and they do contain language that can be read monotheistically. But they also contain language that cannot. The same Song of the Sea that asks "Who is like you among the gods?" describes Yahweh as "a man of war" (Exodus 15:3), a warrior deity with a physical body who hurls horses and riders into the sea. This is not the God of Maimonides. Reading later monotheism backward into early poetry flattens the poetry's own complexity. These poems reflect a world where Yahweh is supreme among the gods, not the only god in existence. The difference between those two positions is the difference between monolatry and monotheism. And that difference is the argument.

### Tigay: The Names Tell a Different Story

Jeffrey Tigay's *You Shall Have No Other Gods* (1986) provides the strongest empirical counter-weight to the archaeological picture of rampant polytheism. His data is straightforward: 94 percent or more of Israelite personal names from the 8th through 6th centuries BCE are Yahwistic. The epigraphic onomasticon, preserved on seals, ostraca, and bullae from administrative and military contexts, is even more Yahwistic than the biblical onomasticon. The Samaria ostraca, Lachish letters, and Arad ostraca all show nearly 100 percent Yahwistic names.[^43]

Tigay's argument is not that Israel was monotheistic. It is that practical monolatry, worshipping only Yahweh whatever you believed about other gods, was the public norm far earlier than the consensus timeline predicts. If polytheism was widespread and normative, why did Israelites overwhelmingly name their children after Yahweh and not after Baal, Asherah, or any other deity?

This is a genuine challenge. But it is resolvable. Names reflect public identity, not private practice. A person named Yohanan ("Yahweh is gracious") might still pray to Asherah for fertility, keep a pillar figurine in her house, and bake cakes for the Queen of Heaven. Names are what you present to the community. Figurines are what you keep in your house. These are different domains of religious life, and they can coexist without contradiction.

The Ugaritic parallel is instructive. At Ugarit, few personal names contain "Asherah" despite her being the high goddess, the consort of El, and the mother of the seventy gods. Naming conventions and cultic devotion are different things. Tigay himself acknowledges the limit of his evidence: "the absence of other gods from the onomasticon would not by itself tell us whether that society denied the existence or divinity of those gods."[^44]

There is also a selection bias problem. The epigraphic evidence comes disproportionately from administrative and military contexts, seals and letters and fort ostraca, the very circles most likely to be aligned with official Yahwism. Women, who were the primary users of pillar figurines and the primary practitioners of domestic religion, are heavily underrepresented in the epigraphic record. Rural peasants, who could not write, are invisible. The onomasticon captures the public, elite, male dimension of Israelite religion. It does not capture the private, popular, female dimension. The figurines do.

Tigay's data establishes that Yahweh was overwhelmingly dominant in public identity far earlier than a model of "rampant polytheism" would predict. This is an important corrective. But it does not refute the evidence for private polytheistic practice. Both datasets, the names and the figurines, can be true simultaneously. And that simultaneous truth is more interesting than either dataset alone.

### Where the Counter-Positions Land

None of these counter-positions is frivolous. Kaufmann identified real features of the biblical text. Heiser takes the divine council seriously when most scholars dismiss it. Stern identifies genuinely early poetry that leans monotheistic. Tigay provides hard data that constrains how polytheistic Israelite religion could have been.

But each position, taken as a whole, fails to account for the full range of evidence. Kaufmann cannot explain the figurines. Heiser cannot explain Kuntillet Ajrud. Stern cannot explain why the same poems he cites contain polytheistic language alongside the monotheistic. Tigay cannot explain why the names and the figurines point in opposite directions, unless both forms of evidence are capturing different dimensions of the same complex religious reality.

The evolutionary model, for all its untidiness, accounts for more of the evidence than any competitor. It accounts for the divine council (preserved from the polytheistic past). It accounts for the figurines (popular practice persisting alongside official theology). It accounts for the names (Yahweh was always central in public identity). It accounts for the poetry (older poems are more polytheistic; later poems are more monotheistic). It accounts for the exile as catalyst (the rhetoric shifts when the political situation shifts). And it accounts for the Bible's own multivocality (multiple theologies preserved in tension because the canon was closed before the tensions could be resolved).

The counter-positions are not wrong about their evidence. They are wrong about what their evidence proves. Kaufmann proves that the biblical editors were effective. Heiser proves that the divine council was real. Stern proves that early poetry can be read monotheistically. Tigay proves that Yahweh dominated public naming conventions. None of these proofs adds up to the conclusion that Israel was monotheistic from the beginning. The conclusion that fits the evidence, all of it, the names and the figurines, the poetry and the inscriptions, the Bible and the ground, is that Israelite religion was diverse, contested, and evolving. Monotheism was not the starting point. It was the destination. And the journey took a thousand years.

[^38] Kaufmann, Yehezkel. *The Religion of Israel: From Its Beginnings to the Babylonian Exile*. Translated and abridged by Moshe Greenberg. Chicago: University of Chicago Press, 1960, Chapter I. See also claim: `israelite-religion-non-mythological-fundamentally-unique`.

[^39] Kaufmann, *Religion of Israel*, Chapter III. See also claim: `biblical-idolatry-not-genuine-mythological-polytheism`.

[^40] Kaufmann, *Religion of Israel*, Chapters XI-XIII. See also claim: `prophets-inherited-monotheism-did-not-invent`.

[^41] Heiser, Michael S. *The Unseen Realm: Recovering the Supernatural Worldview of the Bible*. Bellingham, WA: Lexham Press, 2015. See also Heiser, "Are Yahweh and El Distinct Deities in Deut 32:8-9 and Psalm 82?" *Hiphil* 3 (2006). Claim: `elyon-yahweh-same-god-deut32-not-two-deities`.

[^42] Stern, Philip D. "When Did Monotheism Emerge in Ancient Israel?" *Biblical Archaeology Review*, October 26, 2025. See also claims: `monotheism-well-established-before-exile-biblical-authors`.

[^43] Tigay, Jeffrey H. *You Shall Have No Other Gods: Israelite Religion in the Light of Hebrew Inscriptions*. Atlanta: Scholars Press, 1986, Chapter I. Claims: `post-united-monarchy-polytheism-limited-not-rampant`.

[^44] Tigay, *You Shall Have No Other Gods*, Chapter II.

## 10. Stop Reading the Old Testament Wrong

I am not arguing that the Old Testament is worthless. I am arguing that we have been reading it for the wrong thing.

The early Old Testament is not a reliable description of God's nature. It is a record of how a particular people, embedded in a particular cultural context, thought about the divine over a period of roughly a thousand years. It contains genuine philosophical insight, extraordinary poetry, and the earliest attempts at something like history writing. It also contains a theological program, imposed retrospectively by the Deuteronomistic editors, that misrepresents what most Israelites actually believed and practiced for most of their history.

When you read the Pentateuch as a monotheistic document, you are reading into it a theology that did not exist when it was written. Abraham did not worship Yahweh. The name "Israel" invokes El, not Yahweh. The patriarchs knew God as El Shadday, not Yahweh, and the biblical text itself admits this (Exodus 6:2-3). The First Commandment is monolatrous, not monotheistic. The divine council is real and pervasive. Psalm 82 describes God judging other gods, not human judges. Psalm 29 is a Baal hymn with the name changed. Deuteronomy 32:8-9 in its original form describes a world where Elyon presides and Yahweh is his son. The Masoretic scribes changed it because they could not accept what it said.

Benjamin Sommer, professor at the Jewish Theological Seminary, offers the most helpful reframing I have found. In *The Bodies of God* (2009), he argues that the evolution in Israelite religion is not polytheism to monotheism. It is fluid monotheism to anti-fluid monotheism. In the earliest written sources embedded in the Pentateuch, the Yahwist (J) and Elohist (E) strands, Yahweh has multiple bodies. He appears as three men at Mamre (Genesis 18). The *mal'akh* (angel/messenger) IS Yahweh, not a separate being. Yahweh of Samaria and Yahweh of Teman are distinct yet one. This is exactly how Mesopotamian and Canaanite gods operated. What the Priestly source (P) and the Deuteronomistic school (D) did was reject this fluidity. The Priestly writers replaced God's body with the *kavod* (Glory). The Deuteronomists replaced it with the *shem* (Name). The reformers did not invent monotheism. They invented a specific kind of monotheism: the noncorporeal, transcendent God of later Judaism and Christianity.[^37]

The irony, as Sommer notes, is that the God of the philosophers is not the God of Abraham, Isaac, and Jacob. The older, more "primitive" conception, God with a body, God in multiple places, was suppressed, not superseded. It survived underground in Jewish mysticism, where the kabbalistic *sefirot* are "God's bodies," and openly in Christianity, where the Trinity is fluid monotheism, three persons, one God, one of whom has a body.

The tradition contains multitudes. It always did. The Bible itself is multivocal. It preserves multiple theologies in tension. The Yahwist's embodied God walks in the garden, smells sacrifices, wrestles Jacob. The Priestly source's transcendent God creates by speech and cannot be seen. The Deuteronomist's distant God places only his Name in the Temple, not his presence. These are not contradictions to be harmonized. They are evidence of a living tradition wrestling with its inheritance over centuries. The harmonizers are the ones doing violence to the text.

We should use the early Old Testament to understand early Israelite philosophy, poetry, and thought. We should not use it as a systematic theology textbook. The God described in the earliest strata of the Bible is a southern storm deity who absorbed the identity of a Canaanite high god, took that god's consort as his own, presided over a divine council of subordinate deities, had a physical body that walked and ate and fought, and only became the sole, transcendent, universal creator when his temple was destroyed and his people were exiled.

That story, from desert war god to universal creator, is one of the most remarkable in religious history. It does not need to be a story of pure revelation to be a story worth telling. But if you insist on reading it as revelation, you owe it to the evidence to understand what the revelation actually contains, rather than what later theology projects onto it. The Pentateuch is not a monotheistic document. The people who wrote it were not monotheists. The god they described was not the only god they acknowledged. And the process by which he became the only God took a thousand years, a national catastrophe, and a brilliant theological innovation that the biblical editors themselves worked to conceal.

---

## Notes

[^1] Smith, Mark S. *The Early History of God: Yahweh and the Other Deities in Ancient Israel*. 2nd ed. Grand Rapids: Eerdmans, 2002 [orig. 1990], Chapter 1. See also claim: `el-was-original-god-israel-name-and-absence-yahweh`.

[^2] Lewis, Theodore J. *The Origin and Character of God: Ancient Israelite Religion through the Lens of Divinity*. Oxford: Oxford University Press, 2020, Chapter 4.

[^3] Römer, Thomas. *The Invention of God*. Translated by Raymond Geuss. Cambridge, MA: Harvard University Press, 2015, Chapter 4. See also claim: `israel-name-el-originally-el-worshippers`.

[^4] The Merneptah Stele is housed in the Egyptian Museum, Cairo. Dated to the 5th year of Merneptah's reign, c. 1208 BCE. See primary source note: `merneptah-stele`.

[^5] 4QDeut-j (DJD XIV, plate XXXV) preserves *bny 'lwhm* ("sons of God") or *bny 'l* ("sons of El"). The LXX reads ἀγγέλων θεοῦ ("angels of God"). The MT reads *bĕnê yiśrā'ēl* ("sons of Israel"). See primary source note: `deut-32-8-9-qumran-variant`. Claims: `deut-32-8-9-el-elyon-superior-yahweh-divine-son`, `deut-32-8-9-sons-of-el`.

[^6] Heiser, Michael S. *The Unseen Realm: Recovering the Supernatural Worldview of the Bible*. Bellingham, WA: Lexham Press, 2015, Part 4. See also claim: `elyon-yahweh-same-god-deut32-not-two-deities`.

[^7] Smith, Mark S. *The Origins of Biblical Monotheism: Israel's Polytheistic Background and the Ugaritic Texts*. Oxford: Oxford University Press, 2001, Chapter 8.

[^8] Smith, *Origins of Biblical Monotheism*, Chapter 7.

[^9] Cross, Frank Moore. *Canaanite Myth and Hebrew Epic: Essays in the History of the Religion of Israel*. Cambridge, MA: Harvard University Press, 1973, Part I. See also claim: `yahweh-originated-as-el-epithet-creates-heavenly-armies`.

[^10] See claims: `el-was-original-god-israel-name-and-absence-yahweh`, `name-israel-el-original`.

[^11] Day, John. *Yahweh and the Gods and Goddesses of Canaan*. Sheffield: Sheffield Academic Press, 2000, Chapter 1.

[^12] See claim: `el-original-god-exodus`.

[^13] See primary source note: `soleb-shasu-inscription`. Claims: `yhwh-originated-southern-deserts-edom-seir`, `four-biblical-poems-preserve-southern-origin-tradition`.

[^14] Claim: `four-biblical-poems-preserve-southern-origin-tradition`.

[^15] Primary source note: `kuntillet-ajrud-inscriptions`. Claims: `yhwh-local-manifestations-fluid-monotheism-kuntillet-ajrud`.

[^16] See synthesis: `synthesis-who-was-yahweh`, Question 1.

[^17] Römer, *Invention of God*, Chapter 3. See also claim: `midianite-hypothesis-survived-structural-utility-yahweh-canaan-puzzle`.

[^18] Fleming, Daniel E. *Yahweh Before Israel: Glimpses of History in a Divine Name*. Cambridge: Cambridge University Press, 2021, Chapters 2-3. See also claim: `yahweh-not-taken-from-outsiders-divine-name-israel-diverse-origins` and `southern-geography-theophany-not-origin-memory`.

[^19] Primary source note: `kuntillet-ajrud-inscriptions`. Claims: `kuntillet-ajrud-khirbet-el-qom-asherah-consort-not-symbol`, `kuntillet-ajrud-proves-consort`.

[^20] Dever, William G. *Did God Have a Wife? Archaeology and Folk Religion in Ancient Israel*. Grand Rapids: Eerdmans, 2005, Chapters VI-IX. See claims: `dever-archaeology-proves-asherah-real-goddess-yhwh-consort`, `dever-cumulative-archaeology-asherah-yahweh-consort-goddess`.

[^21] Smith, *Early History of God*, Chapter 3. Claims: `asherah-cult-symbol-not-goddess-monarchic-israel`, `asherah-was-yahwistic-symbol`.

[^22] Keel, Othmar, and Christoph Uehlinger. *Gods, Goddesses, and Images of God in Ancient Israel*. Translated by Thomas H. Trapp. Minneapolis: Fortress Press, 1998, Part V. Claims: `his-asherah-cultic-symbol-stylized-tree-not-goddess-consort`, `no-consort-relationship-yahweh-asherah-divine-couples-absent`.

[^23] Dever, *Did God Have a Wife?*, Chapter V. Claim: `judean-pillar-figurines-asherah-goddess-worship-domestic`.

[^24] Römer, *Invention of God*, Chapter 9. Claims: `bible-deliberately-obscures-yhwh-asherah-link`, `yhwh-consort-asherah-goddess-baal-link-deuteronomistic-synthesis`.

[^25] Dever, *Did God Have a Wife?*, Introduction. Claims: `hebrew-bible-elite-scribal-literature-not-folk-religion`, `monotheism-well-established-before-exile-biblical-authors`.

[^26] Tigay, Jeffrey H. *You Shall Have No Other Gods: Israelite Religion in the Light of Hebrew Inscriptions*. Atlanta: Scholars Press, 1986, Chapter I. Claims: `post-united-monarchy-polytheism-limited-not-rampant`, `biblical-writers-magnified-polytheism-theological-axioms`.

[^27] Tigay, *You Shall Have No Other Gods*, Chapter II. See also evidence brief: `evidence-brief-questions-3-4`, Section 3(d).

[^28] Keel and Uehlinger, *Gods, Goddesses, and Images of God*, Parts VI-VII.

[^29] Smith, *Origins of Biblical Monotheism*, Chapter 8. Claims: `true-monotheism-denies-other-gods-existence`, `monotheism-as-exilic-rhetoric-not-religious-revolution`.

[^30] Römer, *Invention of God*, Chapter 12. Claims: `true-monotheism-emerged-babylonian-exile`, `exile-transformed-israel-state-people-to-religious-community`.

[^31] Albertz, Rainer. *A History of Israelite Religion in the Old Testament Period*. 2 vols. Translated by John Bowden. Louisville: Westminster John Knox, 1994. Vol. 2, Chapter 4. Claim: `deutero-isaiah-first-consistent-monotheism-internal-development`.

[^32] Smith, *Origins of Biblical Monotheism*, Chapter 10.

[^33] Smith, *Early History of God*, Introduction. See also claims: `israelite-culture-was-canaanite-no-separation`, `israel-broadly-west-semitic-religion-not-pristine-monotheism`.

[^34] Keel and Uehlinger, *Gods, Goddesses, and Images of God*, Chapters I-V.

[^35] Day, *Yahweh and the Gods and Goddesses of Canaan*, Chapter 4. See also claim: `day-chaoskampf-canaanite-baal-yam-not-babylonian-marduk-tiamat`.

[^36] Smith, *Origins of Biblical Monotheism*, Chapter 9. Claim: `monotheism-as-transformed-canaanite-myth`.

[^37] Sommer, Benjamin D. *The Bodies of God and the World of Ancient Israel*. Cambridge: Cambridge University Press, 2009, Chapters 1-3. See also claims: `bible-contains-two-theologies-in-tension-fluid-vs-anti-fluid-monotheism`, `sommer-reframes-polytheism-monotheism-evolution-as-fluid-embodiment-shift`.

[^45]: At Ugarit, Asherah (*Aṯiratu*) is El's consort, "Lady Asherah of the Sea," "Creatress/Mother of the Gods." The Ugaritic texts date to the 14th-13th centuries BCE. See Day, *Yahweh and the Gods and Goddesses of Canaan*, Chapter 2; primary source note: `ugaritic-baal-cycle`. Claim: `asherah-el-consort-transferred-to-yahweh`.

[^46]: Dever, *Did God Have a Wife?*, Introduction and Chapters VI-IX. Dever documents eight categories of archaeological evidence for folk polytheistic practice: local shrines, standing stones, altars, figurines, cult stands, inscriptions, votive offerings, and mortuary practices. Claims: `dever-folk-polytheism-outlasted-monarchy-monotheism-book-religion`, `eight-categories-archaeology-folk-religion-asherah-cumulative`.

[^47]: The traditional date of Moses is approximately 13th century BCE. Second Isaiah dates to approximately 540 BCE. The gap is roughly 700 years. See Römer, *Invention of God*, Chapter 12; Smith, *Origins of Biblical Monotheism*, Chapter 8. Claim: `true-monotheism-emerged-babylonian-exile`.

[^48]: The Ugaritic texts (Ras Shamra) were discovered in 1928. The key mythological texts include the Baal Cycle (KTU² 1.1-1.6), which depicts Baal's defeat of Yamm (Sea) and Mot (Death). The seventy sons of Asherah are attested at KTU² 1.4.VI.46. See Smith, *Origins of Biblical Monotheism*, Chapters 2-3; Day, *Yahweh and the Gods and Goddesses of Canaan*, Chapters 1-2; primary source note: `ugaritic-baal-cycle`.

---

*This essay draws on the OSKG-YahWeh knowledge graph project: 17 scholarly monographs, 149 chapter notes, 723 extracted claims with typed edges, and 4 synthesis phases. All claims referenced above are traceable to specific claim files, chapter notes, and primary source documents within the project.*
