from langchain_core.prompts import (
    ChatPromptTemplate
)

from utils.document_loader import (
    load_documents
)

from utils.text_splitter import (
    split_documents
)

from utils.vector_store import (
    create_vector_store
)

from utils.retriever import (
    get_retriever
)

from llm.llm_client import (
    get_llm
)


# --------------------------------
# RAG PROMPT
# --------------------------------

PROMPT = """
You are a helpful AI research assistant.

Answer the user's question using ONLY the
information provided in the context.

Follow these rules carefully:

1. Do not use outside knowledge.
2. Do not invent information.
3. If the answer cannot be found in the
   provided context, clearly say:

   "I could not find sufficient information
   in the uploaded documents."

4. Give a clear and concise answer.
5. When possible, explain the answer using
   information from the retrieved documents.

Context:
{context}

Question:
{question}

Answer:
"""


def create_rag_pipeline(file_paths):
    """
    Create the complete RAG pipeline.
    """

    # Step 1: Load PDFs
    documents = load_documents(
        file_paths
    )

    if not documents:
        raise ValueError(
            "No valid PDF documents were found."
        )

    # Step 2: Split documents
    chunks = split_documents(
        documents
    )

    if not chunks:
        raise ValueError(
            "No text chunks were created."
        )

    # Step 3: Create vector database
    vector_store = create_vector_store(
        chunks
    )

    # Step 4: Create retriever
    retriever = get_retriever(
        vector_store
    )

    # Step 5: Create LLM
    llm = get_llm()

    return retriever, llm


def ask_question(
    question,
    retriever,
    llm
):
    """
    Retrieve relevant documents and
    generate a grounded answer.
    """

    # Retrieve relevant chunks
    documents = retriever.invoke(
        question
    )

    if not documents:
        return (
            "I could not find sufficient "
            "information in the uploaded documents.",
            []
        )

    # Combine retrieved context
    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    # Create prompt
    prompt = ChatPromptTemplate.from_template(
        PROMPT
    )

    messages = prompt.format_messages(
        context=context,
        question=question
    )

    # Generate answer
    response = llm.invoke(
        messages
    )

    return response.content, documents
