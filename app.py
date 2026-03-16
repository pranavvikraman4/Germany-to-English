import streamlit as st
import base64
import tempfile

from services.pdf_loader import extract_blocks
from services.pdf_translator import translate_blocks
from services.pdf_renderer import render_translated_pdf


st.set_page_config(layout="wide")

st.title("Parallel German → English PDF Reader")


uploaded_pdf = st.file_uploader("Upload German PDF", type=["pdf"])

if uploaded_pdf:

    temp_input = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    temp_input.write(uploaded_pdf.read())
    temp_input.close()

    st.info("Extracting text blocks...")

    pages, page_count = extract_blocks(temp_input.name)

    st.info("Translating content...")

    translated_pages = translate_blocks(pages)

    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    render_translated_pdf(temp_input.name, translated_pages, temp_output.name)

    st.success("Translation completed")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("German Original")

        with open(temp_input.name, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")

        pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}"
        width="100%" height="900" type="application/pdf"></iframe>
        """

        st.markdown(pdf_display, unsafe_allow_html=True)

    with col2:
        st.subheader("English Translation")

        with open(temp_output.name, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")

        pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}"
        width="100%" height="900" type="application/pdf"></iframe>
        """

        st.markdown(pdf_display, unsafe_allow_html=True)
