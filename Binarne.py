L = [1, 6, 42, 3, 5, 23423, 654, 234534, 346, -214, -15, -5]
L.sort()
Y = 23423

def Bin(list, element):
    znaleziono = False
    while len(list) > 0 and not znaleziono:
        srodek = int(len(list) / 2)
        if element == list[srodek]:
            znaleziono = True
            break
        elif element < list[srodek]:
            list = list[:srodek]
            return Bin(list, element)
        elif element > list[srodek]:
            list = list[srodek:]
            return Bin(list, element)

    if znaleziono == False:
        print("Nie znaleziono danego elementu")
    elif znaleziono == True:
        print("Znaleziono dany element")

Bin(L, Y)
