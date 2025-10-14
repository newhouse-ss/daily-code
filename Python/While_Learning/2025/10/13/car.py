class Student:

    gender = "male"#attribute shared by all instances.
    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Par", 35)
student3 = Student("Shu", 23)

print(student1.name)
print(student2.age)
print(Student.num_students)
print(f"My class of {Student.class_year} has {Student.num_students} students")