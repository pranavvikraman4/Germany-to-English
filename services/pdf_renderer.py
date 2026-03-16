import fitz

def render_translated_pdf(original_pdf, translated_pages, output_pdf):

    original = fitz.open(original_pdf)
    new_doc = fitz.open()

    for page_index, page in enumerate(original):

        new_page = new_doc.new_page(
            width=page.rect.width,
            height=page.rect.height
        )

        for block in translated_pages[page_index]:

            x0, y0, x1, y1 = block["bbox"]

            rect = fitz.Rect(x0, y0, x1, y1)

            new_page.insert_textbox(
                rect,
                block["text"],
                fontsize=10
            )

    new_doc.save(output_pdf)
