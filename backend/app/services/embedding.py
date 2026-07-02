from sentence_transformers import SentenceTransformer

# Load model once when the application starts
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text: str):
    """
    Generate an embedding for a single piece of text.
    """
    return model.encode(text).tolist()


def generate_embeddings(chunks):
    """
    Generate embeddings for a list of chunks.

    Input:
    [
        {
            "id": 1,
            "text": "...",
            "length": 400
        }
    ]

    Output:
    [
        {
            "id": 1,
            "text": "...",
            "length": 400,
            "embedding": [...]
        }
    ]
    """

    for chunk in chunks:
        chunk["embedding"] = model.encode(chunk["text"]).tolist()

    return chunks
def generate_query_embedding(question: str):
    """
    Generate an embedding for the user's question.
    """
    return model.encode(question).tolist()