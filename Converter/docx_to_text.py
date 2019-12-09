import docxpy
import cleaner

def grab(file_path):
    text = docxpy.process(file_path)
    text = cleaner.filter(text)
    return text

path = input("> ")
text = grab(path)
print(text)