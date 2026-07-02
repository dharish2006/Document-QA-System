from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil
from app.services.document_processor import process_document

router = APIRouter()

# Folder where uploaded PDFs will be stored
UPLOAD_DIR = Path("uploaded_docs")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Check file type
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Save file
    file_path = UPLOAD_DIR / file.filename
    from uuid import uuid4

    unique_name = f"{uuid4()}_{file.filename}"
    file_path = UPLOAD_DIR / unique_name

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    total_chunks = process_document(
    str(file_path),
    file.filename
    )

    return {
    "message": "Document processed successfully",
    "filename": file.filename,
    "chunks": total_chunks
}