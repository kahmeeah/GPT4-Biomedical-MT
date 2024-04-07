#  main
import os
from logging import Logger
from tqdm.auto import tqdm
import utils.api_utils as api 
from translation import google_translate, deepl_translate, gpt4_translate

try:
    api.test_all_auth()
    print("APIs Authenthicated.")
except Exception as e:
    Logger.error("One or more APIs failed: ", e)

    
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
    return data

def process_sentences(data, src, trg, model):
    sentences = []
    doc_ids = []
    lines = []
    with tqdm(total=len(lines), desc="\033[92mTranslating sentences\033[0m") as pbar:  # Progress bar for sentences
        for line in data:
            items = line.split('\t')
            doc_ids.append(items[0])
            lines.append(items[1])
            sentence = items[2]
            if model == 'gpt-4':
                translated_sentence = gpt4_translate(src, trg, sentence)
            elif model == 'google-translate':
                translated_sentence = google_translate(src, trg, sentence)
            elif model == 'deepl':
                translated_sentence = deepl_translate(src, trg, sentence)
            sentences.append(translated_sentence)
            pbar.update(1)
    return doc_ids, lines, sentences

def generate_submission(filename, doc_ids, lines, sentences):
    with open(filename, 'w') as f:
        for i in range(len(doc_ids)):
            f.write(f"{doc_ids[i]}\t{lines[i]}\t{sentences[i]}\n")

def get_input():

    LANGUAGE_CODES = {
        "english":"en",
        "portuguese":"pt",
        "german":"de",
    }
    TRANSLATION_MODELS = ["gpt-4", "google-translate", "deepl"]
    trg = 'english' # default is english

    file_name = input("Enter file name. Ensure it is placed under the \"test_files/\" directory.\n> ")

    model = input("Choose translation model: \ngpt-4\t\tgoogle-translate\t\tdeepl\n> ").lower()
    if model not in TRANSLATION_MODELS:
        raise ValueError("Invalid translation model")

    src = input("Choose source language: \nportuguese\t\tgerman\n> ").lower()
    if src not in LANGUAGE_CODES:
        raise ValueError("Invalid source language.")
    
    # handle differing language codes 
    if model == "deepl":
        src = LANGUAGE_CODES.get(src).upper() 
        trg = LANGUAGE_CODES.get(trg).upper() + '-US' 
    elif model == "google-translate":
        src = LANGUAGE_CODES.get(src)
        trg = LANGUAGE_CODES.get(trg)
    
    return file_name, model, src, trg 
        
def main():

    # test_files/medline_pt2en_pt.txt

    file_name, model, src, trg = get_input()
 
    data = load_data(os.path.join('test_files', file_name))

    doc_ids, lines, sentences = process_sentences(data, src, trg, model)

    output_filename = f"submission_{model}_{src}2{trg}.txt"
    generate_submission(os.path.join('test_files', output_filename), doc_ids, lines, sentences)

    print(f"Submission file generated: {output_filename}") 
    

if __name__ == "__main__":
    main()
