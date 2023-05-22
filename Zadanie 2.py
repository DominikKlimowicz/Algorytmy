def usuwanie(lista, element):
    if element in lista:
        lista.remove(element)
    else :
        print("elementu nie ma na liście")
    print(lista)

L=[1, 2, 3, 4, 5]
usuwanie(L, 4)