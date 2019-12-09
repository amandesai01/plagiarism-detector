def grab(path):
    f = open(path, 'r')
    file_contents = f.read()
    f.close()
    return file_contents