import unicodedata, re, string, os
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


TXTFILES = ['corpus.txt','liste.de.mots.francais.frgut.txt','sample.json',]
TXTFILES2=[]
for txtfile in TXTFILES:
    done = False
    try:
        with open(txtfile,'r') as f:
                texte = f.read()
                done = True 
    except:  done = False
    if not done:
        try:
            with open(txtfile,'r',encoding='utf-8') as f:
                    texte = f.read()
                    done = True
        except: done = False
    if not done:
        try:
            with open(txtfile,'r',encoding='ansi') as f:
                    texte = f.read()
                    done = True
        except:  done = False    
    if done:
        f_name, f_ext = os.path.splitext(txtfile)
        new_name = f_name+'_'+f_ext
        TXTFILES2.append(new_name)
        with open(new_name,'w') as f:
                f.write(remove_accents(texte))

    else:
        print(txtfile,'non traité')
        
        
for txtfile in TXTFILES2:
    done = False
    try:
        with open(txtfile,'r') as f:
                texte = f.read()
                done = True 
    except:  done = False

    if not done:
        print(txtfile,'non ouvert')





