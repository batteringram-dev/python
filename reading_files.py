
# Reading Files in Python are helpful in reading, changing or modifying any other files.
# The first main command is " open " function. It will open the other file.
# The command "r" which stands are Reading, reads the information inside an another file.
# Another command is "w" stands for Writing, where you can write new and overwrite any information.
# "a" which stands for Append, where you can add new information.
# "r+" which basically means Read and Write.


employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)

employee_file.close()


