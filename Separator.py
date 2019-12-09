from Converter import groupify, cleaner
def process(text):
    text = cleaner.filter(text)
    textarray = groupify.group(text)
    return textarray

# def process(text):
#     textarray = getTextArray(text)
#     #template difference
#     return textarray