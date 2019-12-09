import Converter.pdf_to_text
def classify(name):
    if ".pdf" in name:
       Converter.pdf_to_text.grab(name)
    elif ".docx" in name:
        Converter.docx_to_text.grab(name)
    elif ".doc" in name:
        Converter.doc_to_text.grab(name)
    elif ".txt" in name:
        Converter.doc_to_text.grab(name)  
