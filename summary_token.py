#https://www.geeksforgeeks.org/python-tokenize-text-using-textblob/ ::tokenization
#https://www.nltk.org/api/nltk.stem.html#module-nltk.stem.regexp: tokenizaton
#https://www.nltk.org/api/nltk.tokenize.html

#
from nltk.stem import RegexpStemmer
#
from textblob import TextBlob
#
import nltk 
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
#
from nltk.tokenize import word_tokenize
#
tokenizer_nltk_fr = nltk.data.load('tokenizers/punkt/french.pickle')
# 
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
# ['als', 'arb', 'cat', 'cmn', 'dan', 'eng', 'eus', 'fas',
# 'fin', 'fra', 'fre', 'glg', 'heb', 'ind', 'ita', 'jpn', 'nno',
# 'nob', 'pol', 'por', 'spa', 'tha', 'zsm']
lang='fra'
######end

def methode(sentence):
    print('sentence = ',sentence)
    
    
    
    print( '\n----------TreebankWordTokenizer for word tokenization--------------')    
    tokens = tokenizer.tokenize(sentence)
    print(" Word Tokenize:\n", tokens) # tokenize paragraph into words.
    ''' Word Tokenize :
     ['les', 'chiens', 'sont', 'tombés', 'Ils', 'mangeaient', 'des', 'repas', 'empoisonnés']
    '''


    print( '\n----------nltk.Tokenizer for word tokenization--------------')
    tokens = word_tokenize(sentence)
    print(" Word Tokenize:\n", tokens) # tokenize paragraph into words.
    ''' Word Tokenize :
     ['les', 'chiens', 'sont', 'tombés', 'Ils', 'mangeaient', 'des', 'repas', 'empoisonnés']
    '''


    print( '\n----------nltk.Tokenizer with french for sentence tokenization--------------')
    print(" Sentence Tokenize:\n", tokenizer_nltk_fr.tokenize(sentence)) # tokenize paragraph into words.
    ''' Word Tokenize :
     ['les chiens sont tombés.', 'Ils', 'mangeaient', 'des', 'repas', 'empoisonnés']
    '''
    

    print( '\n----------textblob with french for word and sentence tokenization--------------')
    blob_object = TextBlob(sentence) # create a TextBlob object
    tokens = blob_object.words
    print(" Word Tokenize:\n", tokens) # tokenize paragraph into words.
    ''' Word Tokenize :
     ['les', 'chiens', 'sont', 'tombés', 'Ils', 'mangeaient', 'des', 'repas', 'empoisonnés']
    '''
    print("\n Sentence Tokenize:\n", blob_object.sentences)# tokenize paragraph into sentences.
    '''
     Sentence Tokenize :
     [Sentence("les chiens sont tombés."), Sentence("Ils mangeaient des repas empoisonnés")]
    '''



sentence = "Jadis, une nuit, je fus un papillon, voltigeant, content de son sort. Puis, je m’éveillai, étant Tchouang-tseu. Qui suis-je en réalité ? Un papillon qui rêve qu’il est Tchouang-tseu ou Tchouang qui s’imagine qu’il fut papillon ?"
sentence = 'les chiens sont tombés. C\'est pas vrai quoi ! En fait, ils mangeaient des repas empoisonnés !!! Message d\'erreur Il existe des factures pour le cas ___ . Création du mouvement impossible. @ ,;:\_-(\"'
methode(sentence)


################## ce qui est retenu 
def my_tokenizer(paragraph,toword=True):
    if not paragraph: 
        print('no input paragraph or sentence !!!')
        return
    blob_object = TextBlob(paragraph)
    
    #si c'est u paragraphe, je casse en liste de phrases
    if not toword:
        tokens_p = blob_object.sentences
        tokens_w = []
        for sentence in tokens_p:
            #passer de ce format à un vrai string 
            sentence = ''.join( [c for c in sentence] )
            #tokenizer le string en liste de mots 
            tokens = my_tokenizer(sentence,toword=True)
            tokens_w.append ( tokens )
        return blob_object.sentences, tokens_w
        
    #si c'est une phrase, je casse en liste de mots
    else:
        return blob_object.words
        
        
def main():
    print('\n exos de tokenization using TextBlob with frecnh for lemmatization--------------')
    just_change=False
    continuer = True
    toword = False
    while continuer:
        if not toword: sentence = input('enter a paragraph to break in sentences: ')
        else: sentence = input('enter a sentence to break in words: ')
        #si il y a un input donc on continue à ajouter le même
        if sentence:
            just_change = False
            if toword:print('\ntokens = \n', my_tokenizer(sentence,toword=True))
            else:
                result = my_tokenizer(sentence,toword=False)
                #break into sentences
                print('\ntokens_p = \n\n')
                #print('tokens_p = ', result[0])
                tokens_p = result[0]
                #print each sentence
                for sentence in tokens_p:
                    print(sentence)
                #break each parph into words
                for token in result[1]: print(token)
        #si il y a pas de input
        else :
            #c'est la secd fois qu'on met un input vide donnc on sort
            if just_change: 
                continuer=False
            #on continue mais on change de format 
            else:
                just_change=True; toword=not toword
main()




