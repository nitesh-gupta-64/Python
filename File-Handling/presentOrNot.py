f=open("./File-Handling/read.txt", "r")
print("is Present") if input() in f.read() else print("not Present")
f.close()