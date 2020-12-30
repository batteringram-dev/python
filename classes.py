
# Classes are very useful in Python. What does Classes do? It stores big and different types of data.
# In this example program, i have created an information of a student in another file.
# So, with that i am going to create a Student Object. The student object will represent the name, age, gpa etc.

from student import Student

student1 = Student("Jim", "Business", 3.5, False)

print(student1.name)