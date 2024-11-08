#Create a class Student with attributes like name, age, and marks. Include methods to display the student details and calculate the grade based on marks.

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)   
        print("Age:", self.age)
        print("Marks:", self.marks)

    def grade(self):
        if self.marks >= 90:
            print("Grade: A")
        elif self.marks >= 80:
            print("Grade: B")
        elif self.marks >= 70:
            print("Grade: C")
        else:
            print("Grade: F")


s = Student("John", 20, 85)
s.display()
s.grade()