import sys
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

# Quarto passes the output file path as argument
output_file = sys.argv[1] if len(sys.argv) > 1 else None

if not output_file or not output_file.endswith(".docx"):
    sys.exit(0)

doc = Document(output_file)

count = 0
for para in doc.paragraphs:
    has_image = (
        para._element.findall(".//" + qn("w:drawing")) or
        para._element.findall(".//" + qn("a:blip"), {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"})
    )
    if has_image:
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        count += 1

doc.save(output_file)
print(f"[center-images] {count} imagem(ns) centralizada(s) em {output_file}")
