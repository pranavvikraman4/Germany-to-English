import streamlit as st
import tempfile

from streamlit_pdf_viewer import pdf_viewer

from services.pdf_loader import extract_blocks
from services.pdf_translator import translate_blocks
from services.pdf_renderer import render_translated_pdf


st.set_page_config(layout="wide")

st.title("Parallel German → English PDF Reader")

uploaded_pdf = st.file_uploader(
    "Upload German PDF",
    type=["pdf"]
)


if uploaded_pdf:

    temp_input = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    temp_input.write(uploaded_pdf.read())
    temp_input.close()

    st.info("Extracting text blocks...")

    pages = extract_blocks(temp_input.name)

    st.info("Translating content...")

    translated_pages = translate_blocks(pages)

    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    render_translated_pdf(
        temp_input.name,
        translated_pages,
        temp_output.name
    )

    st.success("Translation completed")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("German Original")
        pdf_viewer(temp_input.name, width=700)

    with col2:
        st.subheader("English Translation")
        pdf_viewer(temp_output.name, width=700)
