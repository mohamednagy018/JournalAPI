from nltk.tokenize import word_tokenize
from nltk.stem import ISRIStemmer
from difflib import SequenceMatcher
import os
from newapp.settings import PROJECT_ROOT

text_nolink = ""
def ArabicStopwords():
    StopwordsFile = open(os.path.join(PROJECT_ROOT, 'stopwords-ar.txt'), encoding='utf-8') #this way to open file in django
    #StopwordsFile = open('stopwords-ar.txt', encoding='utf-8')
    ArabicStopwords = StopwordsFile.read().split('\n')
    return ArabicStopwords

def ArabicStemming(text):
    st=ISRIStemmer()
    stemmedwords=[]
    word=text
    for w in word:
        stemmedwords.append(st.stem(w))
    return stemmedwords
