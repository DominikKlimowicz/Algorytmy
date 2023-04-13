n = int(input("Podaj liczbę krążków: "))
a, b, c = "A", "B", "C"
print(f"Przenieś {n} krążków z patyka {a} na patyk {b}.")

stos = []
stos.extend([n, a, b, c])

while stos:
    x, a, b, c = stos.pop()
    if x == 1:
        print(f"Przenieś krążek z {a} na {b}.")
    else:
        stos.extend([x-1, a, c, b, 1, a, b, c, x-1, c, b, a])