import random
from Person import Person
from Instructor import Instructor
from Student import Student

def makePersonInfo():
    FIRSTS = 8
    LASTS = 7
    firstNames = ["Bill", "Mary", "John", "Nancy", "Paul", "George", "Frodo", "Linda"]
    lastNames = ["Jones", "Smith", "Green", "White", "Baggins", "Dunhill", "Bourne"]

    MINAGE = 18
    AGERANGE = 40
    LRANGE = 1000000

    values = []
    values.append(firstNames[random.randrange(FIRSTS)])
    values.append(lastNames[random.randrange(LASTS)])
    values.append(random.randint(MINAGE, MINAGE+AGERANGE))
    values.append("L00"+str(random.randrange(LRANGE)))
    
    return values

def makeHours():
    NUMHRS = 9
    someHours= ["8-9", "9-10", "10-11", "11-12", "12-1", "1-2", "2-3", "3-4", "4-5"]

    result = "Mon:" + someHours[random.randrange(NUMHRS)] \
             + " Tue:" + someHours[random.randrange(NUMHRS)] \
             + " Wed:" + someHours[random.randrange(NUMHRS)] \
             + " Thu:" + someHours[random.randrange(NUMHRS)]
        
    return result


def makeGPA():
    return random.randrange(3) + random.randrange(100)/100


def main():

    print("This tests instructor class\n")

    MAXINSTRUCTORS = 4

        #create instructors
    instructors = []
    for i in range(MAXINSTRUCTORS):
        info = makePersonInfo()
        officeHrs = makeHours()
        instructors.append(Instructor(info[0], info[1], info[2], info[3], officeHrs))
        

    print("Faculty ")
    print(" shoud show 4 instructors with names, ages, Lnumbers, and office hours\n")
    print("     Name       Age  LNumber       Office Hours ")
    for i in range(MAXINSTRUCTORS):
        fName = instructors[i].getFirstName()
        lName = instructors[i].getLastName()
        age = instructors[i].getAge()
        lNum = instructors[i].getLNumber()
        officeHrs = instructors[i].getOfficeHours()
        print(f'{fName:7}' + f'{lName:8}' + f'{age:3}' + "  " + f'{lNum:12}' + f'{officeHrs:10}')
            
    
    print("\nThis tests student class")

    MAXSTUDENTS = 8


        #create students
    students = []
    for i in range(MAXSTUDENTS):
        info = makePersonInfo()
        gpa = makeGPA()
        students.append(Student(info[0], info[1], info[2], info[3], gpa))

    print("Students ")
    print(" should show 8 students with names, ages, Lnumbers, and GPAS\n")
    print("     Name          Age  LNumber    GPA ")
    for i in range(MAXSTUDENTS):
        fName = students[i].getFirstName();
        lName = students[i].getLastName();
        age = students[i].getAge();
        lNum = students[i].getLNumber();
        gpa = students[i].getGPA();
        print(f'{fName:7} {lName:8} {age:4}   {lNum:10} {gpa:.2f}')


    print("\nThis displays polymorphism of getJob")

        # create three persons
    MAXPERSONS = 3
    persons = []

    print("Showing jobs ")
    print("should output Test One Undefined, Test Two Instructor, Test Three Student")
    
    persons.append(Person("Test", "One", 42, "L00000001"))
    persons.append(Instructor("Test", "Two", 55, "L00000002"))
    persons.append(Student("Test", "Three", 21, "L00000003"))

    for person in persons:
        print(person.getFirstName() + " " +  person.getLastName() + " " + person.getJob())



if __name__ == '__main__':
    main()
