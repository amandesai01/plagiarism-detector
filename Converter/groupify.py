from Converter.cleaner import clean
def group(text):
    groups = []
    words = text.split('.')
    count = 0
    message = ""
    for sentence in words:
        if count % 3 == 0:
            count = 0
            groups.append(message)
            message = ""
        message = message + sentence + " "
        count = count +1
    groups.append(message)
    return groups

# inx = input()
# ls = group(inx)
#
# for x in ls:
#     print(x)
