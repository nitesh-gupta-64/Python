s=str(input())
n=0
for i in s:
    if i.isnumeric():
        n+=1
ch=len(s)-n
print(ch)
print(n)
if ch>0 and n>0:
    print("String has atleast one letter and number")
else:
    print("Condition doesn't satisfied")