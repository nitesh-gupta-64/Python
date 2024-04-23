class Father:
    def skills(self):
        print("Father's skills: Fishing, Gardening")

class Mother:
    def skills(self):
        print("Mother's skills: Cooking, Sewing")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Child's skills: Playing, Studying")

child = Child()
child.skills()
