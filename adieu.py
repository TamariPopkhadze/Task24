import inflect

p = inflect.engine()
listOfNames = []
while True:
    try:
       listOfNames.append(input("Name: "))
    except EOFError:
        print("Adieu, adieu, to " + p.join(listOfNames))
        break
