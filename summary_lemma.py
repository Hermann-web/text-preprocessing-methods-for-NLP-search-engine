#https://www.nltk.org/api/nltk.stem.html#module-nltk.stem.regexp: tokenizaton

def my_display(fct_stem,lang):
    #list of tokenized words
    
    if lang=='fr':words = ['mange','manger','mangeais','sportif','chanteuse', 'chants','danses','sports','sportivement']
    else: words = ['cared','university','fairly','easily','singing','sings','sung','singer','sportingly','cats']
        
    print( 'words = ', words)
    
    #stem's of each word
    stem_words = []
    for w in words:
        x = fct_stem(w)
        stem_words.append(x)
        
    #print stemming results
    print( '\noutput')
    for e1,e2 in zip(words,stem_words):
        print(e1+' ----> '+e2)

def my_tokenizer(paragraph,toword=True):
    '''pour toword=True, cet algorithme prend le texte et retourne une liste de mots en enlevant les stop ( point, point d'exclamation,...)'''
    '''pour toword=False, cet algorithme prend le texte et retourne deux choses 
        - liste de phrases (ils sont d'un type etrange peut être avec des fonctionnalites à voir. Anyway, on peut iterer sur les caractères
        - une liste de listes. Chaque sous-liste correspond à une phrase et est liste de mots en enlevant les stop ( point, point d'exclamation,...)
    '''
    from textblob import TextBlob
    if not paragraph: 
        print('no input paragraph or sentence !!!')
        return
    blob_object = TextBlob(paragraph)

    #si c'est une phrase, je casse en liste de mots
    if toword : return blob_object.words
    
    #si c'est u paragraphe, je casse en liste de phrases
    tokens_p = blob_object.sentences
    tokens_w = []
    for sentence in tokens_p:
        #passer de ce format à un vrai string 
        sentence = ''.join( [c for c in sentence] )
        #tokenizer le string en liste de mots 
        tokens = my_tokenizer(sentence,toword=True)
        tokens_w.append ( tokens )
    return blob_object.sentences, tokens_w

        
        

def display_for_sentence_lemmatization(fct_stem,lang,sentence_to_words_tokenizer=my_tokenizer):
    if lang=='fr':sentence = 'les chiens sont tombés'
    else: sentence = 'the bats saw the cats with stripes hanging upside down by their feet.'

    print( '\nsentence:')
    print(sentence)

    words = sentence_to_words_tokenizer(sentence)
    lemmatized_sentence = " ".join([fct_stem(w) for w in words])


    print( 'output:')
    print(lemmatized_sentence)








#################TEXTBLOB##################
from textblob import TextBlob, Word
def textBlob_word_lemmatizer(my_word):
    return Word(my_word).lemmatize()
def textBlob_sentence_tokenizer(sentence): 
    return TextBlob(sentence).words

def lemma_eng():
    print( '\n\n----------textblob with english for lemmatization --------------')
    
    my_display(fct_stem=textBlob_word_lemmatizer,lang='eng')
    ''' output 
    cared ----> cared
    university ----> university
    fairly ----> fairly
    easily ----> easily
    singing ----> singing
    sings ----> sings
    sung ----> sung
    singer ----> singer
    sportingly ----> sportingly
    cats ----> cat
    '''
    
    display_for_sentence_lemmatization(fct_stem=textBlob_word_lemmatizer,lang='eng',sentence_to_words_tokenizer=textBlob_sentence_tokenizer)
    #> the bat saw the cat with stripe hanging upside down by their foot
    

def lemma_fr():
    print( '\n\n----------textblob with french for lemmatization--------------')
    my_display(fct_stem=textBlob_word_lemmatizer,lang='fr')
    
    '''output
    cared ----> cared
    university ----> university
    fairly ----> fairly
    easily ----> easily
    singing ----> singing
    sings ----> sings
    sung ----> sung
    singer ----> singer
    sportingly ----> sportingly
    cats ----> cat
    '''
    display_for_sentence_lemmatization(fct_stem=textBlob_word_lemmatizer,lang='fr',sentence_to_words_tokenizer=textBlob_sentence_tokenizer)
    #> les chiens sont tombés

    #il ne fait rien pour le francais













#################nltk.stem.snowball.SnowballStemmer##################
#https://www.geeksforgeeks.org/snowball-stemmer-nlp/


import nltk
from nltk.stem.snowball import SnowballStemmer
def snowball_word_lemmatizer_eng(my_word):
    #the stemmer requires a language parameter
    snow_stemmer = SnowballStemmer(language='english')
    return snow_stemmer.stem(my_word)
def snowball_word_lemmatizer_fr(my_word):
    #the stemmer requires a language parameter
    snow_stemmer = SnowballStemmer(language='french')
    return snow_stemmer.stem(my_word)
def lemma_snowball_eng():
    print( '\n\n----------nltk snowball with english for lemmatization+stemming --------------')
    
    my_display(fct_stem=snowball_word_lemmatizer_eng,lang='eng')
    ''' output :::
    cared ----> care
    university ----> univers
    fairly ----> fair
    easily ----> easili
    singing ----> sing
    sings ----> sing
    sung ----> sung
    singer ----> singer
    sportingly ----> sport
    '''

    display_for_sentence_lemmatization(fct_stem=snowball_word_lemmatizer_eng,lang='eng')

    #> the bat saw the cat with stripe hanging upside down by their foot
    
    
    
def lemma_snowball_fr():
    print( '\n\n----------nltk snowball with french for lemmatization+stemming --------------')
   
    my_display(fct_stem=snowball_word_lemmatizer_fr,lang='fr')
        
    
    ''' output :::
    mange ----> mang
    manger ----> mang
    mangeais ----> mang
    sportif ----> sportif
    chanteuse ----> chanteux
    chants ----> chant
    danses ----> dans
    sports ----> sport
    sportivement ----> sportiv
    '''

    display_for_sentence_lemmatization(fct_stem=snowball_word_lemmatizer_fr,lang='fr')
    
    #> le chien sont tomb

 








#################nltk.stem.snowball.FrenchStemmer##################
import nltk   
from nltk.stem.snowball import FrenchStemmer
def snowballFrench_word_lemmatizer(my_word):
    #the stemmer requires a language parameter
    snow_stemmer = FrenchStemmer()
    return snow_stemmer.stem(my_word)
def lemma_french_stemmer():
    print( '\n\n----------nltk french_stemmer with french for lemmatization --------------')
    my_display(fct_stem=snowballFrench_word_lemmatizer,lang='fr')
    ''' output :::
    mange ----> mang
    manger ----> mang
    mangeais ----> mang
    sportif ----> sportif
    chanteuse ----> chanteux
    chants ----> chant
    danses ----> dans
    sports ----> sport
    sportivement ----> sportiv
    '''
    display_for_sentence_lemmatization(fct_stem=snowballFrench_word_lemmatizer,lang='fr')
    #> le chien sont tomb




#################nltk.stem.PorterStemmer##################
from nltk.stem import PorterStemmer
def porter_word_stemmer(my_word):
    #the stemmer requires a language parameter
    porter_stemmer = PorterStemmer()
    return porter_stemmer.stem(my_word)

def lemma_english_porter_stemmer():
    print( '\n\n----------nltk porter_stemmer with english for stemming --------------')
    my_display(fct_stem=porter_word_stemmer,lang='en')
    ''' output :::
    cared ----> care
    university ----> univers
    fairly ----> fairli
    easily ----> easili
    singing ----> sing
    sings ----> sing
    sung ----> sung
    singer ----> singer
    sportingly ----> sportingli
    cats ----> cat
    '''
    display_for_sentence_lemmatization(fct_stem=porter_word_stemmer,lang='en')
    #> le chien sont tomb




#################nltk.stem.WordNetLemmatizer##################
from nltk.stem import WordNetLemmatizer
def  word_net_lemma(my_word):
    #the stemmer requires a language parameter
    lem = WordNetLemmatizer()
    return lem.lemmatize(my_word)

def lemma_english_wordnet_lemmatizer():
    print( '\n\n----------nltk WordNetLemmatizer with english for lemmatization --------------')
    my_display(fct_stem=word_net_lemma,lang='en')
    ''' output :::
    cared ----> care
    university ----> univers
    fairly ----> fairli
    easily ----> easili
    singing ----> sing
    sings ----> sing
    sung ----> sung
    singer ----> singer
    sportingly ----> sportingli
    cats ----> cat
    '''
    display_for_sentence_lemmatization(fct_stem=word_net_lemma,lang='en')
    #> le chien sont tomb



    

######################REGEX STEMMER
#https://www.nltk.org/api/nltk.stem.html#module-nltk.stem.regexp: tokenizaton
from nltk.stem import RegexpStemmer
st = RegexpStemmer('es$|s$|ent$|ais$|ment$', min=4)
regex_word_lemmatizer = st.stem
def lemma_using_regex():
    print( '\n\n----------custom nltk stemmer with regex --------------')
    my_display(fct_stem=regex_word_lemmatizer,lang='fr')
    ''' output :::
    mange ----> mang
    manger ----> manger
    mangeais ----> mangeai
    sportif ----> sportif
    chanteuse ----> chanteus
    chants ----> chant
    danses ----> danse
    sports ----> sport
    sportivement ----> sportivement
    '''
    display_for_sentence_lemmatization(fct_stem=regex_word_lemmatizer,lang='fr')
    #> les chien sont tombé







######################utiliser un json qui enumere
#https://perso.limsi.fr/anne/OLDlexique.txt
#list of tokenized words
import json 
with open("data\\lemma_dico\\sample.json",'r') as json_file:
    #json_file.seek(0)
    LISTE = json.load(json_file)
    #LISTE = [json.loads(_.replace('}]}"},', '}]}"}')) for _ in json_file.readlines()]
my_stemmer = lambda word: LISTE[word] if word in LISTE else word
def lemma_from_json():
    print( '\n\n----------my_lemmatizer with french for lemmatization using enumeration--------------')     
    my_display(fct_stem=my_stemmer,lang='fr')          
    ''' output :::
    mange ----> manger
    manger ----> manger
    mangeais ----> manger
    sportif ----> sportif
    chanteuse ----> chanteur
    chants ----> chant
    danses ----> danser
    sports ----> sport
    sportivement ----> sportivement
    '''
    display_for_sentence_lemmatization(fct_stem=my_stemmer,lang='fr')
    #> le chien sont tomber





#numpy-1.9.1%2Bmkl-cp34-none-win_amd64.whl
#numpy-1.9.1%2Bmkl-cp34-none-win32.whl

##############synthese####################

    ##textblob
lemma_eng()              #(stemming)bad (rate souvent)
lemma_fr()               #(stemming)pire que bad : il fait rien 
    ##nltk.stem.snowball.SnowballStemmer(eng)
lemma_snowball_eng()     #(stemming)very good in eng but but i want it french
    ##nltk.stem.snowball.SnowballStemmer(fr)
lemma_snowball_fr()      #(stemming)bad 
    ##nltk.stem.snowball.FrenchStemmer
lemma_french_stemmer()   #(stemming)good 
    ##nltk.stem.RegexpStemmer (customisable)
lemma_using_regex()      #(stemming)il doit avoir de plus puissant filtre sinon bad 
    ##nltk.stem.PorterStemmer
# lemma_french_porter_stemmer() #on sent qu'il est adapté à l'anglais plutôt
lemma_english_porter_stemmer() #plutôt bon sur l'englais
    ##nltk.stem.WordNetLemmatizer
lemma_english_wordnet_lemmatizer() #moyen sur l'englais: il rate des "..ed" et consort
    ##dico
lemma_from_json()        #(lemmatizer)very good (in french) !!


#############################################

#d'autres 
#https://www.geeksforgeeks.org/python-lemmatization-approaches-with-examples/
#pos tag in french #https://stackoverflow.com/questions/42058396/python-nltk-and-textblob-in-french

print('\n exos sur lemmatization with the last one--------------')
my_stemmer = lambda word: LISTE[word] if word in LISTE else word
word = True 
while word:
    word = input('enter a word: ')
    print('lemma = ', my_stemmer(word))