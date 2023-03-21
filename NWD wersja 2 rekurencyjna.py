def NWD_rekur(a, b):
    if b == 0:
        return a
    return NWD_rekur(b, a % b)
print(NWD_rekur(12, 18))
print(NWD_rekur(28, 24))