from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.services.pdf_loader import extract_text_from_pdf
from app.services.chunker import chunk_text
from app.services.embedding import generate_embeddings

router = APIRouter()

UPLOAD_DIR = Path("uploaded_docs")


@router.get("/embed/{filename}")
def embed_document(filename: str):

    pdf_path = UPLOAD_DIR / filename

    if not pdf_path.exists():
        raise HTTPException(
            status_code=404,
            detail="PDF not found."
        )

    result = extract_text_from_pdf(str(pdf_path))

    chunks = chunk_text(result["text"])

    chunks = generate_embeddings(chunks)

    return {
        "filename": filename,
        "total_chunks": len(chunks),
        "embedding_dimension": len(chunks[0]["embedding"]),
        "first_chunk": chunks[0]
    }