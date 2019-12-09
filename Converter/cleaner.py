from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def clean(text):
    words = word_tokenize(text)
    punct = [',','?','(',')',';',':','[',']','{','}',',']
    common_words = stopwords.words['english']
    words = [word for word in words if word not in common_words and word not in punct]
    text = ' '.join(word for word in words)
    return text

def filter(text):
    text = text.strip()
    # text = "".join([s for s in text.splitlines(True) if s.strip("\r\n") and s.strip()])
    data = ""
    for s in text.splitlines():
        s = s.strip()
        if s.strip("\r\n"):
            data = data + s + "\n"
    return data

