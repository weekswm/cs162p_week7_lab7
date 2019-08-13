#Instructor class
from Person import Person

class Instructor(Person):
    '''Creates an Instructor class derived from Person class
    attributes: officeHours
    '''
    #initializes Instructor person object with office hours
    def __init__(self, firstName, lastName, age, lNumber, officeHours = ''):
        super().__init__(firstName, lastName, age, lNumber)
        self.officeHours = officeHours

    #Getter and Setter for officeHours
    def getOfficeHours(self):
        return self.officeHours

    def setOfficeHours(self, newHours):
        self.officeHours = newHours

    #this is not returning the value of a variable, it is simply returning a hard coded string.
    def getJob(self):
        return "Instructor"