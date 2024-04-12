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





# # CLASS METHOD DECORATOR
# # --> It is for whole class
# class Person:
#     name = "anonymous"

#     # @classmethod
#     # def changeName(self, name):
#     #     self.name = name

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

#     # def changeName(self, name):
#     #     self.__class__.name = name

# p1 = Person()
# p1.changeName("Nitesh")
# print(p1.name)
# print(Person.name)




# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
    
#     # def calcPercentage(self):
#     #     self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math)/3) + "%"

# s1 = Student(98, 99, 100)
# print(s1.percentage)

# s1.phy = 86
# print(s1.percentage)







# # POLYMORPHISM : OPERATOR OVERLOADING
# # --> WHEN SAME OPERATOR IS ALLOWED TO HAVE DIFFERENT MEANING

# print(1 + 2)  #add
# print("Nitesh " + "Gupta")  #concatenate
# print([1,2,3] + [4,5,6])  #merge
# # SAME + BUT DIFFERENT MEANINGS


# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)

# n1 = Complex(2,4)
# n1.showNumber()

# n2 = Complex(7,8)
# n2.showNumber()

# n3 = n1 + n2
# n3.showNumber()

# n4 = n2 - n1
# n4.showNumber()






# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def Area(self):
#         self.area = 3.14*self.radius*self.radius
#         print(self.area)

#     def Perimeter(self):
#         self.perimeter = 2*3.14*self.radius
#         print(self.perimeter)

# c1 = Circle(5)
# c1.Area()
# c1.Perimeter()





# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
#     def showDetails(self):
#         print(self.role, self.dept, self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "900000")

# e1 = Engineer("Nitesh", 19)
# e1.showDetails()



# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, o2):
#         if self.price > o2.price:
#             print("o1 > o2")
#         else:
#             print("o1 < o2")

# o1 = Order("Shivek", 6)
# o2 = Order("Nasib", 9)

# o1 > o2

        