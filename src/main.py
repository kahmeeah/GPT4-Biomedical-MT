#  main
import os
from logging import Logger
from tqdm.auto import tqdm
import utils.api_utils as api 
from translation import google_translate, deepl_translate, gpt4_translate
from evaluation import * 

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

def generate_prediction_file(filename, doc_ids, lines, sentences):
    with open(filename, 'w') as f:
        for i in range(len(doc_ids)):
            f.write(f"{doc_ids[i]}\t{lines[i]}\t{sentences[i]}\n")

def handle_translation():
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

    data = load_data(os.path.join('test_files', file_name))

    doc_ids, lines, sentences = process_sentences(data, src, trg, model)

    output_filename = f"prediction_{model}_{src}2{trg}.txt" #TODO: generate results folder and put this in there
    generate_prediction_file(os.path.join('results/prediction_files', output_filename), doc_ids, lines, sentences)

    print(f"Prediction file generated: {output_filename}") 

def handle_evaluation():
    # TODO: verify filename exists
    reference_file = input("Enter the name of your reference file. Ensure it is placed under the \"reference_files/\" directory.\n> ")

    prediction_file = input("Enter the name of your prediction file. Ensure it is placed under the \"prediction_files/\" directory.\n> ")

    refs, preds = detokenize(os.path.join('results/prediction_files', reference_file), os.path.join('results/prediction_files', prediction_file)) #TODO: add ref files and refactor accordingly

    calculate_bleu_corpus(refs, preds)
    calculate_bleu_sentence(refs, preds)

    print(f"Evaluation complete.") 
        
def main():

    # test_files/medline_pt2en_pt.txt
    # prediction_deepl_PT2EN-US.txt
    # prediction_google-translate_pt2en.txt

    task = input("Choose a task:\ntranslate\t\tevaluate\n> ")
    if task == "translate":
        handle_translation()
    elif task == "evaluate":
        handle_evaluation()
    else:
        raise ValueError("Enter valid task name.")
    

if __name__ == "__main__":
    main()
