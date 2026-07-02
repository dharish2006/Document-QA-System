from fastapi import APIRouter
from app.services.vector_store import collection

router = APIRouter()

@router.get("/debug/documents")
def get_documents():
    data = collection.get()

    return {
        "count": len(data["ids"]),
        "ids": data["ids"]
    }