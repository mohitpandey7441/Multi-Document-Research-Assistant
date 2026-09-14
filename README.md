# 🤖 Multi-Document Research Assistant using RAG

An AI-powered **Multi-Document Research Assistant** built with **Python, Streamlit, LangChain, ChromaDB, Hugging Face, and Groq**.

The application supports:

- 📄 Question answering from multiple PDF documents
- 🖼️ Image-based question answering
- 🔎 Semantic document retrieval
- 🧠 LLM-powered grounded responses
- 📚 Source document display
- ⚡ Interactive Streamlit interface

---

## 🚀 Features

### 📄 PDF Research Assistant

1. Upload multiple PDF documents.
2. Click **Build Knowledge Base**.
3. PDF text is extracted and divided into chunks.
4. Text chunks are converted into embeddings.
5. Embeddings are stored in ChromaDB.
6. Relevant information is retrieved using semantic search.
7. Groq LLM generates an answer using the retrieved context.
8. Source PDF and page information are displayed.

### 🖼️ Image Q&A

Upload a:

- JPG
- JPEG
- PNG

Ask a question about the image and receive an AI-generated response using a Groq vision-capable model.

---

## 🏗️ System Architecture

### PDF RAG Pipeline

text
PDF Upload
     ↓
PDF Text Extraction
     ↓
Text Chunking
     ↓
Hugging Face Embeddings
     ↓
ChromaDB Vector Store
     ↓
Semantic Retrieval
     ↓
Relevant Context
     ↓
Groq LLM
     ↓
Grounded Answer
     ↓
Source Document

### Image Q&A Pipeline
Image Upload
     ↓
Image Bytes
     ↓
Base64 Encoding
     ↓
Groq Vision Model
     +
User Question
     ↓
AI Answer

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| Python                | Core programming language |
| Streamlit             | Web application           |
| LangChain             | RAG pipeline              |
| PyPDF                 | PDF document loading      |
| Hugging Face          | Text embeddings           |
| Sentence Transformers | Embedding model           |
| ChromaDB              | Vector database           |
| Groq                  | LLM and vision inference  |
| python-dotenv         | Environment variables     |

## ▶️ Run the Application
python -m streamlit run app.py

## RAG_PROJECT/
│
├── app.py
├── config.py
├── rag_pipeline.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── components/
│   ├── __init__.py
│   ├── chat.py
│   └── sources.py
│
├── llm/
│   ├── __init__.py
│   └── llm_client.py
│
├── utils/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── text_splitter.py
│   └── vector_store.py
│
├── data/
│   └── uploads/
│
└── vectorstore/


# Multi-Document-Research-Assistant
