def difference(template,file):
    # template = template.splitlines()
    file = file.splitlines()
    new_diff=""
    for f_line in file:
        if f_line not in set(template):
            new_diff+=f_line+"\n"

    return new_diff



