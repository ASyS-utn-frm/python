# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**"Curso de introducción a Python para análisis de señales y sistemas"** — publishable digital material. Originally developed for the **"Análisis de Señales y Sistemas"** course at UTN FRM (Universidad Tecnológica Nacional, Facultad Regional Mendoza), Electronic Engineering program. Author: Mg. Ing. Javier Ignacio Velez.

The notebooks are designed to run on **Google Colab** and are served as a GitHub Pages site. Repository: `ASyS-utn-frm/python`.

**Terminology:** the exposé notebooks are called **módulos** (prefix `MNN_*`), not "tutoriales". The deliverable notebooks are called **laboratorios** (prefix `LNN_*`), not "trabajos prácticos" or "TP". Use this terminology in all new content.

**Publishability:** since the course is published standalone, **do not include phrases that reference the professor, assistants, or a specific cohort** (e.g. "consultá al profesor", "avisá al ayudante"). Material must be self-contained.

## Repository Structure

```
├── docs/                        # Project documentation
│   ├── PROJECT_PLAN.md          # Master roadmap (phases, tasks, progress)
│   ├── FORMATO_CELDAS.md        # Cell ID and role conventions
│   ├── GUIA_ESTILO.md           # Editorial style guide
│   ├── AUDIT_REPORT.md          # Phase 1 content audit (historical)
│   └── CARRYOVERS.md            # Cross-notebook decisions still pending
├── tools/                       # Conversion and grading tools
│   ├── nb2md.py                 # ipynb → Markdown source
│   ├── md2nb.py                 # Markdown source → ipynb
│   └── extract_student.py       # Extract student cells for grading
├── src/                         # Markdown source files (source of truth)
├── rubrics/                     # Grading rubrics per laboratorio
├── resources/                   # Images (logoUTN.jpg)
├── MNN_*.ipynb                  # Módulos (expository); generated from src/
├── LNN_*.ipynb                  # Laboratorios (deliverables); generated from src/
├── *_viejo.ipynb / legacy names # Legacy notebooks pending migration
├── graf.py                      # Standalone Fourier visualization script
├── README.md / index.md         # GitHub Pages landing page
└── _config.yml                  # Jekyll config
```

### Módulos (target: 9)
Progressive Python modules for readers with zero programming experience:
- M01: Google Colab intro → M02: Types → M03: Collections → M04: Control flow
- M05: Functions → M06: OOP basics (NEW) → M07: NumPy → M08: Matplotlib → M09: SymPy

### Laboratorios (target: 8)
Deliverable labs that apply the modules (see `docs/PROJECT_PLAN.md` for full plan):
- L1 Python applied → L2 Complex variable → L3 Convolution → L4 CT Fourier
- L5 Laplace → L6 Sampling → L7 FFT + modulation → L8 Z transform

## CRITICAL: Working with Notebooks

**Never edit `.ipynb` files directly.** The workflow is:

1. **Extract** existing notebook to Markdown source:
   ```bash
   python tools/nb2md.py <notebook.ipynb>  # outputs to src/<name>.md
   ```
2. **Edit** the `.md` file in `src/` (see `docs/FORMATO_CELDAS.md` for syntax)
3. **Convert** back to notebook:
   ```bash
   python tools/md2nb.py src/<name>.md [output.ipynb]
   ```

This saves tokens (no JSON/base64 overhead) and produces clean diffs.

### Cell Delimiters in Markdown Source
```
%% md hdr-01      ← Header cell (logo, title)
%% md prov-01     ← Provided content (explanations/examples)
%% code prov-02   ← Provided code (examples to run)
%% md enu-01      ← Exercise statement (enunciado)
%% code act-01    ← Student activity cell (# TU CÓDIGO AQUÍ)
```

Full spec: `docs/FORMATO_CELDAS.md`

### Grading Workflow
```bash
python tools/extract_student.py <submitted.ipynb> --rubric rubrics/Lx_rubric.md --format markdown
```

## Cross-notebook decisions

When a change in one notebook implies something pending in another (e.g., "move triple-quote content from M01 to M02"), record it in `docs/CARRYOVERS.md`. Read that file before working on any module/lab and apply relevant pending items.

## Key Libraries

All notebooks assume Google Colab. Core dependencies:
- **NumPy** (`np`), **Matplotlib** (`plt`), **SymPy** (`sp`), **SciPy** (`signal`)

## Content Language

All reader-facing text in **Spanish** (Argentine voseo). Activity placeholders: `# TU CÓDIGO AQUÍ`.

## Style Guide

See `docs/GUIA_ESTILO.md` for full guidelines. Key principles:
- Tone: close and patient tutor, precise but not exhaustive
- Never reference concepts not yet presented in earlier módulos
- Ascending difficulty within each notebook
- Cycle: explain → show (runnable example) → practice
- **No references to the professor/cátedra**: material must stand on its own
