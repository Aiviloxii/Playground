# Create a directory named Apps with difrrent file formats: pictures, text, pdf and others.
# Create 3 folders: one for picture files, the second for text files, the third for others.
import os
def arrange(ListFiles, folder):
    for i in ListFiles:
        os.rename(i, folder+'/'+i)

getDir = input("Enter the folder name you want to arrange: ")
files = os.listdir(getDir)
picture =[]
text = []
pdf = []
others = []
for i in files:
    if i[-4:] == '.jpeg' or i[-4:] == '.png' or i[-4:]=='.JPG' or i[-4:]=='.PNG':
        picture.append(i)
    elif i[-4:] == '.txt':
        text.append(i)
    elif i[-4:] == '.pdf':
        pdf.append(i)
    else:
        others.append(i)
os.chdir(getDir)
os.mkdir("Pictures")
os.mkdir("Text")
os.mkdir("PDF")
os.mkdir("Others")
arrange(picture,"Pictures")
arrange(text, "Text")
arrange(pdf, "PDF")
arrange(others, "Others")
print("FIles arranged successfully!")