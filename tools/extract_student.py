#!/usr/bin/env python3
"""
extract_student.py — Extrae celdas de alumno de un notebook entregado.

Genera un JSON mínimo con solo las celdas de actividad (role: student)
y sus enunciados asociados, ideal para:
  1. Corrección automatizada con IA (mínimos tokens)
  2. Comparación contra rúbrica

Uso:
    python extract_student.py <entregado.ipynb>
    python extract_student.py <entregado.ipynb> --rubric rubrics/TP1_rubric.md
    python extract_student.py <entregado.ipynb> --format markdown
"""

import json
import sys
import os
import re
import argparse


def extract_outputs_text(outputs):
    """Extrae texto legible de los outputs de una celda de código."""
    texts = []
    for out in outputs:
        if out.get('output_type') == 'stream':
            texts.append(''.join(out.get('text', [])))
        elif out.get('output_type') in ('execute_result', 'display_data'):
            data = out.get('data', {})
            if 'text/plain' in data:
                texts.append(''.join(data['text/plain']))
        elif out.get('output_type') == 'error':
            texts.append(f"ERROR: {out.get('ename', '')}: {out.get('evalue', '')}")
    return '\n'.join(texts) if texts else None


def extract_student_cells(nb_path):
    """Extrae celdas de alumno y enunciados de un notebook."""
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    cells = []
    last_enunciado = None

    for cell in nb.get('cells', []):
        cell_id = cell.get('id', '')
        role = cell.get('metadata', {}).get('role', '')
        source = ''.join(cell.get('source', []))

        # Detectar rol por heurística si no hay metadata
        if not role:
            if cell['cell_type'] == 'code':
                stripped = source.strip()
                if not stripped or re.search(r'TU\s+C[OÓ]DIGO', source, re.IGNORECASE):
                    role = 'student'
            elif cell['cell_type'] == 'markdown':
                if re.search(r'(?:Actividad|Ejercicio)', source):
                    role = 'enunciado'

        if role == 'enunciado':
            last_enunciado = {
                'id': cell_id,
                'source': source
            }
        elif role == 'student':
            entry = {
                'id': cell_id,
                'type': cell['cell_type'],
                'source': source,
            }

            # Incluir enunciado asociado (el inmediatamente anterior)
            if last_enunciado:
                entry['enunciado'] = last_enunciado
                last_enunciado = None

            # Incluir outputs si es celda de código
            if cell['cell_type'] == 'code':
                output_text = extract_outputs_text(cell.get('outputs', []))
                if output_text:
                    entry['output'] = output_text

            cells.append(entry)

    return {
        'notebook': os.path.basename(nb_path),
        'total_activities': len(cells),
        'cells': cells
    }


def format_as_markdown(data, rubric_text=None):
    """Formatea la extracción como Markdown legible."""
    lines = []
    lines.append(f"# Corrección: {data['notebook']}")
    lines.append(f"Total de actividades: {data['total_activities']}")
    lines.append('')

    for i, cell in enumerate(data['cells'], 1):
        lines.append(f"## Actividad {i}")
        lines.append(f"**ID:** `{cell.get('id', 'sin-id')}`")
        lines.append('')

        if 'enunciado' in cell:
            lines.append("### Enunciado")
            lines.append(cell['enunciado']['source'])
            lines.append('')

        lines.append("### Respuesta del alumno")
        lines.append(f"```python\n{cell['source']}\n```")
        lines.append('')

        if 'output' in cell:
            lines.append("### Salida")
            lines.append(f"```\n{cell['output']}\n```")
            lines.append('')

        lines.append('---')
        lines.append('')

    if rubric_text:
        lines.append("## Rúbrica")
        lines.append(rubric_text)

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Extrae celdas de alumno para corrección'
    )
    parser.add_argument(
        'notebook',
        help='Notebook .ipynb entregado por el alumno'
    )
    parser.add_argument(
        '--rubric',
        help='Archivo de rúbrica .md para incluir en la salida'
    )
    parser.add_argument(
        '--format', choices=['json', 'markdown'], default='json',
        help='Formato de salida (default: json)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Archivo de salida (default: stdout)'
    )

    args = parser.parse_args()

    data = extract_student_cells(args.notebook)

    rubric_text = None
    if args.rubric and os.path.exists(args.rubric):
        with open(args.rubric, 'r', encoding='utf-8') as f:
            rubric_text = f.read()

    if args.format == 'markdown':
        result = format_as_markdown(data, rubric_text)
    else:
        if rubric_text:
            data['rubric'] = rubric_text
        result = json.dumps(data, ensure_ascii=False, indent=2)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"Extracción guardada en {args.output}")
    else:
        print(result)


if __name__ == '__main__':
    main()
