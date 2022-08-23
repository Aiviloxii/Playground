# import os
# name = input("Enter name of folder: ")
# os.mkdir(name)
# os.chdir(name)
# data = "Why doesn't it work with Entry?"
# fobj = open('m.txt', 'w')
# fobj.write(data)
# fobj.close()
# name2 = input('Enter name of the second folder: ')
# os.mkdir(name2)
# os.chdir(name2)
# data1 = len(data)
# d = data.split()
# data2 = len(d)
# all_data = f"The number of characters in your first file is: {data1}\nThe number of words are: {data2}"
# obj = open('s.txt', 'w')
# obj.write(all_data)

#Record families in a church, design a JSON file to hold these  records and insert 2 families data and print it out with your code.

# os.mkdir('Pictures')
# os.mkdir('Text')
# os.mkdir('Others')
# print("Folders created successfully")
# Moving to Text Folder
# os.chdir("Apps")
# if ".txt" in fname1:
#      os.rename("pic.jpg", 'Text/text.txt/')
# elif ".txt" in fname2:
#      os.rename("write.txt", 'Text/text.txt/')
# elif ".txt" in fname3:
#       os.rename("read.pdf", 'Text/text.txt/')
# elif ".txt" in fname4:
#       os.rename("mine.py", 'Text/text.txt/')
# Moving to Pictures
# if ".jpg" or "png" in fname1:
#      os.rename("pic.jpg", 'Pictures/pic.jpg/')
# elif ".jpg" or "png" in fname2:
#      os.rename("write.txt", 'Pictures/pic.jpg/')
# elif ".jpg" or "png" in fname3:
#       os.rename("read.pdf", 'Pictures/pic.jpg/')
# elif ".jpg" or "png" in fname4:
#       os.rename("mine.py", 'Pictures/pic.jpg/')
# Moving to Others
# if ".pdf" or ".py"  in fname1:
#      os.rename("pic.jpg", 'Others/pic.jpg/')
# elif ".pdf" or ".py" not in fname2:
#      os.rename("write.txt", 'Others/write.txt/')
# elif ".pdf" or ".py" not in fname3:
#       os.rename("read.pdf", 'Others/read.pdf/')
# elif ".pdf" or ".py" not in fname4:
#       os.rename("mine.py", 'Others/mine.py/')
import qrcode as qr
img = qr.make("welcome to python programming")
img.save("try.jpg")