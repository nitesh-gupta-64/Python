s=str(input())
l=s.split()
max=0
for i in l:
    if len(i)>max:
        ch=i
        max=len(i)
print(ch)
print(max)