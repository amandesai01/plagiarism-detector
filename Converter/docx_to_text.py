import docxpy
from Converter.cleaner import filter

def grab(file_path):
    text = docxpy.process(file_path)
    text = filter(text)
    return text
