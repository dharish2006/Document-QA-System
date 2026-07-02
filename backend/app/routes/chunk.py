from fastapi import APIRouter, HTTPException
from pathlib import Path

from app.services.pdf_loader import extract_text_from_pdf
from app.services.chunker import chunk_text

router = APIRouter()

UPLOAD_DIR = Path("uploaded_docs")


@router.get("/chunk/{filename}")
def chunk_document(filename: str):

    pdf_path = UPLOAD_DIR / filename

    if not pdf_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found."
        )

    result = extract_text_from_pdf(str(pdf_path))

    chunks = chunk_text(result["text"])

    return {
        "filename": filename,
        "total_chunks": len(chunks),
        "chunks": chunks
    }