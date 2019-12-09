import Converter
import Separator

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