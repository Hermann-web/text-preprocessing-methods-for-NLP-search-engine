from nltk.tokenize import TreebankWordTokenizer
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn

# ['als', 'arb', 'cat', 'cmn', 'dan', 'eng', 'eus', 'fas',
# 'fin', 'fra', 'fre', 'glg', 'heb', 'ind', 'ita', 'jpn', 'nno',
# 'nob', 'pol', 'por', 'spa', 'tha', 'zsm']
lang='fra'



sent = TreebankWordTokenizer().tokenize("Je voudrai essayer avec cette phrase. Puis, ajouter une phrase; mais aussi pour m'excamer !!!!")
#> ['Je', 'voudrai', 'essayer', 'avec', 'cette', 'phrase.', 'Puis', ',', 'ajouter', 'une', 'phrase', ';', 'mais', 'aussi', 'pour', "m'excamer", '!', '!', '!', '!']


synsets = [lesk(sent, w, 'n') for w in sent]
print(synsets)

for ws in sent:
    for ss in [n for synset in wn.synsets(ws, lang=lang) for n in synset.lemma_names(lang)]:
        print((ws, ss), '\n') 


while 1:
    print('----------------------------------------')
    sentence = input()
    sent = TreebankWordTokenizer().tokenize(input)
    synsets = [lesk(sent, w, 'n') for w in sent]
    print(synsets)

    for ws in sent:
        for ss in [n for synset in wn.synsets(ws, lang=lang) for n in synset.lemma_names(lang)]:
            print((ws, ss), '\n')
    from nltk.tokenize import TreebankWordTokenizer
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn


#documentaion : https://www.nltk.org/howto/wordnet.html
#explication ::https://www.guru99.com/wordnet-nltk.html

###choisir la langue
# ['als', 'arb', 'cat', 'cmn', 'dan', 'eng', 'eus', 'fas',
# 'fin', 'fra', 'fre', 'glg', 'heb', 'ind', 'ita', 'jpn', 'nno',
# 'nob', 'pol', 'por', 'spa', 'tha', 'zsm']
lang='fra'


###casser en liste de mots
sent = TreebankWordTokenizer().tokenize("Je voudrai essayer avec cette phrase") 

###inut
synsets = [lesk(sent, w, 'n') for w in sent]
print(synsets)

###
for word in sent:
    print('word = ', word)
    #un ensemble de synonymes du mot 
    Liste_synsets = wn.synsets(word, lang=lang) 
    # pour chaque synonyme, 
    for synset in Liste_synsets:
        print('  ', synset)
        #on va recuperer ses synonymes du 1e ordre dans le dictionnaire francais (lang='fra')
        for n in synset.lemma_names(lang):
            print('      ' +n)
    print('  ', 'la somme')
    for n in set([ n for synset in Liste_synsets for n in synset.lemma_names(lang) ]):
        print('      ' +n)
    print('\n')
        
'''
for word in sent:  
    print('word = ', word)
    Liste_synsets = wn.synsets(word, lang=lang) 
    for ss in set([n for synset in Liste_synsets for n in synset.lemma_names(lang)]):
        print('    ' +ss, '\n')
    print('\n')
'''


#ce code marche bien. Il trouve les synonymes en francais*


# 