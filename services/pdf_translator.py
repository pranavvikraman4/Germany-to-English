from utils.translator import translate_text

def translate_pages(pages):

    translated_pages = []

    for page in pages:

        translated_page_text = translate_text(page["text"])

        translated_pages.append({
            "text": translated_page_text,
            "blocks": page["blocks"],
            "width": page["width"],
            "height": page["height"]
        })

    return translated_pages
