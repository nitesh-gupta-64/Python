class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("Animal speaks")

    def __add__(self, other):
        if isinstance(other, Animal):
            return self.species + " " + other.species
        else:
            raise TypeError("Unsupported operand type for +")

    def __mul__(self, other):
        if isinstance(other, int):
            return self.species * other
        else:
            raise TypeError("Unsupported operand type for *")

    def __gt__(self, other):
        if isinstance(other, Animal):
            return len(self.species) > len(other.species)
        else:
            raise TypeError("Unsupported operand type for >")


class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

    def speak(self):
        print("Dog barks")

# Constructor overriding
dog1 = Dog("Canis", "Labrador")
dog2 = Dog("Canis", "German Shepherd")

# Method overriding
dog1.speak()

# Operator overloading
print(dog1 + dog2)  # Output: Canis Canis German Shepherd
print(dog1 * 3)      # Output: CanisCanisCanis
print(dog1 > dog2)   # Output: False
