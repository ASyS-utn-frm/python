
<div style="text-align: center;">
  <img src="resources/logoUTN.jpg" alt="Logo UTN">
</div>




# Curso introductorio de Python para Análisis de Señales y Sistemas

Este es un **curso introductorio** de Python orientado al análisis de señales y sistemas. Está pensado para estudiantes del Departamento de Ingeniería en Tecnologías Electrónicas de la Universidad Tecnológica Nacional, Facultad Regional Mendoza, que tengan poca experiencia previa con programación.

El material se desarrolla como una serie de Jupyter Notebooks pensados para ejecutarse en Google Colab, una plataforma en la nube que permite correr código Python directamente desde el navegador, sin instalaciones locales.

## Cómo está organizado

El curso tiene dos tipos de notebooks:

- **Módulos** (prefijo `M`): notebooks expositivos que presentan, de a poco, las herramientas del lenguaje (variables, colecciones, control de flujo, funciones, clases, NumPy, Matplotlib y SymPy). Están pensados para leerse y ejecutarse, e incluyen actividades cortas para practicar cada concepto sobre la marcha.
- **Laboratorios** (prefijo `L`): notebooks **entregables** en los que se aplican las herramientas de los módulos a problemas concretos de electrónica y telecomunicaciones.

## Cómo trabajar con el material

Para abrir un notebook, hacé clic en el botón **Open in Colab** de la tabla correspondiente. Se recomienda estar autenticado con una cuenta de Google para que Colab guarde una copia editable en tu Drive.

En los **módulos** podés modificar el código libremente: la idea es que experimentes para fijar los conceptos.

En los **laboratorios** vas a encontrar celdas marcadas con el comentario `# Tu código aquí` y celdas de respuesta con el texto `*(Escribí tu respuesta acá)*`. Esas son las únicas celdas que debés modificar.


# Módulos


<table>
  <thead>
    <tr>
      <th>Tema</th>
      <th>Notebook del módulo</th>
      <th>Laboratorio de cierre</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1. Introducción a Google Colab</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/M01_introduccion_colab.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
      <td rowspan="9"><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/Laboratorios/L00_practica_python.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
    <tr>
      <td>2. Tipos de datos y variables</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/M02_tipos_de_datos.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
    <tr>
      <td>3. Colecciones: listas, tuplas, diccionarios, conjuntos</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/M03_colecciones.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
    <tr>
      <td>4. Estructuras de control: condicionales y bucles</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/M04_estructuras_de_control.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
    <tr>
      <td>5. Funciones</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/M05_funciones.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
    <tr>
      <td>6. Clases y objetos</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/M06_clases_objetos.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
    <tr>
      <td>7. NumPy</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/M07_numpy.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
    <tr>
      <td>8. Matplotlib</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/M08_matplotlib.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
    <tr>
      <td>9. SymPy</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/M09_sympy.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
  </tbody>
</table>


# Laboratorios

El Laboratorio 0 cierra la parte introductoria de Python y es el primer entregable del curso. Los laboratorios 1 a 5 aplican esas herramientas a los temas de la asignatura.

Cada laboratorio combina **celdas de código**, donde escribís la solución, y **preguntas de análisis**, donde explicás con tus palabras qué observaste. Las dos cosas se corrigen.

<table>
  <thead>
    <tr>
      <th>Laboratorio</th>
      <th>Notebook</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Laboratorio 0 — Práctica integradora de Python</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/Laboratorios/L00_practica_python.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
    <tr>
      <td>Laboratorio 1 — Señales y operaciones</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/Laboratorios/L01_senales_y_operaciones.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
    <tr>
      <td>Laboratorio 2 — Convolución</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/Laboratorios/L02_convolucion.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
    <tr>
      <td>Laboratorio 3 — Muestreo</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/Laboratorios/L03_muestreo.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
    <tr>
      <td>Laboratorio 4 — Fourier, del continuo al discreto</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/Laboratorios/L04_fourier.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
    <tr>
      <td>Laboratorio 5 — Análisis de sistemas: Laplace y transformada Z</td>
      <td><a href="https://colab.research.google.com/github/ASyS-utn-frm/python/blob/main/Laboratorios/L05_analisis_de_sistemas.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg"  alt="Open In Colab"></a></td>
    </tr>
  </tbody>
</table>





# Autor

Material desarrollado por el Mg. Ing. Javier Ignacio Velez, docente de la Universidad Tecnológica Nacional, Facultad Regional Mendoza.
