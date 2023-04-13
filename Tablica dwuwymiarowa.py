n = int(input("Podaj liczbę wierszy: "))
m = int(input("Podaj liczbę kolumn: "))

A = []

for i in range(n):
    row = []
    for j in range(m):
        y = int(input("Podaj element [" + str(i) + "][" + str(j) + "]: "))
        row.append(y)
    A.append(row)

for i in range(n):
    min_value = A[i][0]
    min_index = 0
    for j in range(1, m):
        if A[i][j] < min_value:
            min_value = A[i][j]
            min_index = j
    A[i][0], A[i][min_index] = A[i][min_index], A[i][0]

print("Tablica po zamianie minimalnych wartości na początek wierszy:")
for i in range(n):
    for j in range(m):
        print(A[i][j], end=" ")
    print()