class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name) 
        self.age = age

    def greet(self):
        super().greet()
        print(f"I am {self.age} years old")

child = Child("Alice", 8)
child.greet()
