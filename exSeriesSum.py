import math
n=int(input())
x=int(input())
sum=0

for i in range(n):
    sum = sum + (x**i)/(math.factorial(i))
print(sum)