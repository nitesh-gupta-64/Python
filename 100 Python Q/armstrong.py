n=int(input())
dig = len(str(n))
s=0
k=n
while k!=0:
    s+=(k%10)**dig
    k//=10
if s==n:
    print("Armstrong")
else:
    print("Not Armstrong")