# scripts/extract_sections.py
import fitz  # PyMuPDF

def extract_sections_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            for line in block.get("lines", []):
                text_line = " ".join([span["text"] for span in line.get("spans", [])]).strip()
                font_size = max([span["size"] for span in line.get("spans", [])]) if line.get("spans") else 0

                if len(text_line) > 20 and font_size > 10:
                    sections.append({
                        "title": text_line.split('.')[0][:50],
                        "text": text_line,
                        "page": page_num + 1
                    })
    return sections
