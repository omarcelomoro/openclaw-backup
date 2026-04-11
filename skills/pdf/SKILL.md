---
name: pdf
description: Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.
source: LeoYeAI/openclaw-master-skills
status: imported-for-leevre-review
---

# PDF Processing Guide

## Overview
Guide for essential PDF processing operations using Python libraries and command-line tools.

## Typical tools
- `pypdf` for merge, split, rotate, metadata, encryption
- `pdfplumber` for text and table extraction
- `reportlab` for PDF generation
- `pdftotext`, `qpdf`, `pdfimages` for CLI workflows

## Common Leevre uses
- Extract text from apólices and relatórios de comissão
- Pull tables from insurer statements
- Generate PDFs for scripts, reports, and internal summaries
- OCR scanned insurance documents when needed

## Safety notes
- Prefer local processing
- Do not embed secrets in generated PDFs
- Review extracted values before using them in financial or operational decisions

## Leevre adaptation notes
- Prioritize workflows for commission reconciliation, insurer reports, policy documents, and content PDFs.
- Pair with `pdf-extract` for fast text extraction and with `excel-xlsx` for structured reconciliation.
