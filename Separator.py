import Converter
def process(text):
    text = Converter.cleaner.filter(text)
    textarray = Converter.groupify.group(text)
    return textarray

# def process(text):
#     textarray = getTextArray(text)
#     #template difference
#     return textarray