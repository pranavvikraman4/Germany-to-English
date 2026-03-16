from utils.translator import translate_text

def translate_blocks(pages):

    translated_pages = []

    for page in pages:

        new_blocks = []

        for block in page:

            translated = translate_text(block["text"])

            new_blocks.append({
                "bbox": block["bbox"],
                "text": translated
            })

        translated_pages.append(new_blocks)

    return translated_pages
