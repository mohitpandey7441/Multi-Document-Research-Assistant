from langchain_chroma import Chroma

from config import VECTOR_DB_PATH

from utils.embeddings import (
    get_embeddings
)


def create_vector_store(chunks):
    """
    Create a Chroma vector database
    from document chunks.
    """

    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    return vector_store
