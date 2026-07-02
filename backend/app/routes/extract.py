from fastapi import APIRouter, HTTPException
from pathlib import Path

from app.services.pdf_loader import extract_text_from_pdf

router = APIRouter()

UPLOAD_DIR = Path("uploaded_docs")


@router.get("/extract/{filename}")
def extract_pdf(filename: str):
    pdf_path = UPLOAD_DIR / filename

    if not pdf_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found."
        )

    text = extract_text_from_pdf(str(pdf_path))

    return {
        "filename": filename,
        "characters": len(text),
        "text": text
    }