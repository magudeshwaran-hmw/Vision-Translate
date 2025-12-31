from deep_translator import GoogleTranslator

def translate_text(text, source_lang, target_lang):
    try:
        translator = GoogleTranslator(
            source=source_lang,
            target=target_lang
        )
        return translator.translate(text)
    except Exception as e:
        return f"Error: {e}"
