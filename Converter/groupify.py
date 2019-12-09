def group(text):
    groups = []
    words = text.split('.')
    sent = ""
    cnt=0
    print([word for word in words])
    rem = len(words)//3
    for word in words:
        print(str(cnt))
        if cnt%3==0 and cnt!=0 or cnt > (3*rem) and cnt < len(words):
            if cnt>(3*rem) and cnt<len(words):
                arr = words[cnt:len(words)]
                sent=""
                for x in arr:
                    sent+=x+" "
                groups.append(sent)
            else:
                groups.append(sent)
                sent=""
        sent+=word+" "
        cnt+=1
    return groups

inx = input()
ls = group(inx)

for x in ls:
    print(x)
