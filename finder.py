def find(FinalHash):
    plagiarism_values=[]
    for hash_text in FinalHash:
        match = 0
        for compare in FinalHash:
            for hash_val in hash_text:
                if hash_val in set(compare):
                    match+=1
        percentage = match/len(hash_text)
        plagiarism_values.append(percentage)

    return plagiarism_values
