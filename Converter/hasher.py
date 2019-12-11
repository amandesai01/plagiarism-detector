import os,hashlib

def HashElement(text):
    hashval = hashlib.sha256(text.encode())
    strOfHashVal = str(hashval.digest()).replace('\\x', '')
    return strOfHashVal

def hash1(text_array):
    hashed_list = []
    for groups in text_array:
        hashed = HashElement(groups)
        hashed_list.append(hashed)

    return hashed_list

def Manager(fileSet):
    hash_list={}
    for key in fileSet:
        temp_list = hash1(fileSet[key])
        hash_list[key]=temp_list
    return hash_list


#driver
# strr = []
# n = int(input())
#
# for i in range(0,n):
#     x = input()
#     strr.append(x)
#
# hashed_list = hash1(strr)
# for hash_words in hashed_list:
#     print(hash_words)

