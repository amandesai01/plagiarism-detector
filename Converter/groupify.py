from Converter.cleaner import clean
def group(text):
    groups = []
    words = text.split('.')
    count = 0
    message = ""
    for sentence in words:
        if count % 1 == 0:
            count = 0
            groups.append(clean(message))
            message = ""
        message = message + sentence + " "
        count = count +1
    groups.append(clean(message))
    return groups

