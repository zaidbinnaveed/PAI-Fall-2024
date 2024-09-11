class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def Print_Biodata(self):
        print("Student name : {}".format(self.name))
        print("Student age : {}".format(self.age))
        
    def student(self):
        print("He is a good student")
        
p1 = Student("Zaid", "20")


p1.Print_Biodata()
p1.student()
