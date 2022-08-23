# Write a program that get the multiplication table of 9, 10, 11 in a tabular form.
a = 9
b = 10
c = 11
for n in range(12):
    print(f"{a} x {n + 1} = {a*(n + 1)} \t{b} x {n + 1} = {b*(n + 1)} \t{c} x {n + 1} = {c*(n + 1)}")
