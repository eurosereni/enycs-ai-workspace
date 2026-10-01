"""Genera JSON (per il CMS) e PDF (per la revisione) da una bozza di approfondimento in Markdown.

La bozza deve avere tre parti, nell'ordine:
  1. scheda editoriale interna (dal titolo fino a "## Articolo");
  2. "## Articolo": titolo "# ...", testo, fonti;
  3. "## Materiali di distribuzione (per revisione)": Slug, Meta title (≤60),
     Meta description (≤155), CTA proposta, Post LinkedIn (bozza), Sintesi newsletter (2 righe).

Uso (dalla cartella della bozza):
  python3 strumenti/build.py approfondimento-dco-retail-draft3.md \
      "bozza 3 (umanizzata), pronta per revisione di Euro — non pubblicata" "draft3 2026-09-24"

Produce accanto al .md un .json e un .pdf con lo stesso nome. Il PDF contiene l'articolo e,
in appendice, la scheda interna e i materiali di distribuzione. Font: DejaVu di sistema.
Librerie: strumenti/requirements.txt.
"""
import json, re, sys, markdown
from fpdf import FPDF
from fpdf.fonts import FontFace

src = sys.argv[1]; base = src[:-3]
STATUS = sys.argv[2] if len(sys.argv) > 2 else "bozza, pronta per revisione di Euro — non pubblicata"
VERSION = sys.argv[3] if len(sys.argv) > 3 else ""
s = open(src, encoding='utf-8').read()
head, rest = s.split('\n## Articolo\n', 1)
art, dist = rest.split('\n## Materiali di distribuzione (per revisione)\n', 1)
art = art.strip().rstrip('-').strip()
title = art.splitlines()[0].lstrip('# ').strip()
body = art.split('\n', 1)[1].strip()
g = lambda k: re.search(r'\*\*' + k + r':\*\*\s*`?([^`\n]+)`?', dist).group(1).strip()
d = {"title": title, "slug": g('Slug'), "meta_title": g(r'Meta title \(≤60\)'),
     "meta_description": g(r'Meta description \(≤155\)'),
     "status": STATUS, "version": VERSION,
     "angle_note": head.split('\n', 1)[1].strip(), "body_markdown": body, "cta": g('CTA proposta'),
     "linkedin_draft": dist.split('**Post LinkedIn (bozza):**')[1].split('**Sintesi newsletter')[0].strip(),
     "newsletter_summary": dist.split('**Sintesi newsletter (2 righe):**')[1].strip()}
json.dump(d, open(base + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(len(d['meta_title']), len(d['meta_description']), len(body.split()), 'parole')

F = '/usr/share/fonts/truetype/dejavu/'

def html_of(md):
    h = markdown.markdown(md, extensions=['tables'])
    h = h.replace('<table>', '<table width="100%">')
    h = re.sub(r'(<t[dh](?:\s[^>]*)?>)(.*?)(</t[dh]>)',
               lambda m: m.group(1) + re.sub(r'<[^>]+>', '', m.group(2)) + m.group(3), h, flags=re.S)
    h = h.replace('<td>', '<td align="left">')
    return h

def prep(md):
    """Note interne: ogni riga resta una riga; liste staccate dal paragrafo."""
    out = []
    for line in md.split('\n'):
        is_item = bool(re.match(r'\s*(- |\d+\. )', line))
        if out and line.strip() and not is_item and out[-1].strip() and not re.match(r'\s*(- |\d+\. )', out[-1]):
            out.append('')
        if is_item and out and out[-1].strip() and not re.match(r'\s*(- |\d+\. )', out[-1]):
            out.append('')
        out.append(line)
    return '\n'.join(out)

class P(FPDF):
    def footer(self):
        self.set_y(-12); self.set_font('S', '', 8); self.set_text_color(120)
        self.cell(0, 8, f'DSKU · bozza per revisione · non pubblicata · pag. {self.page_no()}', align='C')

pdf = P(); pdf.set_margins(18, 16, 18); pdf.set_auto_page_break(True, 16)
pdf.add_font('S', '', F + 'DejaVuSans.ttf'); pdf.add_font('S', 'B', F + 'DejaVuSans-Bold.ttf')
pdf.add_font('S', 'I', F + 'DejaVuSans.ttf'); pdf.add_font('S', 'BI', F + 'DejaVuSans-Bold.ttf')
pdf.add_page(); pdf.set_font('S', '', 10)
tag = dict(h1=FontFace(color=(20, 40, 80), size_pt=18, emphasis='B'),
           h2=FontFace(color=(20, 40, 80), size_pt=14, emphasis='B'),
           h3=FontFace(color=(20, 70, 120), size_pt=12.5, emphasis='B'))

def put(md):
    pdf.write_html(html_of(md), tag_styles=tag, table_line_separators=True, font_family='S')

put('# ' + title + '\n\n' + body)
pdf.add_page()
put('## Scheda editoriale (interna)\n\n' + prep(head.split('\n', 1)[1].strip()))
put('\n\n## Materiali di distribuzione\n\n' + prep(dist.strip()))
pdf.output(base + '.pdf'); print('pdf ok')
