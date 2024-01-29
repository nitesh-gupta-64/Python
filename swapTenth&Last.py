k=input()
n=list(k)
last=n[-1]
tenth=n[9]
n[-1]=tenth
n[9]=last

for i in n:
    print(i, end="")
