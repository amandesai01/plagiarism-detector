import os
from classifier import classify
from finder import find
from Converter.differ import difference
from Converter.hasher import Manager, HashElement
import json
import ntpath


path = input("Enter Path to Dir: ")
pathToTemplate = input("Enter path to Template(Leave Blank if no template): ")
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
fileRetrievelMap = {}
for f in files:
    fileNameMap[f] = HashElement(f)
    fileRetrievelMap[fileNameMap[f]] = f
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
checkedStatus = []
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
        if matchedArray:
            endResult[key] = matchedArray
        checkedStatus.append(checkerFile)
print(json.dumps(endResult, indent=4))


for eachval in endResult:
    print("\n\n\n***********************Matched***********************")
    filesMatched = str(eachval).split('+')
    print(ntpath.basename(fileRetrievelMap[filesMatched[0]]) + " <-> " + ntpath.basename(fileRetrievelMap[filesMatched[1]])+"\n\n")
    for eachsentence in endResult[eachval]:
        print( "-> "+ sentenceHashMap[eachsentence])
    print("***********************End***********************\n\n\n")
