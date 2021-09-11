# text-preprocessing-methods
It is not obvious to compute all parts of a NLP project in french language. After some research, i've found/created some methods that you could use for your own NLP projects.

# Text pre-processing methods
- clear sentences: using regex
- sentence correction: [correction.py](https://github.com/Hermann-web/text-preprocessing-methods-for-NLP-search-engine/blob/main/correcteur.py)
- tokenization : [summary_token.py](https://github.com/Hermann-web/text-preprocessing-methods-for-NLP-search-engine/blob/main/summary_token.py)
- lemmatization: [summary_lemma.py](https://github.com/Hermann-web/text-preprocessing-methods-for-NLP-search-engine/blob/main/summary_lemma.py)
- find synonyms in french: [syn_french.py](https://github.com/Hermann-web/text-preprocessing-methods-for-NLP-search-engine/blob/main/syn_french.py)

# A preprocessing algorithm
After these benchmark You cand find an [function named SENTENCE_TO_CORRECT_WORDS](https://github.com/Hermann-web/text-preprocessing-methods-for-NLP-search-engine/blob/main/all.py#LC146) in the file [all.py](https://github.com/Hermann-web/text-preprocessing-methods-for-NLP-search-engine/blob/main/all.py) that use these methods to get french tokens from a french sentence.

You can also find my search engine that use preprocessing and semantic similarities [here](https://github.com/Hermann-web/Search-engine-with-python-nlp)

# requirements
You can find them [here](https://github.com/Hermann-web/text-preprocessing-methods-for-NLP-search-engine/blob/main/requirements.txt). In respect of the methods you want to test, you can just install some of them
