import re
from collections import Counter




def get_dico():
    #textdir = 'create_dico\dico.txt'
    textdir = "C:\\Users\\SOS\\Favorites\\Desktop\\stages\\found\\project\\envs\\correcEnv\\tests\\create_dico\\liste.de.mots.francais.frgut.txt"
    try:DICO = open(textdir,'r',encoding="utf-8").read()
    except: DICO = open(textdir,'r').read()
    
    textdir = 'C:\\Users\\SOS\\Favorites\\Desktop\\stages\\found\\project\\envs\\correcEnv\\tests\\corpus\\corpus.txt'
    try:CORPUS = open(textdir,'r',encoding="utf-8").read()
    except: CORPUS = open(textdir,'r').read()
    
    #WORDS = Counter(words( 'manger bouger difference update All edits that are one edit away from `word`. The subset of `words` that appear in the dictionary of WORDS '))
    
    return DICO+CORPUS

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

'''
#pas cool car il ya des nombres importants
def tokenize_sentence3(texte):
    #retourner les groupes d'alphabets
    return re.findall(r'\w+', texte.lower())
'''
'''
#inutile ici car sa VA est qu'ik decoupe en phrases
def tokenize_sentence2(texte):
        #clean the sentence
    blob_object = TextBlob(texte)
        #tokenize
    liste_words = blob_object.words
        #return 
    return liste_words
'''
def tokenize_sentence(texte):
        #clean the sentence 
    texte = clean_sentence(texte)
        #tokenize 
    liste_words = texte.split()
        #return 
    return liste_words

def strip_apostrophe(liste_words):
    get_radical = lambda word: word.split('\'')[-1]
    return list(map(get_radical,liste_words))

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

#//https://www.ranks.nl/stopwords/french
#STOPWORDS =['alors', 'au', 'aucun', 'aussi', 'autre', 'avant', 'avec', 'avoir', 'bon', 'car', 'ce', 'cela', 'ces', 'ceux', 'chaque', 'ci', 'comme', 'comment', 'dans', 'des', 'du', 'dedans', 'dehors', 'depuis', 'devrait', 'doit', 'donc', 'dos', 'début', 'elle', 'elles', 'en', 'encore', 'essai', 'est', 'et', 'eu', 'fait', 'faites', 'fois', 'font', 'hors', 'ici', 'il', 'ils', 'je\tjuste', 'la', 'le', 'les', 'leur', 'là', 'ma', 'maintenant', 'mais', 'mes', 'mien', 'moins', 'mon', 'mot', 'même', 'ni', 'nommés', 'notre', 'nous', 'ou', 'où', 'par', 'parce', 'pas', 'peut', 'peu', 'plupart', 'pour', 'pourquoi', 'quand', 'que', 'quel', 'quelle', 'quelles', 'quels', 'qui', 'sa', 'sans', 'ses', 'seulement', 'si', 'sien', 'son', 'sont', 'sous', 'soyez\tsujet', 'sur', 'ta', 'tandis', 'tellement', 'tels', 'tes', 'ton', 'tous', 'tout', 'trop', 'très', 'tu', 'voient', 'vont', 'votre', 'vous', 'vu', 'ça', 'étaient', 'état', 'étions', 'été', 'être']
STOPWORDS = ["a","à","â","abord","afin","ah","ai","aie","ainsi","allaient","allo","allô","allons","après","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","auquel","aura","auront","aussi","autre","autres","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","ayant","b","bah","beaucoup","bien","bigre","boum","bravo","brrr","c","ça","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chaque","cher","chère","chères","chers","chez","chiche","chut","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","delà","depuis","derrière","des","dès","désormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","différent","différente","différentes","différents","dire","divers","diverse","diverses","dix","dix-huit","dixième","dix-neuf","dix-sept","doit","doivent","donc","dont","douze","douzième","dring","du","duquel","durant","e","effet","eh","elle","elle-même","elles","elles-mêmes","en","encore","entre","envers","environ","es","ès","est","et","etant","étaient","étais","était","étant","etc","été","etre","être","eu","euh","eux","eux-mêmes","excepté","f","façon","fais","faisaient","faisant","fait","feront","fi","flac","floc","font","g","gens","h","ha","hé","hein","hélas","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","i","il","ils","importe","j","je","jusqu","jusque","k","l","la","là","laquelle","las","le","lequel","les","lès","lesquelles","lesquels","leur","leurs","longtemps","lorsque","lui","lui-même","m","ma","maint","mais","malgré","me","même","mêmes","merci","mes","mien","mienne","miennes","miens","mille","mince","moi","moi-même","moins","mon","moyennant","n","na","ne","néanmoins","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notre","nôtre","nôtres","nous","nous-mêmes","nul","o","o|","ô","oh","ohé","olé","ollé","on","ont","onze","onzième","ore","ou","où","ouf","ouias","oust","ouste","outre","p","paf","pan","par","parmi","partant","particulier","particulière","particulièrement","pas","passé","pendant","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","plein","plouf","plus","plusieurs","plutôt","pouah","pour","pourquoi","premier","première","premièrement","près","proche","psitt","puisque","q","qu","quand","quant","quanta","quant-à-soi","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelque","quelques","quelqu'un","quels","qui","quiconque","quinze","quoi","quoique","r","revoici","revoilà","rien","s","sa","sacrebleu","sans","sapristi","sauf","se","seize","selon","sept","septième","sera","seront","ses","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","stop","suis","suivant","sur","surtout","t","ta","tac","tant","te","té","tel","telle","tellement","telles","tels","tenant","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutes","treize","trente","très","trois","troisième","troisièmement","trop","tsoin","tsouin","tu","u","un","une","unes","uns","v","va","vais","vas","vé","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vôtre","vôtres","vous","vous-mêmes","vu","w","x","y","z","zut","alors","aucuns","bon","devrait","dos","droite","début","essai","faites","fois","force","haut","ici","juste","maintenant","mine","mot","nommés","nouveaux","parce","parole","personnes","pièce","plupart","seulement","soyez","sujet","tandis","valeur","voie","voient","état","étions"]
STOPWORDS = list(map(remove_accents,STOPWORDS))



import json 
with open("data\\lemma_dico\\sample_.json",'r') as json_file:
    #json_file.seek(0)
    LISTE = json.load(json_file)
my_stemmer = lambda word: LISTE[word] if word in LISTE else word

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
    