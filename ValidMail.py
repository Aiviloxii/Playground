# Write a program to check if an email is valid or not.
print("Mail validity check")
mail = input("Enter your email address: ")
if "@" in mail and len(mail[mail.index("."):]) > 2 and " " not in mail:
    print(f"{mail} is a valid email address")
else:
    print(f"{mail} is not a valid email address")

