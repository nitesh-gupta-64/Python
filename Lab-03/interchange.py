s=str(input())
s1=''
for i in s:
    if i==':':
        s1+='-'
    elif i=='-':
        s1+=':'
    else:
        s1+=i
print(s1)