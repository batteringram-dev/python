
# Function definition - You define the function.
def hello():
    print("hello")

def world():
    print("world")

# Function execution - You actually call the function.
hello()
world()


#----------------------------------------------
# Understanding function scope.
# Any variable defined inside the functions, the scope of the variable is then within that function only.

x = 1 # global scope.

def scope():
    z = 2 # function scope.
    print(x)
    print(z)

def scope2(y):
    print(x)
    print(y)


scope()
scope2(3)
print(x)