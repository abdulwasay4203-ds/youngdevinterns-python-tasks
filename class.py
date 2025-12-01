# Student class with functions to display details and calculate percentage

class Student:
    def __init__(self, name, math, eng, sci):
        self.name = name
        self.math = math
        self.eng = eng
        self.sci = sci

    def total_marks(self):
        return self.math + self.eng + self.sci

    def percentage(self):
        return self.total_marks() / 3

    def show_info(self):
        print("Student Name:", self.name)
        print("Total Marks:", self.total_marks())
        print("Percentage:", self.percentage(), "%")

name = input("Enter name: ")
math = int(input("Math marks: "))
eng = int(input("English marks: "))
sci = int(input("Science marks: "))

s = Student(name, math, eng, sci)
s.show_info()
