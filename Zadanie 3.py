lista1=[45, 184, 4, 4846, 465, 1]
lista2=[-745, 18, 48, 974, 47, -7, -98]
def scalanie(lista1, lista2):
    for i in lista2:
        lista=lista1
        lista.append(i)
    lista.sort()
    print(lista)
scalanie(lista1, lista2)