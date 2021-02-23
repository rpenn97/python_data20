def films():
    temp = []
    cont = True
    while cont is True:
        film = input("What is a favourite film of yours?")
        temp.append(film)
        carry = input("Any more films to add?(Y/N)")
        if carry.lower() == "y":
            continue
        else:
            cont = False
    return temp

print(films())