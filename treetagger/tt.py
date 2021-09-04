# 6. TREETAGGER LEMMATIZER
import pandas as pd
import treetaggerwrapper as tt

t_tagger = tt.TreeTagger(TAGLANG ='en', TAGDIR ='C:\\Users\\SOS\\Documents\\Docs\Setup\\nlp\\tree-tagger-windows-3.2.3\\TreeTagger')
  
pos_tags = t_tagger.tag_text("the bats saw the cats with best stripes hanging upside down by their feet")
  
original = []
lemmas = []
tags = []
for t in pos_tags:
    original.append(t.split('\t')[0])
    tags.append(t.split('\t')[1])
    lemmas.append(t.split('\t')[-1])
  
Results = pd.DataFrame({'Original': original, 'Lemma': lemmas, 'Tags': tags})
print(Results)
  
