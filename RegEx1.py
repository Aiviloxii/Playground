import re
txt = "12 Below is the picture of the entity relationship diagram "\
    "for the above write up which can then be converted to" \
    "database letter on pg 13" \
    "Below is the picture of the entity relationship of diagram "\
    "for the above write up which can then be converted to" \
    "database 567  letter on bank GTb acct 00032421349"
txt1 = "Ogun, Taraba, Jigawa, Kogi, Delta"

# Write a code  that returns the number of times "of" is found in a text.
a = len(re.findall("of", txt))
print("The number of times 'of' appeared is: ",a)

# Write a code to return all positions of 'the' in the text above.
b = re.search(" the ", txt)
print(b)

# Write a code to return all two digits in the text above.
c = re.findall("[1-2][1-3]", txt)
print("All two digits are: ",c)
# A code to return list of states without spacing.
d = re.split(", ", txt1)
print(d)
# A code to return the number of 's' in a string.
# e = input("Enter the text: \n")
# f = len(re.findall("s", e))
# print("The number of 's' in your text is: ",f)