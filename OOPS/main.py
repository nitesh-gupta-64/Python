
# class Student:

#     collegeName = "NIT Kurukshetra"
#     name = "anonymous"

#     #default constructors
#     def __init__(self):
#         pass

#     #parameterized constructors
#     def __init__(self, name, marks):
#         self.name = name    #obj attr > class attr  <-- Priority
#         self.marks = marks
#         print("Adding new student in Database..")

#     def hello(self):
#         print ("Hello", self.name, "!!")
    
#     def getMarks(self):
#         return self.marks

# s1 = Student("Nitesh", 93)
# print(s1.name)
# print(s1.getMarks())
# s1.hello()

# s2 = Student("Rohit", 89)
# print(s2.name)
# print(s2.marks)

# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)




# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("Hello")

#     def displayAverageMarks(self):
#         sum = 0
#         for i in self.marks:
#             sum+=i
#         print("Hello", self.name, "your average marks is: ", sum/len(self.marks))
            
# s1 = Student("Nitesh", [96, 98, 97, 97, 100])
# s1.displayAverageMarks()




# class Student:
#     @staticmethod   #decorator
#     def college():
#         print("NIT Kurukshetra")





# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
    
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car started..")

# car1 = Car()
# car1.start()






# class Account:
#     def __init__(self, balance, accountNo):
#         self.balance = balance
#         self.accountNo = accountNo
    
#     def debit(self, debitedAmt):
#         self.balance -= debitedAmt
#         print("Rs.", debitedAmt, "was debited")

#     def credit(self, creditedAmt):
#         self.balance += creditedAmt
#         print("Rs.", creditedAmt, "was credited")
    
#     def displayBalance(self):
#         print(self.accountNo, ":", self.balance)

# a1 = Account(2000, "hy358u8fduh")
# a1.debit(1500)
# a1.credit(2000)
# a1.displayBalance()
    