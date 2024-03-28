# Functions to interact with GPT-4, Google Translate, DeepL, and CUBBITT APIs
# Handle input/output formatting for each service
import logging
import os
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger(__name__)  
logger.setLevel(logging.INFO)  

from google.cloud import translate

"""
************ Google Translate API Helper Functions ************

This section contains helper functions for interacting with the Google Translate API.
"""

PROJECT_ID = os.environ.get('PROJECT_ID')
credential_path = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
assert PROJECT_ID
PARENT = f"projects/{PROJECT_ID}"

def test_google_authentication():
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

test_google_authentication()
