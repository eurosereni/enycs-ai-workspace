"""Converte in PDF un documento di prompt per le immagini, scritto in Markdown.

Uso (dalla cartella dell'approfondimento):
  python3 strumenti/prompt_pdf.py prompt-vetrina-meteo-v1.md
Produce prompt-vetrina-meteo-v1.pdf accanto al .md. I prompt da incollare vanno scritti come
citazione (righe che iniziano con "> "), così nel PDF risultano in blu. Per le sottoliste usare
4 spazi di rientro. Librerie: strumenti/requirements.txt.
"""
import re, sys, markdown
from fpdf import FPDF
from fpdf.fonts import FontFace
src = sys.argv[1]; md = open(src, encoding='utf-8').read()
md = re.sub(r'(?<=\S)\n(?=\*\*)', '\n\n', md)
h = markdown.markdown(md)
h = re.sub(r'<hr\s*/?>', '<br>', h)
F = '/usr/share/fonts/truetype/dejavu/'
class P(FPDF):
    def footer(self):
        self.set_y(-12); self.set_font('S', '', 8); self.set_text_color(120)
        self.cell(0, 8, f'DSKU · prompt immagini · pag. {self.page_no()}', align='C')
pdf = P(); pdf.set_margins(18, 16, 18); pdf.set_auto_page_break(True, 16)
pdf.add_font('S', '', F + 'DejaVuSans.ttf'); pdf.add_font('S', 'B', F + 'DejaVuSans-Bold.ttf')
pdf.add_font('S', 'I', F + 'DejaVuSans.ttf'); pdf.add_font('S', 'BI', F + 'DejaVuSans-Bold.ttf')
pdf.add_page(); pdf.set_font('S', '', 10)
tag = dict(h1=FontFace(color=(20, 40, 80), size_pt=18, emphasis='B'),
           h2=FontFace(color=(20, 40, 80), size_pt=13.5, emphasis='B'),
           blockquote=FontFace(color=(25, 60, 110)))
pdf.write_html(h, tag_styles=tag, font_family='S')
pdf.output(src[:-3] + '.pdf'); print('ok')
