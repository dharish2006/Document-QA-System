from pathlib import Path
import chromadb

# Absolute path to backend/chroma_db
BACKEND_ROOT = Path(__file__).resolve().parents[2]
DB_PATH = BACKEND_ROOT / "chroma_db"

# Create/Open ChromaDB
client = chromadb.PersistentClient(path=str(DB_PATH))

COLLECTION_NAME = "documents"

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)


def store_chunks(chunks, filename):
    """
    Store chunk text and embeddings in ChromaDB.
    """

    for chunk in chunks:
        collection.add(
            ids=[f"{filename}_chunk_{chunk['id']}"],
            documents=[chunk["text"]],
            embeddings=[chunk["embedding"]],
            metadatas=[
                {
                    "source": filename,
                    "chunk_id": chunk["id"],
                }
            ],
        )


def search(query_embedding, top_k=3):
    """
    Search for the most similar chunks.
    """

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=[
            "documents",
            "metadatas",
            "distances",
        ],
    )

    return results

def reset_collection():
    """
    Delete and recreate the Chroma collection.
    """

    global collection

    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )