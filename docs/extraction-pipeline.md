# Extraction Pipeline

This repository includes a local-only extraction pipeline for turning PDFs into machine-readable text caches.

## Goals
- support LLM reading and reuse on a local machine
- keep raw source files out of the public repository
- separate extraction from publication

## Steps
1. Run `python3 scripts/inventory.py`
2. Run `python3 scripts/extract_pdf.py --limit 30 --render-preview` for a sample pass
3. Run `python3 scripts/extract_pdf.py --all` for a full local pass if needed

## What The Extractor Does
- reads PDF metadata with `pdfinfo`
- extracts text with `pdftotext -layout`
- strips repeated per-page boilerplate lines by frequency
- optionally renders a first-page preview with `pdftoppm`
- writes local JSON and Markdown outputs to `private_cache/pdf_extracts/`

## Publication Boundary
Extraction outputs are for local indexing only. They are ignored by Git and never become public repository content.
