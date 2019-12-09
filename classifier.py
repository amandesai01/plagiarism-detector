import Converter.pdf_to_text
import hasher
import groupify

def classify(name):
    if ".pdf" in name:
       text =  Converter.pdf_to_text.grab(name)
       text = groupify.group(text)
       hash_val = hasher.hash(text)
    elif ".docx" in name:
        Converter.docx_to_text.grab(name)
    elif ".doc" in name:
        Converter.doc_to_text.grab(name)
    elif ".txt" in name:
        Converter.doc_to_text.grab(name)
