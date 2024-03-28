# Functions to interact with GPT-4, Google Translate, DeepL, and CUBBITT APIs
# Handle input/output formatting for each service
import logging
import os
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger(__name__)  
logger.setLevel(logging.INFO)  

# import MT packages
from google.cloud import translate
import deepl

"""
************ Google Translate API Helper Functions ************

This section contains helper functions for interacting with the Google Translate API.
"""

PROJECT_ID = os.environ.get('PROJECT_ID')
CREDENTIAL_PATH = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
assert PROJECT_ID
PARENT = f"projects/{PROJECT_ID}"

def test_google_auth():
    try:
        # Perform a simple translation task to trigger authentication
        client = translate.TranslationServiceClient()
        response = client.translate_text(
            parent=PARENT,
            contents="Hello",
            target_language_code="es",
        )

        logger.info("Google Translate API authentication successful.")

    except Exception as e:  
        logger.error("Google Translate API authentication failed: %s", e)

test_google_auth()

"""
************ DeepL API Helper Functions ************

This section contains helper functions for interacting with the DeepL API.
"""
DEEPL_AUTH_KEY = os.environ['DEEPL_AUTH_KEY']
assert DEEPL_AUTH_KEY
translator = deepl.Translator(DEEPL_AUTH_KEY)

def test_deepl_auth():
    try:
        result = translator.translate_text("Hello, world!", target_lang="FR")
        logger.info("DeepL API authentication successful.")  # "Bonjour, le monde !"

    except Exception as e:
        logger.error("DeepL API authentication failed: %s", e)

test_deepl_auth()