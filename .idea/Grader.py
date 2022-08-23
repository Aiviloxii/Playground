# Write a python code that prints the grades of a list of scores.
scores = [55, 89, 90, 56, 30, 87, 97, 42, 48,109, 59,10,29, 12]
for i in scores:
    if i >= 70 and i <= 100:
        print(f"{i}, Grade= A")
    elif i >=50 and i < 70:
        print(f"{i}, Grade = B")
    elif i >=45 and i < 50:
        print(f"{i}, Grade= C")
    elif i >= 30 and i < 45:
        print(f"{i}, Grade= D")
    elif i < 29:
        print(f"{i}, Grade= F")
    else:
        print("Invalid Score!")
