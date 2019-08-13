#Person class
class Person:
    '''Create base Person class from which the Instructor and Student classes
    will be derived.
    attributes: firstName, lastName, age, lNumber
    '''
    def __init__(self, firstName = '', lastName = '', age = 0, lNumber = ''):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.lNumber = lNumber

    '''Getters and Setters for Person class variables'''
    #Getter and Setter for firstName
    def getFirstName(self):
        return self.firstName

    def setFirstName(self, newFirst):
        self.firstName = newFirst

    #Getter and Setter for lastName
    def getLastName(self):
        return self.lastName

    def setLastName(self, newLast):
        self.lastName = newLast

    #Getter and Setter for age
    def getAge(self):
        return self.age

    def setAge(self, newAge):
        self.age = newAge

    #Getter and Setter for lNumber
    def getLNumber(self):
        return self.lNumber

    def setLNumber(self, newLNumber):
        self.lNumber = newLNumber

    #this does not access a variable, it simply returns a hard coded string.
    def getJob(self):
        return "Undefined"