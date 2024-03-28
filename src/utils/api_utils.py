# Functions to interact with GPT-4, Google Translate, DeepL, and CUBBITT APIs
# Handle input/output formatting for each service
import logging
import openai
import requests
import os
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger(__name__)  
logger.setLevel(logging.INFO)  

# import MT packages
from google.cloud import translate
import deepl
from openai import OpenAI


"""
API Helper Functions
This section contains helper functions for interacting with the Google Translate, DeepL, and OpenAi API.
"""

# ================= GOOGLE TRANSLATE API =================

PROJECT_ID = os.environ.get('PROJECT_ID')
CREDENTIAL_PATH = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
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

# ================= DEEPL API ================= 

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



# ================= CUBBITT API ================= 

# response = requests.get("https://lindat.mff.cuni.cz/services/translation/api/v2/")
# if response:
#     data = response.json()
#     print("Success!")
# else:
#     raise Exception(f"Non-success status code: {response.status_code}")

# print(data)

# cubbitt_models={
#     "English->French (CUBBITT)":"en-fr",
#     "French->English (CUBBITT)":"fr-en",
# }


# ================= OPENAI API ================= 

OPENAI_MODEL = os.environ.get('OPENAI_MODEL')
client = OpenAI(
    api_key = os.environ.get('OPENAI_KEY')
)

def test_openai_auth():
    try:
        client.models.list()
        logger.info("OpenAI API Authentication Successful")
    except openai.AuthenticationError as e: 
        logger.error("OpenAI API Authentication Failed: %s", e)

test_openai_auth()

