import docxpy
from . import cleaner

def grab(file_path):
    text = docxpy.process(file_path)
    text = cleaner.filter(text)
    return text
