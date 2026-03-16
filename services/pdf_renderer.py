import fitz

def render_translated_pdf(original_pdf, translated_pages, output_path):

    doc = fitz.open(original_pdf)
    new_doc = fitz.open()

    for page_index, page in enumerate(doc):

        new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)

        blocks = translated_pages[page_index]

        for block in blocks:

            x0, y0, x1, y1 = block["bbox"]
            text = block["text"]

            rect = fitz.Rect(x0, y0, x1, y1)

            new_page.insert_textbox(rect, text, fontsize=10)

    new_doc.save(output_path)
