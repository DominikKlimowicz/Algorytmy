T=[1,8,6,7,1,87,236,74,15,7]
najmn=T[0]
i=0
pozycja=0
while i < len(T):
    if najmn > T[i]:
        najmn = T[i]
        pozycja = i+1
    i+=1
print(f"najmniejsza {najmn} \n pozycja {pozycja}")