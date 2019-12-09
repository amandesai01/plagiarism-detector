import string

def clean(text):
    return text.translate(str.maketrans('', '', string.punctuation))
    

def filter(text):
    text = text.strip()
    # text = "".join([s for s in text.splitlines(True) if s.strip("\r\n") and s.strip()])
    data = ""
    for s in text.splitlines():
        s = s.strip()
        if s.strip("\r\n"):
            data = data + s + "\n"
    return data
