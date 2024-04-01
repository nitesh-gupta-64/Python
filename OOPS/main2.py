# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Shivek")
# print(s1.name)
# # del s1.name



# class Account:
#     def __init__(self, balance, accountNo, accountPass):
#         self.balance = balance
#         self.accountNo = accountNo
#         self.__accountPass = accountPass
    
#     def debit(self, debitedAmt):
#         self.balance -= debitedAmt
#         print("Rs.", debitedAmt, "was debited")

#     def credit(self, creditedAmt):
#         self.balance += creditedAmt
#         print("Rs.", creditedAmt, "was credited")
    
#     def displayBalance(self):
#         print(self.accountNo, ":", self.balance)

#     def resetPass(self):
#         print(self.__accountPass)

# a1 = Account(2000, "hy358u8fduh", "n1i2t3e4s5h6")
# a1.debit(1500)
# a1.credit(2000)
# a1.displayBalance()
# a1.resetPass()
# # print(a1.__accountPass)   #Not gonna Work
    




# Inheritance:
# --> when child class derives the properties and methods of another class.

# class Car:
#     @staticmethod
#     def start():
#         print("Car Started")

#     @staticmethod
#     def stop():
#         print("Car Stopped")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")

# car1.start()
# car2.stop()
        
# car1 = Fortuner("diesel")
# car1.start()




# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A, B):
#     varC = "Welcome to class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)




# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car Started")

#     @staticmethod
#     def stop():
#         print("Car Stopped")

# class ToyotaCar(Car):
#     def __init__(self, brand, type):
#         super().__init__(type)
#         self.brand = brand
#         super().start()

# car1 = ToyotaCar("prius", "electric")
# print(car1.type)





# CLASS METHOD DECORATOR
# --> It is for whole class
class Person:
    name = "anonymous"

    @classmethod
    def changeName(self, name):
        self.name = name

p1 = Person()
p1.changeName("Nitesh")
print(p1.name)
print(Person.name)