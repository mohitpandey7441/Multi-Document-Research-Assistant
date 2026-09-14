
import os
import streamlit as st


def show_sources(documents):
    """
    Display unique source PDF files.

    Only one source entry is shown for each PDF,
    using the page number of the first retrieved chunk.
    """

    if not documents:
        return

    st.markdown("---")

    st.subheader("📚 Sources")

    shown_files = set()

    for document in documents:

        source = document.metadata.get(
            "source",
            "Unknown"
        )

        file_name = os.path.basename(source)

        # Skip duplicate PDF files
        if file_name in shown_files:
            continue

        shown_files.add(file_name)

        page = document.metadata.get("page")

        if page is not None:
            st.markdown(
                f"📄 **{file_name}** — Page **{page + 1}**"
            )
        else:
            st.markdown(
                f"📄 **{file_name}**"
            )


