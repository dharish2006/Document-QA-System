from fastapi import APIRouter

from app.models.question import QuestionRequest
from app.services.retriever import retrieve
from app.services.llm import generate_answer

router = APIRouter()


@router.post("/ask")
def ask(request: QuestionRequest):

    retrieved = retrieve(request.question)

    answer = generate_answer(
        request.question,
        retrieved["context"]
    )

    return {
        "question": request.question,
        "answer": answer,
        "sources": retrieved["chunks"]
    }