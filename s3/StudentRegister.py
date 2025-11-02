
class Student:

    def __init__(self, name, id = -1):
        self.id = id
        self.name = name

    def isComplete(self):
        if self.id == -1:
            print("Invalid Student ID")
            return False
        elif not self.name.isalpha():
            print("Invalid Student Name")
            return False
        else:
            return True

    @staticmethod   
    def checkID(id):
        if id.isalnum():
            return True
        else:
            #print(f"Invalid input {id}")
            return False
    
    @staticmethod
    def checkName(name):
        if name.strip():
            return True
        else:
            #print(f"Invalid input {name}")
            return False

def saveToCSV():
    print("Saving data....")
    with open("students.csv","+at") as csvFile:
        print(csvFile.readline())
        for student in studentList:
            print(f"{student.id} : {student.name}")
            csvFile.write(f"{student.id},{student.name}\n")

def exit():
    saveToCSV()
    print("Terminating the program....")
    quit()

studentList = []

try:
    with open("students.csv","+rt") as csvFileR:
        csvFileR.readline()
except:
    with open("students.csv","+wt") as csvFileH:
        csvFileH.write(f"ID,Name\n")

while True:
    student = Student("", "")
    
    id = "_"
    while not student.checkID(id):
        id = input("Enter Student ID (or type 'exit' to finish):")
        if id == "exit":
            exit()

    name = ""
    while not student.checkName(name):
        name = input("Enter Student Name:")
        if name == "exit":
            exit()

    id = id.strip()
    name = name.strip(" ,_.!")
    student.id = id
    student.name = name
    studentList.append(student)

        

