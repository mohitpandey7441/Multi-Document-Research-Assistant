import os

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-120b"
)

GROQ_VISION_MODEL = os.getenv(
    "GROQ_VISION_MODEL",
    "qwen/qwen3.6-27b"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
TOP_K = 5

UPLOAD_DIR = os.path.join(
    "data",
    "uploads"
)

VECTOR_DB_PATH = os.path.join(
    "vectorstore"
)
