from utils.api_utils import client
import os
from openai import OpenAI


import os

def generate_text(prompt):
    try:
        message = {
            'role': 'user',
            'content': prompt
        }
        model_name = os.environ.get('OPENAI_MODEL')
        response = client.chat.completions.create(model=model_name, messages=[message])
        #print(response)
        return response.choices[0].message.content
    except Exception as e:
        print("Error:", e)


def generate_prompt(src, trg, sentence):
    return f"You are a helpful assistant specialized in biomedical translation. " \
           f"You will be provided with a sentence in {src}, and your task is to translate " \
           f"it into {trg}. Here is the sentence to translate " \
           f"(give me nothing else other than the translated sentence): {sentence}"

def translate_sentence(src, trg, sentence):
    prompt = generate_prompt(src, trg, sentence)
    generated_text = generate_text(prompt)
    return generated_text



