class Student:
    def __init__(self, name, rollno, age, marks):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.marks = marks

    def calculate_percentage(self):
        total_marks = sum(self.marks)
        return (total_marks / len(self.marks))

students = []
students_info = [
    ("John", 101, 20, [85, 90, 88, 92]),
    ("Alice", 102, 21, [78, 85, 80, 90]),
    ("Bob", 103, 19, [92, 88, 90, 85]),
    ("Emily", 104, 20, [80, 85, 75, 82]),
    ("David", 105, 22, [88, 90, 85, 78]),
    ("Emma", 106, 21, [85, 82, 90, 88]),
    ("Michael", 107, 20, [90, 85, 88, 92]),
    ("Sophia", 108, 19, [82, 78, 85, 80]),
    ("James", 109, 20, [85, 90, 88, 86]),
    ("Olivia", 110, 21, [88, 85, 90, 92])
]

for info in students_info:
    student = Student(info[0], info[1], info[2], info[3])
    students.append(student)

total_percentage = 0
for student in students:
    percentage = student.calculate_percentage()
    total_percentage += percentage
    print("Name:", student.name)
    print("Roll No:", student.rollno)
    print("Age:", student.age)
    print("Marks:", student.marks)
    print("Percentage:", "{:.2f}%".format(percentage))
    print()

average_percentage = total_percentage / len(students)
print("Average Percentage of all students:", "{:.2f}%".format(average_percentage))
print()

sorted_students = sorted(students, key=lambda x: x.calculate_percentage(), reverse=True)
print("Students sorted based on percentage of marks:")
for student in sorted_students:
    print("Name:", student.name)
    print("Roll No:", student.rollno)
    print("Age:", student.age)
    print("Marks:", student.marks)
    print("Percentage:", "{:.2f}%".format(student.calculate_percentage()))
    print()
