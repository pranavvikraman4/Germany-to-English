import fitz

def render_translated_pdf(pages, output_pdf):

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

    new_doc.save(output_pdf)
