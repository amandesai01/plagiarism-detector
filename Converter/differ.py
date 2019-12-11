def difference(template,file):
    # template = template.splitlines()
    new_diff= []
    for f_line in file:
        if f_line not in set(template):
            new_diff.append(f_line)

    return new_diff



