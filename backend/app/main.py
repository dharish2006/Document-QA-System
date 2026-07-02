from contextlib import asynccontextmanager
from app.services.vector_store import reset_collection

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.ask import router as ask_router
from app.routes.chunk import router as chunk_router
from app.routes.debug import router as debug_router
from app.routes.embed import router as embed_router
from app.routes.extract import router as extract_router
from app.routes.upload import router as upload_router
from app.utils.startup import clean_uploaded_documents


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Document Q&A API...")

    clean_uploaded_documents()

    reset_collection()

    print("Development data cleaned.")

    yield

    print("Shutting down Document Q&A API...")


app = FastAPI(
    title="Document Q&A API",
    version="1.0.0",
    lifespan=lifespan,
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Document Q&A API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(upload_router)
app.include_router(extract_router)
app.include_router(chunk_router)
app.include_router(embed_router)
app.include_router(debug_router)
app.include_router(ask_router)