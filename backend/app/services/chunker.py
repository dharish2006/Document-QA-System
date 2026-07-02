from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    raw_chunks = splitter.split_text(text)

    chunks = []

    for i, chunk in enumerate(raw_chunks):

        chunks.append({
            "id": i + 1,
            "text": chunk,
            "length": len(chunk)
        })

    return chunks