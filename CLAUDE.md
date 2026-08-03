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
├── src/                         # Markdown source for MÓDULOS only (source of truth)
├── Laboratorios/                # Lab enunciados (.ipynb, generated) — published
├── resources/                   # Images (logoUTN.jpg) y audios/ para los labs
├── MNN_*.ipynb                  # Módulos (expository); generated from src/
├── graf.py                      # Standalone Fourier visualization script
├── README.md / index.md         # GitHub Pages landing page
├── _config.yml                  # Jekyll config
├── _fuente/                     # PRIVATE source repo for labs — gitignored (see below)
└── _legacy/                     # Superseded material (TP0–TP4, pre-contract L00) — gitignored
```

### Módulos (target: 9) — COMPLETE
Progressive Python modules for readers with zero programming experience:
- M01: Google Colab intro → M02: Types → M03: Collections → M04: Control flow
- M05: Functions → M06: OOP basics → M07: NumPy → M08: Matplotlib → M09: SymPy

### Laboratorios (target: 6 = L00–L05)
Deliverable labs that apply the modules (see `docs/PROJECT_PLAN.md` for full plan):
- L00 Python practice ✅ → L01 Signals & operations ✅ → L02 Convolution ✅ → L03 Sampling ✅
- L04 Fourier (Part A continuous transform + convolution theorem, Part B DFT/FFT + AM modulation)
- L05 System analysis (Part A Laplace, Part B Z transform)

Restructured 2026-08-03 from 8 labs to 6: **Fourier series is out of the lab
material entirely** (theory and gabinete only), which made the continuous
transform too thin for its own lab, so Fourier merged into L04; that in turn
required moving sampling up to L03, since an FFT cannot be computed without
first fixing `fs`. Laplace and Z merged into L05 because they were the same lab
in two planes. **L03 must not use anything from Fourier** — aliasing is
explained in the time domain, and the spectral reading is L04's opening.

There is **no complex-numbers lab** in this edition; its full scope is parked in
Annex A of `docs/PROJECT_PLAN.md` for a future edition. Do not delete it.

## CRITICAL: two different toolchains

Módulos and laboratorios are authored with **different** systems. Pick by file type.

### Módulos → `src/*.md` + `tools/md2nb.py`

**Never edit `MNN_*.ipynb` directly.**

1. Extract: `python tools/nb2md.py <notebook.ipynb>` → `src/<name>.md`
2. Edit the `.md` in `src/` (cell delimiters `%% md prov-01`, `%% code act-01`;
   header written as the single directive `@header`)
3. Rebuild: `python tools/md2nb.py src/<name>.md`

Full spec: `docs/FORMATO_CELDAS.md` (applies to **módulos only** since 2026-08-02).

### Laboratorios → `_fuente/sources/*.lab.md` + the `lab-notebook` contract

Labs follow the contract of the **`lab-notebook`** plugin (repo `lab-corrector`),
which is what makes them correctable by the grading app. **Load that skill before
writing or editing any lab** — the `cell_id` convention, the `.lab.md` format and
the style guide live there and are not duplicated here.

Because this repo is **public and serves GitHub Pages**, and a `.lab.md` embeds
the solution, sources and solutions live in a **separate private repo** cloned in
as `_fuente/` (gitignored). Only the generated enunciado is published.

```
ASyS-utn-frm/python  (PUBLIC)
├── Laboratorios/            ← generated enunciados, committed & published
└── _fuente/                 ← private repo, gitignored, NEVER committed
    ├── .labconfig.yaml      ← layout: enunciados ../Laboratorios, prefijo "L"
    ├── build.py             ← wrapper that expands @header, then calls lab_build.py
    ├── sources/*.lab.md     ← source of truth (enunciado + solution together)
    ├── Soluciones/*.ipynb   ← generated solutions, executed with outputs
    └── rubricas/            ← rubrics (the app generates the YAML ones)
```

Cycle:

```bash
cd _fuente
python build.py sources/L0X_tema.lab.md          # writes both notebooks
python <plugin>/scripts/lab_validate.py ../Laboratorios/L0X_tema.ipynb   # must be 0 errors
# then execute Soluciones/L0X_tema_Solucion.ipynb and save it WITH outputs
```

**Never commit anything under `_fuente/` to the public repo.** `git mv` on a
tracked file bypasses `.gitignore` — after moving anything in there, check with
`git ls-files | grep _fuente` (must be empty).

Contract details that differ from the old módulo format:
- Placeholders are exactly `# Tu código aquí` and `*(Escribí tu respuesta acá)*`
  (note the case — the old `# TU CÓDIGO AQUÍ` is no longer valid in labs).
- Student cell ids are `ejN-code` / `ejN-respuesta`, never `act-NN`.
- Every lab carries **preguntas de análisis** (`ejN-pregunta` + `ejN-respuesta`),
  a role the old format did not have.

### Grading

Rubrics are generated by the grading app from the enunciado/solución pair, so the
solution must be **executed and saved with its outputs**. `tools/extract_student.py`
belongs to the old flow and does not apply to contract-era labs.

## Cross-notebook decisions

When a change in one notebook implies something pending in another (e.g., "move triple-quote content from M01 to M02"), record it in `docs/CARRYOVERS.md`. Read that file before working on any module/lab and apply relevant pending items.

## Key Libraries

All notebooks assume Google Colab. Core dependencies:
- **NumPy** (`np`), **Matplotlib** (`plt`), **SymPy** (`sp`), **SciPy** (`signal`)

## Content Language

All reader-facing text in **Spanish** (Argentine voseo). Activity placeholders:
`# TU CÓDIGO AQUÍ` in módulos, `# Tu código aquí` in laboratorios (the contract
is case-sensitive and the validator checks it).

## Style Guide

**Read `docs/GUIA_ESTILO.md` §0 "Criterio rector" first.** These notebooks are
pedagogical documents: their only product is the reader's understanding, so **the
quality of the writing is the function of the material, not its finish**. A notebook
that compiles, validates and plots correctly but explains vaguely, names things
imprecisely or asserts unverified numbers **has failed at the one thing it had to
do**. Priority order when writing or reviewing: (1) clarity and exactness, (2) the
didactic path, (3) the technical contract, (4) format consistency. Items 3–4 are
necessary, script-checkable conditions — passing them adds no quality, it only lets
the work of item 1 reach the reader.

Full guidelines in `docs/GUIA_ESTILO.md`. Key principles:
- Tone: close and patient tutor, precise but not exhaustive
- **Register: semiformal and technically precise.** The close tone does not license
  colloquialisms. See §1 bis of the style guide: substitution table, exact technical
  vocabulary (*instante* vs *muestra*, índice, longitud, frecuencia de muestreo),
  the "define, don't just name" rule, and the requirement to verify every numeric
  claim and cross-module reference before writing it
- Never reference concepts not yet presented in earlier módulos
- Ascending difficulty within each notebook
- Cycle: explain → show (runnable example) → practice
- **No references to the professor/cátedra**: material must stand on its own
