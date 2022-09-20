import enchant #pip install pyenchant
#import codecs

def spellcheckfile(filepath):
    #d = enchant.DictWithPWL("fr_FR","test.pwl")
    d = enchant.Dict("fr_FR")
    try:
        #f = codecs.open(filepath, "r", "utf-8")
        f = open(filepath, "r")
    except IOError:
        print("Error reading the file, right filepath?")
        return
    textdata = f.read()
    mispelled = []
    words = textdata.split()
    for word in words:
        # if spell check failed and the word is also not in
        # mis-spelled list already, then add the word
        if d.check(word) == False and word not in mispelled:
            mispelled.append(word)
    print('mispelled :',mispelled)
    for mspellword in mispelled:
        #get suggestions
        suggestions=d.suggest(mspellword)
        #make sure we actually got some
        if len(suggestions) > 0:
            # pick the first one
            picksuggestion=suggestions[0]
            print('from',mspellword,'to',picksuggestion)
        else: 
            print('nope: ',mspellword)
        #replace every occurence of the bad word with the suggestion
        #this is almost certainly a bad idea :)
        textdata = textdata.replace(mspellword,picksuggestion)
    try:
        fo=open("spellfixed.txt","w")
    except IOError:
        print("Error writing spellfixed.txt to current directory. Who knows why.")
        return 
    fo.write(textdata.encode("UTF-8"))
    fo.close()
    return

filepath = 'words.txt'
spellcheckfile(filepath)