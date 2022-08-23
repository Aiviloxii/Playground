# Write a python class of Employee with ID, name, gender, post, salary, date of birth,date of employment.
# If he/she has spent 30 years with the company is due for retirement and age limit is 60 years.
from datetime import date
class Employee:
    empId =0
    empName = ""
    gender = ""
    post = ""
    salary = ""
    dob = ""
    doe = ""
    def create(self,empId,empName,gender,post,salary,dob,doe):
        self.empId =empId
        self.empName = empName
        self.gender = gender
        self.post = post
        self.salary = salary
        self.dob = dob
        self.doe = doe
    def viewEmp(self):
        print("_"*50)
        print("Employee Details")
        print("_" * 50)
        print(f"Employee name is {self.empName} \nEmployee ID is {self.empId}")
        print(f"Post is {self.post} \nDOB: {self.dob}")
        print(f"Gender:{self.gender} \nSalary: {self.salary}")
        print(f"The employee was employed at {self.doe}")
def empdata():
    a = input("Enter ID: ")
    b = input("Enter Name: ")
    c = input("Enter your gender:")
    d = input("Enter your post: ")
    e = input("Enter your salary: ")
    emp = Employee()
    def birthDate():
        print("******Birth Details******")
        diy = 365.2425
        y =int(input("Enter year: "))
        m = int(input("Enter the month: "))
        day = int(input("Enter the day: "))
        def empDate():
            print("****** Employment Date ******")
            ye = int(input("Enter year: "))
            me = int(input("Enter the month: "))
            de = int(input("Enter the day: "))
            DOB = date(y, m, day)
            DOE = date(ye, me, de)
            emp.create(a,b,c,d,e,DOB,DOE)
            empAge = int((date(ye, me, de) - date(y, m, day)).days / diy)
            age = int((date.today() - date(y, m, day)).days / diy)
            reAge = int((date.today() - date(ye, me, de)).days / diy)
            if empAge >= 60:
                print("You are above the required age limit and can't be employed")
            elif age >= 60:
                print("You are above the required age limit and can't be employed")
            elif empAge < 18:
                print("You are under the required age limit and can't be employed")
            elif age < 18:
                print("You are under the required age limit and can't be employed")
            elif 60 > empAge >= 18:
                if reAge >= 30:
                    print("This employee is due for retirement")
                elif reAge < 30:
                    emp.viewEmp()
            elif 60 > age >= 18:
                if reAge >= 30:
                    print("This employee is due for retirement")
                elif reAge < 30:
                    emp.viewEmp()
        empDate()
    birthDate()
print("Enter Employee details:")
empdata()
check = True
while check:
    x = input("Do you wish to enter another employee's details? [y/n]: ")
    if x == "y" or x == "yes":
        empdata()
    elif x == "n" or x == "no":
        print("Thank you for using this app")
        check = False
    else:
        print("You have entered an invalid option.")










