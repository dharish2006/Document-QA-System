from app.services.embedding import generate_query_embedding
from app.services.vector_store import search


def retrieve(question: str, top_k: int = 3):

    embedding = generate_query_embedding(question)

    results = search(embedding, top_k)

    retrieved = []

    context = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for doc, meta, distance in zip(documents, metadatas, distances):

        retrieved.append({
            "text": doc,
            "metadata": meta,
            "distance": distance
        })

        context.append(doc)

    return {
        "context": "\n\n".join(context),
        "chunks": retrieved
    }