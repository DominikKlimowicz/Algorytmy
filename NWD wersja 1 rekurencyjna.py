def NWD_rekur(a, b):
    if a == b:
        return a
    elif a > b:
        return NWD_rekur(a - b, b)
    else:
        return NWD_rekur(a, b - a)
print(NWD_rekur(12,18))
print(NWD_rekur(28,24))