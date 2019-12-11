def find(FinalHash):
    # plagiarism_values=[]
    # for hash_text in FinalHash:
    #     match = 0
    #     for compare in FinalHash:
    #         temp_list=[]
    #         for hash_val in hash_text:
    #             if hash_val in set(compare):
    #                 match+=1

    #     percentage = match/len(hash_text)
    #     plagiarism_values.append(percentage)
    # return plagiarism_values
    plagiarism_values =[]
    for hash_text_file in FinalHash:
        hash_vals = []
        for compare_text_file in FinalHash:
            match=0
            for hash_val in FinalHash[hash_text_file]:
                if hash_val in set(FinalHash[compare_text_file]):
                    match+=1
            percentage = match
            hash_vals.append((compare_text_file,percentage))
        plagiarism_values.append((hash_text_file,hash_vals))
    return plagiarism_values




