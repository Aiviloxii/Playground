import datetime as dt
class Employee:
    def __init__(self,empId,empName,gender,post,salary,doe):
        self.empId =empId
        self.empName = empName
        self.gender = gender
        self.post = post
        self.salary = salary
        self.doe = doe
    def viewEmp(self):
        print("_"*50)
        print("Employee Details")
        print("_" * 50)
        print(f"Employee name is {self.empName} \nEmployee ID: {self.empId}")
        print(f"Post: {self.post}")
        print(f"Gender:{self.gender} \nSalary: {self.salary}")
        print(f"The employee was employed at {self.doe}")

def empdata():
    a = input("Enter ID: ")
    b = input("Enter Name: ")
    c = input("Enter your gender:")
    p = input("Enter your post: ")
    e = input("Enter your salary: ")
    print("****** Employment Date ******")
    y1 = int(input("Enter year: "))
    m1 = int(input("Enter the month: "))
    d1 = int(input("Enter the day: "))
    DOE = dt.date(y1, m1, d1)
    emp=Employee(a, b, c, p, e,DOE)
    rtAge = int((dt.date.today() - dt.date(y1, m1, d1)).days / 365)
    if rtAge >= 30:
        emp.viewEmp()
        print("\bTHIS EMPLOYEE IS DUE FOR RETIREMENT!")
    elif rtAge < 30:
        emp.viewEmp()
        print(f"You have {30 - rtAge} years to retirement")
def ager():
    print("******Birth Details******")
    diy = 365
    y = int(input("Enter your birth year: "))
    m = int(input("Enter your birth month: "))
    d = int(input("Enter your birthday: "))
    DOB = dt.date(y, m, d)
    age = int((dt.date.today() - DOB).days / diy)
    if age >= 60:
        print(f"You are {age}years old and above the required age limit.Thus can't be employed")
    elif age < 18:
        print(f"You are {age}years old and under the required age limit. Thus can't be employed")
    else:
        print(f"Congratulations!! You are {age}years old and  elidgible for employment!")
        empdata()
print("<>"*50)
print("\bWelcome to the Employee Analysis Platform")
print("<>"*50)
ager()
check = True
while check:
    q = input("Do you wish to enter another? [y- yes or n- no]: ")
    if q == "y" or q == "yes" or q=="Y":
        ager()
    elif q == "n" or q == "no" or q=="N":
        print("Thank you for using this app")
        check = False
    else:
        print("You have entered an invalid option.")