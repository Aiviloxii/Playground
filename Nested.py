# Write a program that adds two electives to each student.
students = ["Jerry", "Martha", "Phil", "Louis", "Ruth", "Kendra"]
corecourses = ["Python Programming", "Visual Basic", "Fortran"]
electives = ["BOI 301", "GST 302", "PHY 303"]
for i in students:
    print(i)
    for j in corecourses:
        print("\t"+j+",", end="")
    print()
    for k in electives:
        print("\t"+k+"", end="")
        if len(corecourses) ==3 and len(electives) <= 2 :
            break
    print()
print(len(electives))