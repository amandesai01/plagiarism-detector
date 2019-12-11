import os
from classifier import classify
from finder import find
from Converter.differ import difference
from Converter.hasher import Manager
import json
path = input()
pathToTemplate = input()
if pathToTemplate == "":
    pathToTemplate = "template.txt"
files = []
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

template = classify(pathToTemplate)
fileSet = {}
for f in files:
    print(f)
    fileTextArray = classify(f)
    fileSet[f] = (difference(template, fileTextArray))    #stores the text array of the files

print(json.dumps(fileSet, indent=4))

FinalHash = Manager(fileSet)
# for i in FinalHash:
#     filetoWrite = open('HashValues.txt', 'w')
#     # write name
#     # append that name
#     for j in i:
#         filet oWrite.write(str(j) + "\n")
# #     filetoWrite.write("\n")

plagiarism_values = find(FinalHash)




