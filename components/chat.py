import streamlit as st


def show_chat(retriever, llm):
    """
    Display the chat interface.
    """

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):
            st.markdown(
                message["content"]
            )

    question = st.chat_input(
        "Ask a question about your documents..."
    )

    if question:

        # User message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        # Import here to avoid unnecessary
        # imports when chat is not used
        from rag_pipeline import ask_question

        # Generate answer
        with st.chat_message("assistant"):

            with st.spinner(
                "🔎 Searching documents..."
            ):

                answer, documents = ask_question(
                    question,
                    retriever,
                    llm
                )

            st.markdown(answer)

            # Save assistant message
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            return documents

    return []
