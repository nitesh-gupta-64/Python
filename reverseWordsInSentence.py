s=str(input())
l=s.split()
l1=[]
for i in l:
    a=i[::-1]
    l1.append(a)
print(' '.join(l1))