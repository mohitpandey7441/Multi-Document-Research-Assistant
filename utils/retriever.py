from config import TOP_K


def get_retriever(vector_store):
    """
    Create a similarity-based retriever.
    """

    retriever = vector_store.as_retriever(
        search_kwargs={
            "k": TOP_K
        }
    )

    return retriever
