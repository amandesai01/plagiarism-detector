import Converter

def getTextArray(text):
    text = Converter.cleaner.filter(text)
    textarray = Converter.groupify.group(text)

def process(text):
    textarray = getTextArray(text)
    #template difference
    hash_val = Converter.hasher.hash(textarray)

def classify(name):
    if ".pdf" in name:
       process(Converter.pdf_to_text.grab(name))
    elif ".docx" in name:
        process(Converter.docx_to_text.grab(name))
    elif ".doc" in name:
        process(Converter.docx_to_text.grab(name))
    elif ".txt" in name:
        process(Converter.extractText.grab(name))
