
# Classes are very useful in Python. What does Classes do? It stores big and different types of data.
# In this example program, i have created an information of a student in another file.
# So, with that i am going to create a Student Object. The student object will represent the name, age, gpa etc.

from student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("John", "Accountant", 3.8, False)

print(student2.on_honor_roll())