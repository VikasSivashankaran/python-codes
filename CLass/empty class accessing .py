class Student:
    pass
class Marks:
    pass

student1=Student()
marks1=Marks()

print(isinstance(student1,Student))
print(isinstance(marks1,Student))
print(isinstance(marks1,Marks))
print(issubclass(Student,object))
print(Marks,object)