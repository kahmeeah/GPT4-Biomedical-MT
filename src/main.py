#  main
from logging import Logger
import utils.config as config
import utils.api_utils as api 
# from processing import 
# from translation import 
# from evaluation import

try:
    api.test_all_auth()
    print("APIs Authenthicated.")
except Exception as e:
    Logger.error("One or more APIs failed: ", e)

    
def load_data(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
    return data

def process_sentences(data):
    sentences = []
    for line in data:
        items = line.split('\t')
        sentence = items[2]


    return sentences

def translate_sentences(sentence):
    pass

def generate_submission(filename):
    with open(filename, 'w') as f:
        f.write("DOC_ID\tSENT_ID\tTRANSLATED_SENTENCE\n")
        for doc_id in range(1, 5):
            for sent_id in range(1, 4):
                f.write(f"doc{doc_id}\t{sent_id}\ttranslated_sentence_{sent_id}\n")
def main():
    data = load_data('../reference_files/medline_en2pt_en.txt')
    sentences = process_sentences(data)


if __name__ == "__main__":
    main()
