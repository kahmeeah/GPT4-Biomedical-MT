import sacrebleu
from sacremoses import MosesDetokenizer
md = MosesDetokenizer(lang='en')

def detokenize(reference_file, translation_file):
    # open files and detokenize
    refs = []
    with open(reference_file) as test:
        for line in test: 
            line = line.strip().split() 
            line = md.detokenize(line) 
            refs.append(line)
    preds = []
    with open(translation_file) as pred:  
        for line in pred: 
            line = line.strip().split() 
            line = md.detokenize(line) 
            preds.append(line)
    return refs, preds

def calculate_bleu_sentence(refs, preds):
     # calculate individual bleu scores for each sentence
     with open("results/bleu.txt", "w+") as output:
        for line in zip(refs,preds):
            test = line[0]
            pred = line[1]
            # print(test, "\t--->\t", pred)
            bleu = sacrebleu.sentence_bleu(pred, [test], smooth_method='exp')
            # print(bleu.score, "\n")
            output.write(str(bleu.score) + "\n")
        print("BLEU Scores for each sentence generated in bleu.txt")    

def calculate_bleu_corpus(refs, preds):
     # calculate bleu score for entire corpus
     refs = [refs] # list of lists, as required by bleu
     bleu = sacrebleu.corpus_bleu(preds, refs)
     print(f"BLEU Score for corpus: {bleu.score}")
     return bleu.score
    




# reference_file = 'test_files/submission_google-translate_pt2en.txt'
# translation_file = 'test_files/submission_deepl_PT2EN-US.txt'

# refs, preds = detokenize(reference_file, translation_file)
# calculate_bleu_corpus(refs, preds)
# calculate_bleu_sentence(refs, preds)
