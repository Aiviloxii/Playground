import CalFxn
print("=" * 50)
print("========My Calculator========")
print("=" * 50)
def cal():
    print(
        "Welcome to My Calculator\nEnter[1- for addition, 2- for subtraction, 3- for multiplication, 4- for division]")
    option = int(input())
    if option == 1:
        x = float(input("Enter any integer value:"))
        y = float(input("Enter another integer value to sum:"))
        print(f"The sum of {x} and {y} is {CalFxn.add(x, y)}")
    elif option == 3:
        x = float(input("Enter any integer value:"))
        y = float(input("Enter another integer value to multiply:"))
        print(f"The multiplication of {x} to {y} is {CalFxn.multiply(x, y)}")
    elif option == 4:
        x = float(input("Enter any integer value:"))
        y = float(input("Enter another integer value to divide:"))
        print(f"The division of {x} by {y} is {CalFxn.divide(x, y)}")
    elif option == 2:
        x = float(input("Enter any integer value:"))
        y = float(input("Enter another integer value to subtract:"))
        print(f"The subtraction between {x} and {y} is {CalFxn.subtract(x, y)}")
    else:
        print("Your have entered an invalid option")
check = True
while check:
    print("Do you wish to continue?\n[y- yes, n- no]: ")
    answer = input()
    if answer == 'y' or answer == "Y" or answer == "y":
        cal()
    elif answer == 'n' or answer == "N" or answer == "no":
        check = False
        print("Thanks for using my calculator")
    else:
        print("invalid option")
