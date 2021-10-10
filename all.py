import re,json
from collections import Counter


'''get corpus of documents'''
def get_dico():
    textdir = "data/dico/liste.de.mots.francais.frgut.txt"
    try:DICO = open(textdir,'r',encoding="utf-8").read()
    except: DICO = open(textdir,'r').read()
    
    textdir = 'data/corpus/corpus.txt'
    try:CORPUS = open(textdir,'r',encoding="utf-8").read()
    except: CORPUS = open(textdir,'r').read()
    
    #WORDS = Counter(words( 'manger bouger difference update All edits that are one edit away from `word`. The subset of `words` that appear in the dictionary of WORDS '))
    
    return DICO+CORPUS

''' a function to remove diacritics from letters'''
import unicodedata, re, string
def remove_accents(input_str):
    '''
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii
    '''
    """This method removes all diacritic marks from the given string"""
    norm_txt = unicodedata.normalize('NFD', input_str)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)

''' a function to clean sentence and return only words'''
def clean_sentence(texte):
    # Replace diacritics
    texte = remove_accents(texte)
    # Lowercase the document
    texte = texte.lower()
    # Remove Mentions
    texte = re.sub(r'@\w+', '', texte)
    # Remove punctuations
    texte = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', texte)
    # Remove the doubled space
    texte = re.sub(r'\s{2,}', ' ', texte)
    #remove whitespaces at the beginning and the end
    texte = texte.strip()
    
    return texte

'''cleaning and tokenization'''
def tokenize_sentence(texte):
        #clean the sentence 
    texte = clean_sentence(texte)
        #tokenize 
    liste_words = texte.split()
        #return 
    return liste_words
'''
#alternatives
def tokenize_sentence_way2(texte):
    #retourner les groupes d'alphabets
    return re.findall(r'\w+', texte.lower())
def tokenize_sentence_way3(texte):
        #clean the sentence
    blob_object = TextBlob(texte)
        #tokenize
    liste_words = blob_object.words
        #return 
    return liste_words
'''

''' remove apostrophe and get only base form of a word'''
def strip_apostrophe(liste_words):
    get_radical = lambda word: word.split('\'')[-1]
    return list(map(get_radical,liste_words))

''' first text preprocessing. I use methods above get clean words (3 letters minimum) from a sentence'''
def pre_process(sentence):
    #remove '_' from the sentence 
    sentence = sentence.replace('_','')
    
    #get words fro the sentence 
    liste_words = tokenize_sentence(sentence)
    #cut out 1 or 2 letters ones 
    liste_words = [elt for elt in liste_words if len(elt)>2]
    #prendre le radical après l'apostrophe
    liste_words = strip_apostrophe(liste_words)
    print('\nsentence to words : ',liste_words)
    return liste_words






'''words correction in respect of a corpus'''

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)
    
def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def DICO_ET_CORRECTEUR():
    "cette fonction retourne la liste des mots de dictionnaire"
    DICO = get_dico()
    WORDS = Counter(pre_process(DICO)) #Counter prends un str et retourne une sorte de liste enrichie
    "correction des mots "
    N = sum(WORDS.values())
    P = lambda word: WORDS[word] / N #"Probability of `word`."
    correction = lambda word: max(candidates(word), key=P) #"Most probable
    return WORDS,correction

WORDS,CORRECTION = DICO_ET_CORRECTEUR()

'''stopwords'''
with open("data/stop_words/stp_words_.json",'r') as json_file:
    STOPWORDS = json.load(json_file) #une liste
STOPWORDS = list(map(remove_accents,STOPWORDS))


''' get lemmatizer'''
with open("data\\lemma_dico\\sample_.json",'r') as json_file:
    #json_file.seek(0)
    LISTE = json.load(json_file) #un dict cle/val
my_stemmer = lambda word: LISTE[word] if word in LISTE else word


''' Use all fonctionnalities above (preprocessing, correction, stemming) to get correct french words from any french sentence'''
def SENTENCE_TO_CORRECT_WORDS(sentence):
    "cette fonction retourne la liste des mots du user"
    print('\n------------pre_process--------\n')
    liste_words = pre_process(sentence)
    print(liste_words)
    print('\n------------correction--------\n')
    liste_words = list(map(CORRECTION,liste_words))
    print(liste_words)
    print('\n------------stemming--------\n')
    liste_words = list(map(my_stemmer,liste_words))
    print(liste_words)
    print('\n------------remove stp-words--------\n')
    liste_words = [elt for elt in liste_words if elt not in STOPWORDS]
    print(liste_words)
    print('\n-------------------------------------\n')
    return liste_words


''' a test here'''
out = 0 
if __name__ == '__main__':
    print('\n-------------------------------------\n')
    sentence = 'voilà ma phrase'
    print('sentence: ',sentence)
    liste_words = SENTENCE_TO_CORRECT_WORDS(sentence)
    print('liste_words:',liste_words)
    print('\n-------------------------------------\n')
    print('\ndes phrases à mots raté, d\'une faute ou deux, à corriger')
    while out!=2:
        sentence = input('sentence or word: ')
        
        if sentence: 
            #CORRECTION(word.lower())
            liste_words = SENTENCE_TO_CORRECT_WORDS(sentence)
            #print(liste_words)
        else: out +=1
    