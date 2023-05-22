def sortlist(ilosc):
    lista=[]
    zliczanie=0
    while zliczanie<ilosc:
        a=int(input("Podaj liczbę: "))
        lista.append(a)
        lista.sort()
        zliczanie+=1
    print(lista)

sortlist(5)