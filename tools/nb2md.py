#!/usr/bin/env python3
"""
nb2md.py — Convierte Jupyter Notebooks (.ipynb) a formato Markdown fuente.

El formato Markdown fuente usa delimitadores %% para marcar celdas,
permitiendo editar notebooks como texto plano y luego reconvertir con md2nb.py.

Uso:
    python nb2md.py <notebook.ipynb> [salida.md]
    python nb2md.py --all   # Convierte todos los .ipynb del directorio actual
"""

import json
import sys
import os
import re
import glob
import argparse


# ---------------------------------------------------------------------------
# Detección de rol de celda
# ---------------------------------------------------------------------------

# Patrones que indican celda de actividad del alumno
STUDENT_PATTERNS = [
    r'TU\s+C[OÓ]DIGO\s+AQU[IÍ]',
    r'COMPLETAR',
    r'RESOLVER',
    r'# tu código',
    r'# tu codigo',
]

# Patrones que indican enunciado de actividad
ENUNCIADO_PATTERNS = [
    r'(?:^|\n)\s*#{1,4}\s*(?:Actividad|Ejercicio|Problema)',
    r'🔧|🌟|🚀|🎯|📝|✏️',
]

# Patrones de encabezado/logo
HEADER_PATTERNS = [
    r'base64',
    r'logoUTN',
    r'An[aá]lisis de Se[nñ]ales',
]


def detect_role(cell):
    """Determina el rol de una celda a partir de su contenido y metadata."""
    # Si ya tiene rol en metadata, usarlo
    existing_role = cell.get('metadata', {}).get('role')
    if existing_role:
        return existing_role

    source = ''.join(cell.get('source', []))
    cell_type = cell['cell_type']

    # Código vacío o con placeholder → actividad del alumno
    if cell_type == 'code':
        stripped = source.strip()
        if not stripped:
            return 'student'
        for pat in STUDENT_PATTERNS:
            if re.search(pat, source, re.IGNORECASE):
                return 'student'
        return 'provided'

    # Markdown: verificar si es header/logo
    for pat in HEADER_PATTERNS:
        if re.search(pat, source, re.IGNORECASE):
            return 'header'

    # Markdown: verificar si es enunciado de actividad
    for pat in ENUNCIADO_PATTERNS:
        if re.search(pat, source):
            return 'enunciado'

    return 'provided'


# ---------------------------------------------------------------------------
# Conversión notebook → markdown
# ---------------------------------------------------------------------------

ROLE_TO_PREFIX = {
    'header': 'hdr',
    'provided': 'prov',
    'enunciado': 'enu',
    'student': 'act',
}


def notebook_to_markdown(nb_path, output_path=None):
    """Convierte un archivo .ipynb a formato Markdown fuente."""
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    basename = os.path.splitext(os.path.basename(nb_path))[0]

    lines = []
    lines.append('---')
    lines.append(f'prefix: {basename}')
    lines.append(f'source: {os.path.basename(nb_path)}')
    lines.append('---')
    lines.append('')

    # Contadores por rol para generar IDs secuenciales
    counters = {}

    for cell in nb.get('cells', []):
        cell_type = 'md' if cell['cell_type'] == 'markdown' else 'code'
        role = detect_role(cell)

        # Generar ID
        prefix = ROLE_TO_PREFIX.get(role, 'prov')
        counters[prefix] = counters.get(prefix, 0) + 1
        cell_id = f"{prefix}-{counters[prefix]:02d}"

        # Si la celda ya tiene un ID significativo del notebook, anotarlo
        existing_id = cell.get('id', '')

        # Escribir delimitador de celda
        lines.append(f'%% {cell_type} {cell_id}')

        # Escribir contenido
        source = ''.join(cell.get('source', []))
        # Encabezado con imagen embebida → colapsar a directiva @header
        # (el contenido real vive en src/_header.md y md2nb.py lo expande al convertir)
        if role == 'header' and 'base64,' in source:
            lines.append('@header')
        else:
            lines.append(source)
        lines.append('')

    result = '\n'.join(lines)

    if output_path is None:
        output_path = os.path.join('src', basename + '.md')

    # Crear directorio de salida si no existe
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

    cell_count = len(nb.get('cells', []))
    print(f"  {os.path.basename(nb_path)} → {output_path}  ({cell_count} celdas)")
    return output_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Convierte Jupyter Notebooks a formato Markdown fuente'
    )
    parser.add_argument(
        'input', nargs='?',
        help='Archivo .ipynb a convertir'
    )
    parser.add_argument(
        'output', nargs='?',
        help='Archivo .md de salida (por defecto: src/<nombre>.md)'
    )
    parser.add_argument(
        '--all', action='store_true',
        help='Convertir todos los .ipynb del directorio actual'
    )
    parser.add_argument(
        '--dir', default='.',
        help='Directorio donde buscar .ipynb (con --all)'
    )

    args = parser.parse_args()

    if args.all:
        pattern = os.path.join(args.dir, '*.ipynb')
        files = sorted(glob.glob(pattern))
        if not files:
            print(f"No se encontraron archivos .ipynb en {args.dir}")
            sys.exit(1)
        print(f"Convirtiendo {len(files)} notebooks:")
        for f in files:
            notebook_to_markdown(f)
        print("Listo.")
    elif args.input:
        notebook_to_markdown(args.input, args.output)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
