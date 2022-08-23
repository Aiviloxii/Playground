# Write a simple calculator that takes in two numbers from the user and adds, subtracts, multiply, modulus, quotient of
# those numbers.
print("Welcome to Olivia's Calculator")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def remain(a, b):
    return a % b


def power(a, b):
    return a ** 2, b ** 2


x = float(input("Enter the first value : "))
y = float(input("Enter the second value : "))
print("Here are the options")
print("a  = add")
print("b =  multiply")
print("c = divide")
print("d = remainder")
print("e = square")
print("f = subtract")
print("# = stop")


check = True
while check == True:
    v = input("Please pick an option:")
    if v == "a":
        print(f"The addition of {x} to {y} = ", add(x, y))
    elif v == "f":
        print(f"To subtract {x} from {y} =", subtract(x, y))
    elif v == "d":
        print(f"The remainder of {x} divided by {y} =", remain(x, y))
    elif v == "c":
        print(f"To divide {x} by  {y} =", divide(x, y))
    elif v == "b":
        print(f"To multiply  {x} to  {y} =", multiply(x, y))
    elif v == "e":
        print(f"The square of {x} and  {y} =", power(x, y))
    elif v == "#":
        print("Thank you and Adios!")
        check = False
    else:
        print("Invalid option")











