# AI-Powered Document Question Answering System using RAG and LLMs

An AI-powered Document Question Answering (Document Q&A) system that enables users to upload PDF documents and ask questions in natural language. The system uses Retrieval-Augmented Generation (RAG), semantic search, vector embeddings, and Large Language Models to provide accurate, context-aware answers with source citations.

---

## Features

- Upload PDF documents
- Extract text from PDFs
- Automatic document chunking
- Generate semantic embeddings
- Store embeddings in ChromaDB
- Semantic similarity search
- Question answering using Llama 3 via Ollama
- Source citation for every answer
- Modern React + Tailwind CSS frontend
- FastAPI backend
- ChatGPT-style chat interface
- Collapsible source references

---

## Tech Stack

### Backend

- Python
- FastAPI
- ChromaDB
- Sentence Transformers
- PyMuPDF
- Ollama
- Llama 3

### Frontend

- React
- Vite
- Tailwind CSS
- Axios

---

## Project Architecture

```
                User Uploads PDF
                       │
                       ▼
              PDF Text Extraction
                       │
                       ▼
                Document Chunking
                       │
                       ▼
            Generate Embeddings
                       │
                       ▼
              Store in ChromaDB
                       │
                       ▼
              User Asks Question
                       │
                       ▼
          Embed User Question
                       │
                       ▼
          Similarity Search (Top-K)
                       │
                       ▼
         Retrieve Relevant Chunks
                       │
                       ▼
      Context + Question → Llama 3
                       │
                       ▼
               AI Generated Answer
                       │
                       ▼
               Display Sources
```

---

## Folder Structure

```
DocumentQA/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── prompts/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   ├── chroma_db/
│   └── uploaded_docs/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## Workflow

1. Upload a PDF document.
2. Extract text from the document.
3. Split text into chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in ChromaDB.
6. Ask questions in natural language.
7. Retrieve relevant chunks using semantic search.
8. Generate answers using Llama 3.
9. Display the answer with supporting source chunks.

---

## API Endpoints

### Upload Document

```
POST /upload
```

Uploads and processes a PDF document.

---

### Ask Question

```
POST /ask
```

Request Body

```json
{
  "question": "What is the leave policy?"
}
```

---

### Health Check

```
GET /health
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/Document-QA-System.git

cd Document-QA-System
```

---

### Backend Setup

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

Run the backend

```bash
uvicorn app.main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

## Running Ollama

Ensure Ollama is installed.

Start Llama 3

```bash
ollama run llama3:8b
```

---

## Example

### Upload

```
Employee_Handbook.pdf
```

### Question

```
What is the work from home policy?
```

### Response

```
Employees may work remotely for up to three days per week, subject to manager approval.
```

### Sources

```
Employee_Handbook.pdf

Chunk 14
```

---

## Current Features

- PDF Upload
- Document Parsing
- Semantic Search
- RAG Pipeline
- Llama 3 Integration
- Source Citations
- Responsive React UI
- Tailwind CSS Styling

---

## Future Improvements

- Multiple document support
- DOCX and PPTX support
- OCR for scanned PDFs
- Streaming LLM responses
- Conversation history persistence
- Authentication
- User dashboard
- Document management
- Hybrid keyword + semantic search
- Docker deployment
- Cloud deployment
- Dark mode

---

## Screenshots
<img width="1849" height="456" alt="Screenshot 2026-07-02 105028" src="https://github.com/user-attachments/assets/3a08ff7b-cee2-4e40-93ef-028ff7abd8e7" />
<img width="1908" height="871" alt="Screenshot 2026-07-02 105550" src="https://github.com/user-attachments/assets/6aaacb3c-c786-4726-8c85-0f5ca1a03e1e" />
<img width="1386" height="815" alt="Screenshot 2026-07-02 105610" src="https://github.com/user-attachments/assets/5c569d3d-2620-40a1-8dae-d256d289185e" />

