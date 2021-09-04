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

def get_t(str):
    if not str: return 
    if len(str)<=6: return
    #get word 
    word = ''
    for i in range( len(str)):
        if str[i]=='\t': 
            word = str[0:i]
            pos_fin=i 
            break
    if not word: return
    #get a deb 
    deb = word[0:2]
    #search lemma
    lemma = ''
    for i in range(pos_fin, len(str)):
        if str[i:i+2]==deb:
            for j in range(i, len(str)):
                if str[j]=='\t': 
                    lemma = str[i:j]
                    break
            break
    if not lemma: return 
    return [word, lemma]

def load_doc(removeAccent=False):
    print( 'loading document ------------')
    file = open('input.txt','r')
    list = file.readlines()
    
    print( 'len = ',len(list))

    #print([list[i] for i in range(200,600)])
    
    print( 'getting lemma of french words ------------')
    L = {}
    for elt in list:
        tk = get_t(elt)
        if tk and removeAccent: L[ remove_accents(tk[0]) ] = remove_accents(tk[1] )
        elif tk and not removeAccent: L[ tk[0] ] = tk[1]
    
    return L




LISTE = load_doc()



dictionary = LISTE

print( 'len = ',len(dictionary))

#un test
print('--------------------some examples out of {} ones-------------------- '.format(len(dictionary)))
deb=100;fin=200000;pace=5000
stp =fin
for a,b in LISTE.items():
    stp-=1
    if stp%pace==0: print(a,'--->',b)
    if stp ==deb: break
    

# Serializing json   
import json


''' #voir le json
json_object = json.dumps(dictionary, indent = 4,ensure_ascii=False)  
print(json_object) 
'''

#exporter

with open("sample.json", "w") as outfile: 
    print("\ncreating json file-----------")
    json.dump(dictionary, outfile, ensure_ascii=False,indent=4)
    print("\njson created in that directory")


'''
accéder au json 

def get_file():
    import json 
    with open("sample_.json",'r') as json_file:
        #json_file.seek(0)
        LISTE = json.load(json_file)
    print('les 5 premiers elements')
    print([elt for elt in LISTE.keys()][:5])
def get_file2():
    import json 
    with open("sample.json",'r') as json_file:
        #json_file.seek(0)
        LISTE = json.load(json_file)
    print('les 5 premiers elements')
    print([elt for elt in LISTE.keys()][:5])
'''
    