def palindrone(phrase):
    x = -1
    y = 0
    noSpaces = []
    makeList = list(phrase)
    for i in makeList:
        if i == " ":
            del i
        else:
            noSpaces.append(i)
    for i in noSpaces:
        if i != noSpaces[x]:
            y = 1
            break
        x = x - 1
    if y == 1:
        print("Not a palindrone!:(")
    else:
        print("It is a palindrone!:D")

print("This algorithm checks for palindrones.")
phrase = input("Please enter input: ")
palindrone(phrase)
