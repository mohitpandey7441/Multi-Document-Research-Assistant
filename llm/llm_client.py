from langchain_groq import ChatGroq

from config import (
    GROQ_API_KEY,
    GROQ_MODEL
)


def get_llm():
    """
    Create and return the Groq LLM.
    """

    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Add it to the .env file."
        )

    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model=GROQ_MODEL,
        temperature=0
    )

    return llm
