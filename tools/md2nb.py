#!/usr/bin/env python3
"""
md2nb.py — Convierte archivos Markdown fuente a Jupyter Notebooks (.ipynb).

Lee archivos .md con delimitadores %% y genera .ipynb con:
- IDs de celda determinísticos basados en el prefijo del notebook
- Metadata de rol (provided / student / enunciado / header) en cada celda
- Estructura JSON compatible con Jupyter 4.5 y Google Colab

Uso:
    python md2nb.py <fuente.md> [salida.ipynb]
    python md2nb.py --all          # Convierte todos los .md de src/
    python md2nb.py --watch src/   # (futuro) Modo watch
"""

import json
import re
import sys
import os
import glob
import argparse
import base64

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

# Patrón del delimitador de celda: %% tipo id
CELL_DELIM = re.compile(r'^%%\s+(md|code)\s+(\S+)\s*$')

# Ruta al logo UTN (relativo al directorio del proyecto)
LOGO_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', 'logoUTN.jpg')

# Plantilla de notebook
NOTEBOOK_TEMPLATE = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "colab": {"provenance": []},
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.10.0"
        }
    }
}


# ---------------------------------------------------------------------------
# Parseo del Markdown fuente
# ---------------------------------------------------------------------------

def parse_frontmatter(text):
    """Extrae frontmatter YAML simple y retorna (metadata_dict, resto_del_texto)."""
    if not text.startswith('---'):
        return {}, text

    end_idx = text.index('---', 3)
    fm_text = text[3:end_idx].strip()
    rest = text[end_idx + 3:].strip()

    metadata = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            metadata[key.strip()] = val.strip()

    return metadata, rest


def determine_role(cell_id):
    """Determina el rol de una celda a partir de su ID."""
    if cell_id.startswith('act'):
        return 'student'
    elif cell_id.startswith('enu'):
        return 'enunciado'
    elif cell_id.startswith('hdr'):
        return 'header'
    else:
        return 'provided'


def parse_cells(text, prefix):
    """Parsea el texto Markdown con delimitadores %% y genera lista de celdas."""
    cells = []
    lines = text.split('\n')

    current_type = None
    current_id = None
    current_lines = []

    for line in lines:
        match = CELL_DELIM.match(line)
        if match:
            # Guardar celda anterior
            if current_type is not None:
                cells.append(build_cell(current_type, current_id, current_lines, prefix))

            current_type = match.group(1)
            current_id = match.group(2)
            current_lines = []
        else:
            current_lines.append(line)

    # Guardar última celda
    if current_type is not None:
        cells.append(build_cell(current_type, current_id, current_lines, prefix))

    return cells


def build_cell(cell_type, cell_id, lines, prefix):
    """Construye un dict de celda para el notebook JSON."""
    # Limpiar líneas vacías al inicio y final
    while lines and lines[0].strip() == '':
        lines.pop(0)
    while lines and lines[-1].strip() == '':
        lines.pop()

    full_id = f"{prefix}-{cell_id}"
    role = determine_role(cell_id)

    # Convertir líneas a formato source (cada línea termina en \n excepto la última)
    source = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            source.append(line + '\n')
        else:
            source.append(line)

    cell = {
        "cell_type": "markdown" if cell_type == "md" else "code",
        "id": full_id,
        "metadata": {
            "role": role
        },
        "source": source
    }

    if cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = []

    return cell


# ---------------------------------------------------------------------------
# Generación del notebook
# ---------------------------------------------------------------------------

def make_notebook(cells):
    """Envuelve las celdas en la estructura de notebook."""
    nb = dict(NOTEBOOK_TEMPLATE)
    nb["cells"] = cells
    return nb


def convert(input_path, output_path=None):
    """Convierte un archivo Markdown fuente a .ipynb."""
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    frontmatter, body = parse_frontmatter(text)

    # El prefijo se usa para generar IDs completos
    prefix = frontmatter.get('prefix', os.path.splitext(os.path.basename(input_path))[0])

    cells = parse_cells(body, prefix)

    if not cells:
        print(f"  ⚠ {input_path}: no se encontraron celdas (¿faltan delimitadores %%?)")
        return

    notebook = make_notebook(cells)

    if output_path is None:
        # Generar nombre basado en el archivo fuente
        basename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = basename + '.ipynb'

    # Crear directorio de salida si no existe
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=1)

    print(f"  {os.path.basename(input_path)} → {output_path}  ({len(cells)} celdas)")
    return output_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Convierte archivos Markdown fuente a Jupyter Notebooks'
    )
    parser.add_argument(
        'input', nargs='?',
        help='Archivo .md a convertir'
    )
    parser.add_argument(
        'output', nargs='?',
        help='Archivo .ipynb de salida'
    )
    parser.add_argument(
        '--all', action='store_true',
        help='Convertir todos los .md de src/'
    )
    parser.add_argument(
        '--src', default='src',
        help='Directorio de fuentes (con --all, por defecto: src/)'
    )

    args = parser.parse_args()

    if args.all:
        pattern = os.path.join(args.src, '*.md')
        files = sorted(glob.glob(pattern))
        if not files:
            print(f"No se encontraron archivos .md en {args.src}")
            sys.exit(1)
        print(f"Convirtiendo {len(files)} archivos:")
        for f in files:
            convert(f)
        print("Listo.")
    elif args.input:
        convert(args.input, args.output)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
