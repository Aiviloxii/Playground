# Record families in a church, design a JSON file to hold these  records and insert 2 families data and print it out with your code.
import json
def view():
    with open("data.json", "r") as rf:
        data = json.load(rf)
        return data
def viewChild():
    with open("data.json", "r") as rf:
        data = json.load(rf)
        for i in range(len(data)):
            print(data[i]["children"][0][0]+" "+data[i]["surname"])

surname= input("Enter your surname: ")
dad = input("Enter Father's name: ")
mum = input("Enter Mother's name: ")
dadAge = int(input("Enter Father's age: "))
mumAge = int(input("Enter Mother's age: "))
child = input("Enter Child's name: ")
childAge = int(input("Enter Child's age: "))
newFamily = {"surname": surname,
        "dad": dad,
        "dadAge": dadAge,
        "mum": mum,
        "mumAge": mumAge,
        "children": [
        [
child,
childAge
]
]
             }
newData = newFamily
oldData = view()
oldData.append(newData)
with open("data.json", "w") as wf:
    json.dump(oldData, wf)
print("Data inserted successfully\n")
print("The names of all the children are: ")
viewChild()

