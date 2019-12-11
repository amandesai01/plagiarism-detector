import os
from classifier import classify
from finder import find
from Converter.differ import difference
from Converter.hasher import Manager, HashElement
import json
path = "/Users/aman/Documents/GitHub/plagiarism-detector/Sample_Files"
pathToTemplate = ""
if pathToTemplate == "":
    pathToTemplate = "template.txt"
files = []
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

template = classify(pathToTemplate)
fileSet = {}
fileNameMap = {}
sentenceHashMap = {}

for f in files:
    fileNameMap[f] = HashElement(f)
    fileTextArray = classify(f)
    fileSet[fileNameMap[f]] = (difference(template, fileTextArray))    #stores the text array of the files

for eachfile in fileSet:
    for eachsentence in fileSet[eachfile]:
        sentenceHashMap[HashElement(eachsentence)] = eachsentence

HashedFileSet = {}
for eachfile in fileSet:
    hasharray = []
    for eachsentence in fileSet[eachfile]:
        hasharray.append(HashElement(eachsentence))
    HashedFileSet[eachfile] = hasharray

endResult = {}

for eachfile in HashedFileSet:
    for checkerFile in HashedFileSet:
        if(checkerFile == eachfile):
            continue
        key = eachfile + '+' + checkerFile
        matchedArray = []
        for eachHashedValue in set(HashedFileSet[eachfile]):
            for checkHashValue in set(HashedFileSet[checkerFile]):
                if eachHashedValue == checkHashValue:
                    matchedArray.append(eachHashedValue)
        endResult[key] = matchedArray

print(json.dumps(endResult, indent=4))