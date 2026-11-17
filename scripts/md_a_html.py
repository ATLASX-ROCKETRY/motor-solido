"""Convierte un documento .md en formato de hoja dividida en una página HTML.

Uso:
    pip install markdown
    python3 scripts/md_a_html.py ejemplos/00_mision_comun.md ejemplos/mision_comun.html

La página resultante se ve igual que la versión publicada en el chat y se
puede abrir en el navegador o publicar con GitHub Pages. El estilo está en
scripts/hoja.css. Hay que volver a ejecutar este script cada vez que cambie
el .md, para que la página quede igual al documento.
"""
import re, sys, html
import markdown

src, salida = sys.argv[1:3]
md = open(src, encoding="utf-8").read()
import os
estilo = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "hoja.css"), encoding="utf-8").read()

# --- proteger matemáticas ---
math = []
def guardar(m):
    t = m.group(0).replace("<", r"\lt ").replace(">", r"\gt ")
    math.append(t)
    return f"@@M{len(math)-1}@@"
def proteger(t):
    t = re.sub(r"\$\$.+?\$\$", guardar, t, flags=re.S)
    t = re.sub(r"(?<!\$)\$(?!\$)[^$\n]+?\$", guardar, t)
    return t
def restaurar(t):
    return re.sub(r"@@M(\d+)@@", lambda m: html.escape(math[int(m.group(1))], quote=False), t)
def md2h(t):
    return restaurar(markdown.markdown(proteger(t.strip()), extensions=["tables", "sane_lists"]))

# --- separar secciones ---
partes = re.split(r"^## ", md, flags=re.M)
cabecera, secciones = partes[0], partes[1:]

def envolver_tablas(h):
    return re.sub(r"(<table>.*?</table>)", r'<div class="tabla">\1</div>', h, flags=re.S)

def fila(res, nota):
    res_h = envolver_tablas(md2h(res))
    nota_txt = nota.strip()
    if nota_txt.startswith("*") and "no hay suposiciones" in nota_txt or "Fila de definiciones" in nota_txt:
        return f'<div class="fila"><div class="res">{res_h}</div><div class="nota sin"><p class="vacia">{md2h(nota_txt)[3:-4]}</p></div></div>'
    return f'<div class="fila"><div class="res">{res_h}</div><div class="nota">{envolver_tablas(md2h(nota_txt))}</div></div>'

def resultado(bloque):
    lineas = [l[1:].strip() for l in bloque.strip().splitlines() if l.startswith(">")]
    lineas = [l for l in lineas if l]
    res = next((l for l in lineas if l.startswith("**Resultado")), "")
    sig = next((l for l in lineas if "Con este resultado" in l), "")
    res = re.sub(r"^\*\*Resultado[^*]*:\*\*\s*", "", res)
    sig = re.sub(r"^\*\*Con este resultado →\*\*\s*", "", sig)
    return ('<div class="resultado"><div><b class="etq">Resultado</b>'
            f'<div class="valor">{md2h(res)}</div></div>'
            f'<div class="sig"><b class="etq">Con este resultado →</b>{md2h(sig)}</div></div>')

out = []
for sec in secciones:
    titulo, _, cuerpo = sec.partition("\n")
    titulo = titulo.strip()
    cuerpo = cuerpo.replace("\n---\n", "\n").strip()
    if cuerpo.endswith("---"):
        cuerpo = cuerpo[:-3]
    ident = re.sub(r"[^a-z0-9]+", "-", titulo.lower().split("—")[0].strip()).strip("-")

    if titulo.startswith("Cómo leer"):
        out.append('<section class="leyenda" aria-label="Cómo leer"><div><b>Resolución</b><span>Qué se calcula, con qué ecuación, qué significa cada término y el resultado.</span></div>'
                   '<div class="l-nota"><b>Suposición y análisis</b><span>Cada simplificación o dato supuesto, por qué se acepta y cuánto cambia el resultado si no se cumple. Solo usa lo calculado hasta ese paso.</span></div></section>')
        seq = re.search(r"\*\*Secuencia:\*\*(.*)", cuerpo).group(1)
        chips = "".join(f'<a href="#{re.sub(r"[^a-z0-9]+","-",c.strip().lower().split("(")[0].strip()).strip("-")}">{html.escape(c.strip())}</a><i>→</i>' for c in seq.split("→"))
        out.append(f'<nav class="flujo" aria-label="Secuencia">{chips[:-8]}</nav>')
        continue
    if titulo.startswith("Resumen"):
        out.append(f'<section class="resumen" id="{ident}"><h2>{html.escape(titulo)}</h2>{envolver_tablas(md2h(cuerpo))}</section>')
        continue

    m = re.match(r"(Paso \d+)\s*—\s*(.*)", titulo)
    if m:
        eyebrow, h2 = m.group(1), m.group(2)
    else:
        eyebrow, h2 = "Datos de entrada", titulo
    antes, _, resto = cuerpo.partition("<table>")
    tabla, _, despues = resto.partition("</table>")
    cab = []
    for p in [x.strip() for x in antes.strip().split("\n\n") if x.strip()]:
        if p.startswith("**Pregunta"):
            cab.append(f'<p class="pregunta">{md2h(p)[3:-4]}</p>')
        elif p.startswith("**Viene") or p.startswith("Cálculo"):
            cab.append(f'<p class="viene">{md2h(p)[3:-4]}</p>')
        else:
            cab.append(f'<div class="aclara">{md2h(p)}</div>')
    filas = []
    for tr in re.findall(r"<tr>(.*?)</tr>", tabla, flags=re.S):
        celdas = re.findall(r"<td[^>]*>(.*?)</td>", tr, flags=re.S)
        if len(celdas) == 2:
            filas.append(fila(*celdas))
    num = eyebrow.split()[-1] if m else "P"
    out.append(f'<article class="paso" id="{ident}"><div class="paso-cab"><div class="eyebrow">{eyebrow}</div><h2>{html.escape(h2)}</h2>{"".join(cab)}</div>'
               f'<div class="colcab"><div>Resolución</div><div>Suposición y análisis</div></div>{"".join(filas)}{resultado(despues)}</article>')

# --- cabecera del documento ---
cab_lineas = cabecera.strip().splitlines()
intro_md = "\n".join(l for l in cab_lineas[1:] if not l.startswith("Ecuaciones:") and not l.startswith("Cálculo:"))

extra_css = ""

pagina = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Misión común Atlas X</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Space+Grotesk:wght@500;600;700&display=swap">
<script>
window.MathJax = {{ tex: {{ inlineMath: [['$', '$']], displayMath: [['$$', '$$']] }}, svg: {{ fontCache: 'global' }}, options: {{ enableMenu: false }} }};
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.min.js"></script>
<style>{estilo}{extra_css}</style>
</head>
<body>
<main class="doc">
<header class="intro">
  <div class="eyebrow">Atlas X · Propulsión · Motor sólido KNSB</div>
  <h1>Misión común: pasos 1 a 7</h1>
  {md2h(intro_md)}
</header>
{"".join(out)}
</main>
</body>
</html>
"""
open(salida, "w", encoding="utf-8").write(pagina)
print("ok", len(out), "bloques;", len(math), "fórmulas")
