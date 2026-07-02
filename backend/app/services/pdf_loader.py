import fitz
from pathlib import Path


def extract_text_from_pdf(pdf_path: str):
    pdf_file = Path(pdf_path)

    if not pdf_file.exists():
        raise FileNotFoundError(pdf_path)

    document = fitz.open(pdf_file)

    pages = []
    full_text = ""

    for page_number, page in enumerate(document, start=1):
        text = page.get_text()

        pages.append({
            "page": page_number,
            "text": text
        })

        full_text += text

    document.close()

    return {
        "text": full_text,
        "pages": pages
    }