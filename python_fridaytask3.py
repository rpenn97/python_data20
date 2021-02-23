def iso(x):
    templist = []
    for i in x:
        if i.isalpha():
            templist.append(i.lower())
    if len(templist) != len(set(templist)):
        return False
    else:
        return True
print(iso(input()))


