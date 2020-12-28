
# Try, Exception is useful for error handling.

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")

# ---------------------------------------------------------------------------------------

# There are 2 different except blocks which can handle 2 different types of errors.
# 1) ZeroDivisionError - If you divide a number by zero, this block can be used.
# 2) ValueError - If you type an invalid input.
# The above blocks can also be used as variables.
# err = error

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")




