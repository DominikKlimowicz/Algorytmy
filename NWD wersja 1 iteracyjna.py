def NWD(a,b):
    while a!=b:
        if a>b :
            a=a-b
        else:
            b=b-a
    return a
print(NWD(12,18))
print(NWD(28,24))