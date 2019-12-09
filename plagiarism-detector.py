import os
import classifier
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
    fileSet.append(differ.difference(template, file))

FinalHash = hasher.Manager(fileSet)
# for i in FinalHash:
#     filetoWrite = open('HashValues.txt', 'w')
#     # write name
#     # append that name
#     for j in i:
#         filetoWrite.write(str(j) + "\n")
#     filetoWrite.write("\n")

plagiarism_values=[]
for hash_text in FinalHash:
    match = 0
    for compare in FinalHash:
        for hash_val in hash_text:
            if hash_val in set(compare):
                match+=1
    percentage = match/len(hash_text)
    plagiarism_values.append(percentage)
