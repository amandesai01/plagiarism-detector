from Converter import pdf_to_text,docx_to_text,txt_to_text
from Separator import process

def classify(name):
    textarray = []
    if ".pdf" in name:
       textarray = process(pdf_to_text.grab(name))
    elif ".docx" in name:
       textarray = process(docx_to_text.grab(name))
    elif ".doc" in name:
       textarray = process(docx_to_text.grab(name))
    elif ".txt" in name:
       textarray = process(txt_to_text.grab(name))
    return textarray
