n=int(input())
i=2
isPrime = True
while i<n:
    if n%i==0:
        isPrime = False
    i+=1
if isPrime:
    print("Prime")
else:
    print("Not Prime")
