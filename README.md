
# 🤖 Multi-Document Research Assistant using RAG

A **document-grounded AI research assistant** built using **Retrieval-Augmented Generation (RAG)**.

The application allows users to upload multiple PDF documents, build a searchable knowledge base, and ask natural-language questions based on the uploaded documents.

It also includes an **Image Question Answering** mode that allows users to upload JPG, JPEG, or PNG images and ask questions about their visual content.

---

## 🚀 Features

### 📄 PDF Document Q&A

* Multiple PDF upload
* PDF text extraction
* Intelligent text chunking
* Hugging Face embeddings
* ChromaDB vector database
* Semantic similarity search
* Groq LLM integration
* Context-grounded answers
* Source document identification
* Source page information
* Multiple document support

### 🖼️ Image Q&A

* JPG, JPEG, and PNG image upload
* Image preview
* Natural-language questions about images
* Vision-language model integration
* Supports document images, screenshots, diagrams, and visual content
* Direct image analysis without adding images to the PDF vector database

### 💻 User Interface

* Built with Streamlit
* Simple PDF and Image modes
* Interactive question-answering interface
* Clean and user-friendly design

---

# 🧠 RAG Architecture

The PDF workflow follows a standard Retrieval-Augmented Generation architecture:

```text
                PDF Upload
                    │
                    ▼
             PDF Text Extraction
                    │
                    ▼
               Text Chunking
                    │
                    ▼
          Hugging Face Embeddings
                    │
                    ▼
                ChromaDB
                    │
                    ▼
            Semantic Retrieval
                    │
                    ▼
             Relevant Context
                    │
                    ▼
                 Groq LLM
                    │
                    ▼
             Grounded Answer
                    │
                    ▼
              Source Document
```

---

# 🖼️ Image Q&A Architecture

Image questions use a separate multimodal pipeline:

```text
              Image Upload
                    │
                    ▼
              Image Bytes
                    │
                    ▼
             Base64 Encoding
                    │
                    ▼
          Groq Vision Model
                    ▲
                    │
                  Query
                    │
                    ▼
                 Answer
```

The image pipeline does not use the PDF vector database because an uploaded image can be directly processed by a vision-capable model.

---

# 🔄 How the RAG Pipeline Works

## 1. PDF Upload

The user uploads one or more PDF documents through the Streamlit interface.

## 2. PDF Text Extraction

The application uses `PyPDFLoader` to extract text and metadata from the uploaded PDF files.

## 3. Text Chunking

Large documents are divided into smaller chunks using:

```text
RecursiveCharacterTextSplitter
```

Current configuration:

```text
Chunk Size: 800
Chunk Overlap: 150
```

Chunking allows the system to retrieve smaller and more relevant sections of the documents.

## 4. Embedding Generation

Each document chunk is converted into a numerical vector using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

These embeddings represent the semantic meaning of the document chunks.

## 5. Vector Database

The generated embeddings are stored in:

```text
ChromaDB
```

ChromaDB enables efficient similarity-based retrieval.

## 6. Semantic Retrieval

When the user asks a question, the system searches the vector database and retrieves the most relevant document chunks.

The current configuration retrieves:

```text
TOP_K = 5
```

relevant chunks.

## 7. Context-Based Generation

The retrieved chunks are passed to the Groq-hosted LLM along with the user's question.

The prompt instructs the model to answer using the retrieved document context.

## 8. Source Identification

The application displays the source PDF associated with the retrieved information.

---

# 🖼️ How Image Q&A Works

The Image mode follows a different workflow.

The uploaded image is first read as bytes and converted into Base64 format.

The image and user's question are then sent directly to a vision-capable Groq model.

Example questions include:

```text
What is written in this image?

Summarize this document.

Extract the text from this image.

What is the main topic of this diagram?

Explain the information shown in this image.
```

---

# 🛠️ Technologies Used

| Technology            | Purpose                         |
| --------------------- | ------------------------------- |
| Python                | Application development         |
| Streamlit             | Web interface                   |
| LangChain             | RAG pipeline                    |
| PyPDF                 | PDF document loading            |
| Hugging Face          | Text embeddings                 |
| Sentence Transformers | Semantic embeddings             |
| ChromaDB              | Vector database                 |
| Groq                  | LLM and vision inference        |
| python-dotenv         | Environment variable management |

---

# 📁 Project Structure

```text
RAG_PROJECT/
│
├── app.py
├── config.py
├── rag_pipeline.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── data/
│   └── uploads/
│
├── vectorstore/
│
├── utils/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── retriever.py
│
├── llm/
│   ├── __init__.py
│   └── llm_client.py
│
└── components/
    ├── __init__.py
    └── sources.py
```

---

```




```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

## 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_groq_api_key

GROQ_MODEL=openai/gpt-oss-120b

GROQ_VISION_MODEL=qwen/qwen3.6-27b
```

> **Important:** Never upload your `.env` file or API key to GitHub.

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
vectorstore/
*.pyc
```

---

# ▶️ Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your web browser.

---

# 💬 Example PDF Questions

After uploading PDF documents, users can ask questions such as:

```text
What are Python built-in functions?

Explain the main concepts discussed in the document.

Summarize the uploaded document.

What functions are discussed in this PDF?

Explain the difference between the functions mentioned in the document.
```

The system retrieves relevant information from the uploaded documents before generating the answer.

---

# 🖼️ Example Image Questions

Users can upload a document image or other visual content and ask:

```text
What is written in this document?

Extract all readable text.

Summarize this image.

What is the main topic of this document?

Explain the diagram shown in the image.
```

---

# 🎯 Use Cases

The application can be used for:

* 📚 Academic PDF research
* 📄 Research papers
* 📊 Business reports
* 📖 Books and study material
* 💻 Technical documentation
* 🏢 Business documents
* 📝 Document summarization
* 🔎 Knowledge-base question answering
* 🖼️ Document image analysis
* 📑 Visual document understanding

---

# 🧠 Key Concepts Demonstrated

This project demonstrates practical knowledge of:

* Retrieval-Augmented Generation (RAG)
* Large Language Models
* Text embeddings
* Vector databases
* ChromaDB
* Semantic search
* Document chunking
* Information retrieval
* Prompt engineering
* Multimodal AI
* Vision-language models
* API integration
* Streamlit development
* Modular Python architecture
* Environment variable management

---

# 🔐 Grounded Answering

The RAG prompt is designed to make the model use the retrieved document context rather than relying on unrelated external knowledge.

The system instructs the LLM to:

```text
1. Use only the provided context.
2. Do not use outside knowledge.
3. Do not invent information.
4. Clearly state when sufficient information is unavailable.
```

This approach helps reduce unsupported or hallucinated answers.

---

# ⚙️ Configuration

Important settings are maintained in `config.py`.

```python
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
TOP_K = 5
```

The configuration also manages:

* Groq API key
* Groq text model
* Groq vision model
* Hugging Face embedding model
* PDF upload directory
* ChromaDB storage directory

---

# 📌 Project Highlights

### PDF RAG

```text
PDF
 ↓
Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
ChromaDB
 ↓
Retrieval
 ↓
Groq LLM
 ↓
Answer + Source
```

### Image Q&A

```text
Image
 ↓
Base64
 ↓
Groq Vision Model
 ↓
Question Answer
```

---

# 🔮 Future Improvements

Possible future improvements include:

* Hybrid keyword + semantic search
* Reranking retrieved documents
* Similarity score display
* Metadata-based document filtering
* Conversation memory
* Streaming responses
* OCR preprocessing
* PDF page preview
* RAG evaluation metrics
* Hallucination evaluation
* Support for DOCX files
* Support for TXT files
* Support for CSV files
* Advanced citation generation
* Authentication and user management
* Cloud deployment

---

# ⚠️ Limitations

* PDF retrieval primarily depends on extracted text.
* Scanned PDFs may require OCR preprocessing.
* Retrieval quality depends on chunking and embedding quality.
* LLM answers depend on the quality of retrieved context.
* Groq API usage is subject to model and account limits.
* Image analysis depends on the capabilities and limits of the selected vision model.

---

---
