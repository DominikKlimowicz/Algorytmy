n = int(input("Podaj długość tablicy: "))

T = []
i = 0

while i < n:
    y = int(input(f"Podaj {i+1}-tą wartość: "))
    T.append(y)
    i += 1

min = T[0]
i = 1

while i < n:
    if T[i] < min:
        min = T[i]
    i += 1

print(f"Minimalna wartość w tablicy to {min}")
