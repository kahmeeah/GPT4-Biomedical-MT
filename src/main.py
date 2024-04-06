#  main
from logging import Logger
import utils.config as config
import utils.api_utils as api 
from gpt_4 import translate_sentence
# from processing import 
# from translation import 
# from evaluation import

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
    for line in data:
        items = line.split('\t')
        doc_ids.append(items[0])
        lines.append(items[1])
        sentence = items[2]
        if model == 'gpt-4':
            translated_sentence = translate_sentence(src, trg, sentence)
        sentences.append(translated_sentence)
    return doc_ids, lines, sentences

def generate_submission(filename, doc_ids, lines, sentences):
    with open(filename, 'w') as f:
        for i in range(len(doc_ids)):
            f.write(f"{doc_ids[i]}\t{lines[i]}\t{sentences[i]}\n")
        
def main():
    data = load_data('../test_files/test.txt')
    #doc_ids, lines, sentences = process_sentences(data, 'portuguese', 'english', 'gpt-4')
    #generate_submission('../test_files/submission.txt', doc_ids, lines, sentences)

if __name__ == "__main__":
    main()
