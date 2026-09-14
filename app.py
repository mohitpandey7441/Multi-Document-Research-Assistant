import os
import shutil
import base64

import streamlit as st
from groq import Groq

from config import (
    UPLOAD_DIR,
    VECTOR_DB_PATH,
    GROQ_API_KEY,
    GROQ_VISION_MODEL
)

from rag_pipeline import (
    create_rag_pipeline,
    ask_question
)

from components.sources import (
    show_sources
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Multi-Document Research Assistant",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# CREATE DIRECTORIES
# --------------------------------------------------

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

os.makedirs(
    VECTOR_DB_PATH,
    exist_ok=True
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title(
    "🤖 Multi-Document Research Assistant"
)

st.write(
    "Upload documents or images and ask questions using AI."
)


# --------------------------------------------------
# INPUT TYPE
# --------------------------------------------------

input_type = st.radio(
    "Select input type:",
    ["📄 PDF Documents", "🖼️ Images"],
    horizontal=True
)


# ==================================================
# PDF MODE
# ==================================================

if input_type == "📄 PDF Documents":

    st.subheader("📄 Upload PDF Documents")

    uploaded_files = st.file_uploader(
        "Upload one or more PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        st.write(
            f"**{len(uploaded_files)} PDF document(s) selected.**"
        )

        if st.button(
            "🔨 Build Knowledge Base",
            type="primary"
        ):

            try:

                with st.spinner(
                    "📖 Processing PDF documents..."
                ):

                    # Clear old uploads
                    if os.path.exists(UPLOAD_DIR):

                        for file_name in os.listdir(
                            UPLOAD_DIR
                        ):

                            file_path = os.path.join(
                                UPLOAD_DIR,
                                file_name
                            )

                            if os.path.isfile(
                                file_path
                            ):
                                os.remove(
                                    file_path
                                )

                    # Clear old vector database
                    if os.path.exists(
                        VECTOR_DB_PATH
                    ):

                        shutil.rmtree(
                            VECTOR_DB_PATH
                        )

                    os.makedirs(
                        VECTOR_DB_PATH,
                        exist_ok=True
                    )

                    file_paths = []

                    # Save uploaded PDFs
                    for uploaded_file in uploaded_files:

                        file_path = os.path.join(
                            UPLOAD_DIR,
                            uploaded_file.name
                        )

                        with open(
                            file_path,
                            "wb"
                        ) as output_file:

                            output_file.write(
                                uploaded_file.getbuffer()
                            )

                        file_paths.append(
                            file_path
                        )

                    # Create RAG pipeline
                    retriever, llm = (
                        create_rag_pipeline(
                            file_paths
                        )
                    )

                    st.session_state.retriever = (
                        retriever
                    )

                    st.session_state.llm = llm

                    st.session_state.documents_ready = True

                    st.session_state.messages = []

                st.success(
                    "✅ Knowledge base created successfully!"
                )

            except Exception as e:

                st.error(
                    f"❌ Error while building knowledge base: {e}"
                )


    # --------------------------------------------------
    # PDF CHAT
    # --------------------------------------------------

    if (
        "retriever" in st.session_state
        and st.session_state.retriever
    ):

        st.markdown("---")

        st.subheader(
            "💬 Ask Questions About Your PDFs"
        )

        if "pdf_messages" not in st.session_state:

            st.session_state.pdf_messages = []

        for message in st.session_state.pdf_messages:

            with st.chat_message(
                message["role"]
            ):

                st.markdown(
                    message["content"]
                )

        question = st.chat_input(
            "Ask something about your PDFs..."
        )

        if question:

            st.session_state.pdf_messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            with st.chat_message("user"):

                st.markdown(question)

            with st.chat_message("assistant"):

                with st.spinner(
                    "🔎 Searching your documents..."
                ):

                    answer, documents = ask_question(
                        question,
                        st.session_state.retriever,
                        st.session_state.llm
                    )

                st.markdown(answer)

                st.session_state.pdf_messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

                show_sources(
                    documents
                )


# ==================================================
# IMAGE MODE
# ==================================================

else:

    st.subheader("🖼️ Upload an Image")

    uploaded_image = st.file_uploader(
        "Upload JPG, JPEG or PNG",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=False
    )

    if uploaded_image:

        # --------------------------------------------------
        # DISPLAY IMAGE
        # --------------------------------------------------

        st.image(
            uploaded_image,
            caption="Uploaded Image",
            use_container_width=True
        )

        st.markdown("---")

        st.subheader(
            "💬 Ask About This Image"
        )

        question = st.text_input(
            "Ask a question about the image:",
            placeholder="What is written in this image?"
        )

        if st.button(
            "🔍 Ask Question",
            type="primary"
        ):

            if not question.strip():

                st.warning(
                    "Please enter a question."
                )

            elif not GROQ_API_KEY:

                st.error(
                    "GROQ_API_KEY is missing in your .env file."
                )

            else:

                try:

                    with st.spinner(
                        "🤖 Analyzing image..."
                    ):

                        # Read image bytes
                        image_bytes = (
                            uploaded_image.getvalue()
                        )

                        # Convert image to Base64
                        image_base64 = base64.b64encode(
                            image_bytes
                        ).decode(
                            "utf-8"
                        )

                        # Get MIME type
                        mime_type = (
                            uploaded_image.type
                        )

                        # Create Groq client
                        client = Groq(
                            api_key=GROQ_API_KEY
                        )

                        response = client.chat.completions.create(
                            model=GROQ_VISION_MODEL,
                            messages=[
                                {
                                    "role": "user",
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": question
                                        },
                                        {
                                            "type": "image_url",
                                            "image_url": {
                                                "url": (
                                                    f"data:{mime_type};base64,"
                                                    f"{image_base64}"
                                                )
                                            }
                                        }
                                    ]
                                }
                            ],
                            temperature=0,
                            max_tokens=800
                        )

                        answer = (
                            response.choices[0]
                            .message.content
                        )

                    st.success(
                        "✅ Answer"
                    )

                    st.write(
                        answer
                    )

                except Exception as e:

                    st.error(
                        f"❌ Error analyzing image: {e}"
                    )
