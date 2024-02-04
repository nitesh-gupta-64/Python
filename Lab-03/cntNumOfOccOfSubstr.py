s1=str(input())
s2=str(input())
l=[]
i=0
while i<len(s1):
    index=s1.find(" "+s2,i)
    if index==-1:
        break
    l.append(index)
    i=index+1
print(len(l))