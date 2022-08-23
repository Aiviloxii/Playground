# Write a python code that randomly picks a name from a list of students and gives a student a unique 7-digit code.
#Note your app should have only 6 unique codes to distribute and once six students have been given codes, it should not generate anymore.
import random as rd
students = ["Jeremy Agbo", "Rosette John", "Kendra James", "Bobby Grey",
            "Folande Ajayi", "Gabby Joseph", "Sandra Jacob", "Liam Henry"]
codes = rd.randrange(1000001,1000006)
choose = rd.choice(students)
for i in students:
    print(f"{choose} {codes}")