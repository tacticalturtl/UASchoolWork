#Tyson R. Gant
#4/10/2020
#HW5 - Pet Sitting
from enum import Enum

class PetType(Enum):
    DOG = 1,
    CAT = 2,
    HAMSTER = 3,
    SNAKE = 4

class Gender(Enum):
    MALE = 1,
    FEMALE = 2,
    OTHER = 3,
    NO_INFO = 4

class Services(Enum):
    FEED = 1,
    WALK = 2,
    BOARD = 3,
    VISIT = 4

class Age(Enum):
    Young = 20,
    MidAge = 35,
    Elder = 60

class PetSitting:
    def __init__(self, petType, Services, startDate, endDate, startTime, endTime,  petName = "",):
        self.__name = petName
        self.__pettype = petType
        self.__services = Services
        self.__startdate = startDate
        self.__enddate = endDate
        self.__starttime = startTime
        self.__endtime = endTime

    def getName(self):
        return self.__name
    
    def getPetType(self):
        return self.__pettype

    def getServices(self):
        return self.__services

    def getStartDate(self):
        return self.__startdate

    def getEndDate(self):
        return self.__enddate

    def getStartTime(self):
        return self.__starttime

    def getEndTime(self):
        return self.__endtime

    def setName(self, petName):
        self.__name = petName

    def setPetType(self, petType):
        self.__pettype = petType

    def setServices(self, Services):
        self.__services = Services
    
    def setStartDate(self, startDate):
        self.__startdate = startDate
    
    def setEndDate(self, endDate):
        self.__enddate = endDate
    
    def setStartTime(self, startTime):
        self.__starttime = startTime
    
    def setEndTime(self, endTime):
        self.__endtime = endTime

    def toString(self):
        returnedString = "Pet Name: " + self.__name
        returnedString += "\n\t Pet Type: " + self.__pettype
        returnedString += "\n\t Services: " + self.__services
        returnedString += "\n\t Start Date: " + self.__startdate
        returnedString += "\n\t End Date: " + self.__enddate
        returnedString += "\n\t Start Time: " + self.__starttime
        returnedString += "\n\t End Time: " + self.__endtime
        return returnedString

class Person:
    def __init__(self, age, name = "", gender = Gender.NO_INFO):
        self.__name = name
        self.__gender = gender
        self.__age = age

    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender
    
    def getAge(self):
        return self.__age
    
    def setName(self, name):
        self.__name = name
    
    def setGender(self, gender):
        self.__gender = gender
    
    def setAge(self, age):
        self.__age = age
    
    def toString(self):
        returnedString = "Name: " + ( self.__name)
        returnedString += "\n\t Gender: " + (self.__gender)
        returnedString += "\n\t Age: " + (self.__age)
        return returnedString

class Boarding:
    def __init__(self, Person):
        self.__PersonList = []
        self.__PetList = []
        self.__PersonList.append(Person)

    def addPerson(self, person):
        self.__PersonList.append (person)

    def addPet(self, pet):
        self.__PetList.append (pet)

    def move(self, name):
        i = 0
        isFound = False
        while (isFound == False and i <len(self.__PersonList)):
            if (self.__PersonList[i].getName() == name):
                isFound = True
            else:
                i += 1
        self.__PersonList.pop(i)

    def getStringPerson(self):
        returnedString = ""
        for i in self.__PersonList:
            returnedString += str (i.toString()) + "\n"
        return returnedString

    def getStringPet(self):
        returnedString = ""
        for i in self.__PetList:
            returnedString += str (i.toString()) + "\n"
        return returnedString
    
    def toString(self):
        stringReturned = "Persons:\n\t" + self.getStringPerson()
        if (self.__PetList != []):
            stringReturned += "\n Pets:\n\t" + str(self.getStringPet())
        return stringReturned

def main():
    Person1 = Person("Jason", "Male", "34")
    firstBoarding = Boarding (Person1)

    Pet1 = PetSitting("Dog", "Board, Walk, Feed", "04/08/2020", "04/10/2020", "1200", "1300", "Bolt")
    firstBoarding.addPet(Pet1)
    print (firstBoarding.toString())

main()