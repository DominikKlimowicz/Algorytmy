tablica = [1, 2, 3, 4, 5]
i = 0
j = len(tablica) - 1
while i < j:
    x = tablica[i]
    tablica[i] = tablica[j]
    tablica[j] = x
    i += 1
    j -= 1
print(tablica)