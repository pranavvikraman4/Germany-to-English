import streamlit as st
import tempfile
import fitz
from deep_translator import GoogleTranslator
from streamlit_pdf_viewer import pdf_viewer


st.set_page_config(layout="wide")

st.title("Parallel German → English PDF Reader")


uploaded_pdf = st.file_uploader(
    "Upload German PDF",
    type=["pdf"]
)


def translate_text(text):

    if not text.strip():
        return text

    try:
        translator = GoogleTranslator(source="auto", target="en")
        return translator.translate(text)
    except:
        return text


def extract_pages(pdf_path):

    doc = fitz.open(pdf_path)

    pages = []

    for page in doc:

        text = page.get_text()

        pages.append({
            "text": text,
            "width": page.rect.width,
            "height": page.rect.height
        })

    return pages


def translate_pages(pages):

    translated = []

    for page in pages:

        translated_text = translate_text(page["text"])

        translated.append({
            "text": translated_text,
            "width": page["width"],
            "height": page["height"]
        })

    return translated


def build_translated_pdf(pages, output_file):

    new_doc = fitz.open()

    for page in pages:

        new_page = new_doc.new_page(
            width=page["width"],
            height=page["height"]
        )

        rect = fitz.Rect(
            40,
            40,
            page["width"] - 40,
            page["height"] - 40
        )

        new_page.insert_textbox(
            rect,
            page["text"],
            fontsize=11
        )

    new_doc.save(output_file)


if uploaded_pdf:

    input_temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    input_temp.write(uploaded_pdf.read())
    input_temp.close()

    st.info("Extracting pages...")

    pages = extract_pages(input_temp.name)

    # LIMIT PAGES FOR SPEED
    MAX_PAGES = 10
    pages = pages[:MAX_PAGES]

    st.info("Translating pages...")

    translated_pages = translate_pages(pages)

    output_temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    build_translated_pdf(
        translated_pages,
        output_temp.name
    )

    st.success("Translation completed")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("German Original")
        pdf_viewer(input_temp.name, width=700)

    with col2:
        st.subheader("English Translation")
        pdf_viewer(output_temp.name, width=700)
