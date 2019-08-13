import math
from Person import Person

#Student class
class Student(Person):
    '''Creates Student class derived from Person class
    attributes: gPA
    '''
    #initializes a student person with GPA
    def __init__(self, firstName, lastName, age, lNumber, gPA = 0):
        self.gPA = gPA
        super().__init__(firstName, lastName, age, lNumber)

    #Getter and Setter for GPA
    def getGPA(self):
        return self.gPA

    def setGPA(self, newGPA):
        self.gPA = newGPA

    #this is returning a hard coded string.
    def getJob(self):
        return "Student"

