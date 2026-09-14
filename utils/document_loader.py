import os

from langchain_community.document_loaders import PyPDFLoader


def load_documents(file_paths):
    """
    Load multiple PDF documents.

    Parameters:
        file_paths: List of PDF file paths

    Returns:
        List of LangChain documents
    """

    all_documents = []

    for file_path in file_paths:

        extension = os.path.splitext(
            file_path
        )[1].lower()

        if extension != ".pdf":
            continue

        loader = PyPDFLoader(file_path)

        documents = loader.load()

        all_documents.extend(documents)

    return all_documents
