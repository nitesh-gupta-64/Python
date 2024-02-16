f=open("./File-Handling/spaceNumbers.txt", "r")
sum=0
for i in f.read():
    if i != " ":
        print(i)
        sum+=int(i)
print(sum)
f.close()