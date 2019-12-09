import os
import classifier
import Converter

path = input()
pathToTemplate = input()
files = []
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

template = classifier.classify()
fileSet = []
for f in files:
    fileTextArray = classifier.classify(f)
    fileSet.append(Converter.differ.difference(template, file))

FinalHash = Converter.hasher.Manager(fileSet)