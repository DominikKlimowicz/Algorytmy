def hanoi(N, A, B, C):
    if N == 1:
        print(f"Przenieś krążek z {A} na {B}")
    else:
        hanoi(N - 1, A, C, B)
        print(f"Przenieś krążek z {A} na {B}")
        hanoi(N - 1, C, B, A)

# Testowanie algorytmu
N = 3
A = "A"
B = "B"
C = "C"

hanoi(N, A, B, C)