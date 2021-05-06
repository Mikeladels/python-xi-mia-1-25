#Latihan inheritance 1
class person(object):
    #constructor
    def __init__(self, name):
        self.name = name
    #to get name
    def getname(self):
        return self.name
    #to check if this person is an employee
    def isemployee(self):
        return False

#inherited or subclass (note person in bracket)
class employee(person):
    #here we return true
    def isemployee(self):
        return True

#driver code
emp = person("Mikel") #an object of person
print(emp.getname(), emp.isemployee())

emp = employee("Michi") #an object of employee
print(emp.getname(), emp.isemployee())