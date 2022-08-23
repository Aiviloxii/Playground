class BestBrains:
    name = "Best Brains College USA"
    colour = "Green"
    motto = "The Sky is your starting point"
class SSS(BestBrains):
    section = 0
    partition = ""
    coreSub = ["Eng", "Maths","Trade","Civic Edu","Economics","Geography"]
    def create(self, section,partition):
        self.section = section
        self.partition = partition
class ArtStudent(SSS):
    ArtSec1 = ["Govt One", "History One", "Literature One"]
    ArtSec2 = ["Govt Two", "History Two", "Literature Two"]
    ArtSec3 = ["Govt Three", "History Three", "Literature Three"]
    subjectList = []
    def Art(self,section,partition):
        if section ==1 and partition == "Art":
            self.subjectList = self.coreSub + self.ArtSec1
        elif section ==2 and partition == "Art":
            self.subjectList = self.coreSub + self.ArtSec2
        else:
            self.subjectList = self.coreSub + self.ArtSec3

class SciStudent(SSS):
    SciSec1 = ["Biology One", "Chemistry One", "Physics One","Fur Maths"]
    SciSec2 = ["Biology Two", "Chemistry Two", "Physics Two","Fur Maths"]
    SciSec3 = ["Biology Three", "Chemistry Three", "Physics Three","Fur Maths"]
    subjectList = []
    def Sci(self,section,partition):
        if section ==1 and partition == "Science":
            self.subjectList = self.coreSub + self.SciSec1
        elif section ==2 and partition == "Science":
            self.subjectList = self.coreSub + self.SciSec2
        elif section ==3 and partition == "Science":
            self.subjectList = self.coreSub + self.SciSec3


class SenStudent(ArtStudent,SciStudent):
    fullname = ""
    age = 0
    gender = ""
    guardian = ""
    def __init__(self,fullname,age,gender,guardian,class1,part):
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.guardian = guardian
        self.Art(class1,part)
        self.Sci(class1,part)
student=SenStudent("Jason Brown",15,"male","Brown Folade",2,"Art")
print(f"Welcome, {student.fullname} to {student.name} ")
print(f"These are your subjects:{student.subjectList} ")
