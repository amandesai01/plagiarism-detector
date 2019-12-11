import os
import classifier,finder
from Converter import differ, hasher

path = input()
pathToTemplate = input()
files = []
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

template = classifier.classify(pathToTemplate)
fileSet = []
for f in files:
    print(f)
    fileTextArray = classifier.classify(f)
    fileSet.append(differ.difference(template, file))    #stores the text array of the files

FinalHash = hasher.Manager(fileSet)
# for i in FinalHash:
#     filetoWrite = open('HashValues.txt', 'w')
#     # write name
#     # append that name
#     for j in i:
#         filet oWrite.write(str(j) + "\n")
#     filetoWrite.write("\n")

plagiarism_values = finder.find(FinalHash)


for file_list in plagiarism_values:
    for perc in file_list:
        print(perc)

