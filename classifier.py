from Converter import pdf_to_text,docx_to_text,txt_to_text
import Separator

def classify(name):
    textarray = []
    if ".pdf" in name:
       textarray = Separator.process(pdf_to_text.grab(name))
    elif ".docx" in name:
       textarray = Separator.process(docx_to_text.grab(name))
    elif ".doc" in name:
       textarray =  Separator.process(docx_to_text.grab(name))
    elif ".txt" in name:
       textarray = Separator.process(txt_to_text.grab(name))
    return textarray