# Literature Stack Playbooks

Use this reference after the stack is installed and the user wants to run real workflows.

## Playbook 1: Google Scholar To Zotero Project Collection

Goal:
- discover a topic broadly
- track citations
- export high-value references into Zotero

Suggested sequence:
1. Use `gs-researcher` or the `gs-*` skills in Claude Code to search and inspect cited-by trails.
2. Export chosen records into Zotero.
3. In Zotero MCP, create or choose a project collection.
4. Batch-tag the imported items by topic, method, theory, or project stage.
5. Run duplicate checks before starting synthesis.

Useful follow-up:
- hand off to `dan-literature` for literature matrix design
- hand off to `dan-question-gap` for gap discovery

## Playbook 2: CNKI To Zotero Chinese Literature Track

Goal:
- add Chinese-language literature, journal level information, and index coverage into the same project library

Suggested sequence:
1. Use `cnki-researcher` or `cnki-*` skills in Claude Code to search, filter, and inspect journals.
2. Export records to Zotero.
3. If a PDF download is available under your access rights, handle login and download manually when prompted.
4. Add language, database, and journal-index tags in Zotero.
5. Merge duplicates with existing English records if needed.

Useful follow-up:
- hand off to `dan-review-paper` if the user is doing a Chinese-English integrated review

## Playbook 3: Zotero Project Management

Goal:
- turn a pile of records into a project-ready library

Suggested sequence:
1. Define a collection hierarchy by project, manuscript, or chapter.
2. Define a tag schema before bulk tagging.
3. Normalize attachments, notes, and naming conventions.
4. Use Zotero MCP to search by topic, tag, annotation, or semantic similarity.
5. Keep one project collection as the review-ready source set.

Recommended outputs:
- collection schema
- tag schema
- duplicate cleanup note
- review-ready source list

## Playbook 4: Zotero Collection To Literature Review

Goal:
- convert a cleaned Zotero collection into a review-ready synthesis workflow

Suggested sequence:
1. Search the target collection via Zotero MCP.
2. Pull metadata, abstracts, notes, annotations, and full text where available.
3. Ask `dan-literature` to design the matrix fields.
4. Ask `dan-review-paper` to choose review type and synthesis structure.
5. Ask `dan-paper-writing` to turn findings into a review outline.

Recommended prompts:
- "Use Zotero MCP to pull all items in this collection and organize them by method and theme."
- "Create a literature matrix for this Zotero collection."
- "Turn this cleaned source set into a review-paper outline with sections and synthesis logic."

## Handoff Rules

- If the main bottleneck is collection and tagging, stay in `dan-literature-stack`.
- If the main bottleneck is reading and note structure, move to `dan-literature`.
- If the main bottleneck is synthesis and review findings, move to `dan-review-paper`.
- If the main bottleneck is writing, move to `dan-paper-writing`.
