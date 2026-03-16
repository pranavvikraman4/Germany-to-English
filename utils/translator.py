from deep_translator import GoogleTranslator

def translate_text(text, target="en"):
    if not text.strip():
        return text

    try:
        return GoogleTranslator(source="auto", target=target).translate(text)
    except:
        return text
