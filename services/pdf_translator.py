from utils.translator import translate_text

def translate_blocks(pages):

    translated_pages = []

    for page in pages:

        translated_blocks = []

        for block in page:

            translated = translate_text(block["text"], "en")

            translated_blocks.append({
                "bbox": block["bbox"],
                "text": translated
            })

        translated_pages.append(translated_blocks)

    return translated_pages
