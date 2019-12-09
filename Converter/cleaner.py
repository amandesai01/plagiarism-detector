from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def clean(text):
    words = word_tokenize(text)
    punct = [',','?','(',')',';',':','[',']','{','}',',']
    common_words = stopwords.words['english']
    words = [word for word in words if word not in common_words and word not in punct]
    text = ' '.join(word for word in words)
    return text
