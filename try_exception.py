
# Try, Exception is useful for error handling.

def get_input():
    try:
        number = int(input("Enter a number: "))
        return number
    except ValueError:
        raise NameError("asd")


def func1():

    try:
        n = get_input()
        return n
    except NameError as err:
        return err

res = func1()

if type(res) == int:
    print("goody")
else:
    print("try again, dumbo!")
    func1()




if type(n) == int:
    print("goody")
    print(n)
else:
    print("Not a number, dumbo!, try again")
    get_input()


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




