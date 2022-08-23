# Write a python code that prints the grades of a list of scores.
def grade(lst):
    for i in lst:
        if 70 <= i <= 100:
            print(f"{i}, Grade = A")
        elif 50 <= i < 70:
            print(f"{i}, Grade = B")
        elif 45 <= i < 50:
            print(f"{i}, Grade= C")
        elif 30 <= i < 45:
            print(f"{i}, Grade= D")
        elif i < 30:
            print(f"{i}, Grade= F")
        else:
            print("Invalid Score!")


scores = [55, 89, 90, 56, 30, 87, 97, 42, 48, 109, 2]
grade(scores)
