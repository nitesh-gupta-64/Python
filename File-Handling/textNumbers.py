f=open("./File-Handling/textNumbers.txt", "r")
textFile=open("./File-Handling/text.txt", "w")
numbersFile=open("./File-Handling/numbers.txt", "w")
for i in f.read():
    if i.isdigit():
        numbersFile.write(i)
    else:
        textFile.write(i)
f.close()
textFile.close()
numbersFile.close()