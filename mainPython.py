# save_to_txt.py

from pathlib import Path
from pypdf import PdfWriter
from pypdf import PdfReader
# /home/napoleon/WORKSPACE/Python311/mainPython.py
pdf_path = (
    Path.home()
    / "WORKSPACE" / "Python311" / "aaRS (1).pdf"
    # / "WORKSPACE" / "Python311" / "s41467-019-11331-5.pdf"
    # / "WORKSPACE" / "Python311" / "Pride_and_Prejudice.pdf"
)
pdf_path2 = (
    Path.home()
    # / "WORKSPACE" / "Python311" / "aaRS (1).pdf"
    # / "WORKSPACE" / "Python311" / "s41467-019-11331-5.pdf"
    / "WORKSPACE" / "Python311" / "TEST_PDF.pdf"
)
pdf_writer = PdfWriter(pdf_path2)
page = pdf_writer.add_blank_page(width=8.27 * 72, height=11.7 * 72)
pdf_writer.write(pdf_path2)
pdf_reader = PdfReader(pdf_path)
txt_file = Path.home() / "WORKSPACE" / "Python311" / "Pride_and_Prejudice.txt"
content = [
    f"{pdf_reader.metadata.title}",
    f"Number of pages: {len(pdf_reader.pages)}"
]

for page in pdf_reader.pages:
    content.append(page.extract_text())

txt_file.write_text("\n".join(content))

#END OF LINE feq