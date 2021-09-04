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
def create_dico():
    print( 'loading document ------------')
    file = open('OLDlexique.txt','r')
    list = file.readlines()
    
    with open('dico.txt','w') as file2:
        print( 'getting lemma of french words ------------')
        L = {}
        for elt in list:
            tk = get_t(elt)
            if tk: file2.write( tk[0]+'\n' ) 
    
    return L
 
create_dico()