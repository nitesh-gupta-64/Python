f=open("./File-Handling/read.txt", "r")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.read(3))

for i in f:
    print(i)

f.close()
