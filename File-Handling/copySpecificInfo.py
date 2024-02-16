f=open("./File-Handling/studentInfo.txt", "r")
newFile=open("./File-Handling/lessInfo.txt", "w")
for i in f.readline():
    while i!=",":
        newFile.write(i)
f.close()
newFile.close()