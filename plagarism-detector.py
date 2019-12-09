import os
import classifier
path = input()
files = []
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

for f in files:
    classifier.classify(f)
