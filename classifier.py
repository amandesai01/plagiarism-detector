import Converter
<<<<<<< HEAD
import Separator
=======

def getTextArray(text):
    text = Converter.cleaner.filter(text)
    text = Converter.differ.difference(text)
    textarray = Converter.groupify.group(text)

def process(text):
    textarray = getTextArray(text)
    hash_val = Converter.hasher.hash(textarray)
>>>>>>> 84229b277b4ee550dddf295e02246f92cf622442

def classify(name):
    textarray = []
    if ".pdf" in name:
       textarray = Separator.process(Converter.pdf_to_text.grab(name))
    elif ".docx" in name:
       textarray = Separator.process(Converter.docx_to_text.grab(name))
    elif ".doc" in name:
       textarray =  Separator.process(Converter.docx_to_text.grab(name))
    elif ".txt" in name:
       textarray = Separator.process(Converter.extractText.grab(name))
    return textarray