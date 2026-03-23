# Neutral Provenance Policy

## Public Rule
This repository exposes only neutral provenance metadata.

Public provenance may include:
- `source_id`
- `theme`
- `content_type`
- `derived_role`
- `pack_ids`

Public provenance must not include:
- raw filenames
- raw folder names
- raw local paths
- page images
- screenshots
- original source documents
- source-side author identifiers

## Practical Effect
The public repository is a reconstructed method system, not a mirror of any private file archive.

## Local Private Layer
Local extraction outputs can retain operational metadata needed for indexing and reuse, but they stay in `private_cache/` and must not be committed.
