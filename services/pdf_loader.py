import fitz

def extract_blocks(pdf_path):

    doc = fitz.open(pdf_path)
    pages = []

    for page in doc:

        blocks = page.get_text("blocks")

        page_blocks = []

        for block in blocks:

            x0, y0, x1, y1, text, *_ = block

            page_blocks.append({
                "bbox": (x0, y0, x1, y1),
                "text": text
            })

        pages.append(page_blocks)

    return pages
