from app.services.pdf_loader import extract_text_from_pdf
from app.services.chunker import chunk_text
from app.services.embedding import generate_embeddings
from app.services.vector_store import store_chunks


def process_document(pdf_path, filename):
    """
    Complete ingestion pipeline:
    PDF -> Text -> Chunks -> Embeddings -> ChromaDB
    """

    result = extract_text_from_pdf(pdf_path)

    chunks = chunk_text(result["text"])

    chunks = generate_embeddings(chunks)

    store_chunks(chunks, filename)

    return len(chunks)