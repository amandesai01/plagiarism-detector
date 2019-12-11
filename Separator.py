from Converter.cleaner import filter
from Converter.groupify import group

def process(text):
    text = filter(text)
    textarray = group(text)
    return textarray

# def process(text):
#     textarray = getTextArray(text)
#     #template difference
#     return textarray
