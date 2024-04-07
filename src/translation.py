# Core translation function taking the corpus, source/target languages, and calling appropriate API functions
from utils import api_utils as api
import deepl
from google.cloud import translate

LANGUAGE_CODES = {
        "english": "en",
        "portuguese": "pt",
        "german": "de",
    }


def google_translate(src, trg, sentence):
    client = translate.TranslationServiceClient()

    response = client.translate_text(
        parent=api.PARENT,
        contents=[sentence],
        target_language_code=trg,
        source_language_code=src,
    )

    for translation in response.translations:
        return translation.translated_text
    
def deepl_translate(src, trg, sentence):
    translator = api.translator

    result = translator.translate_text([sentence], source_lang=src, target_lang=trg)
    return result.text
