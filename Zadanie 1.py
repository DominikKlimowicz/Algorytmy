lista = [5, 87, 95, 45, 15, 4, 45, 378, 248, 6, 54, 782, 123]
def szukaj(lista, szukana):
    if szukana in lista:
        print("Podana wartość znajduje się na miejscu ", lista.index(szukana)+1)
    else :
        print("Podanej wartości nie ma w liście")
szukaj(lista, 5)
szukaj(lista, 15)
szukaj(lista, 784)
szukaj(lista, 0)