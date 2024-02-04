s=str(input())
l=s.split()
l1=[]
for i in l:
    l1.append(''.join(sorted(i)))
print(' '.join(l1))