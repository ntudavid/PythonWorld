'''
tutorial (6) - object-oriented, class

2016/06/20

David Hsu
'''

class Resident:
    def __init__(self, firstName, lastName, gender, ssn):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.ssn = ssn

    def getName(self):
        print(self.firstName,self.lastName)

    def getSSN(self):
        print('SSN =', self.ssn)

class Student(Resident):
    def __init__(self, firstName, lastName, gender, ssn, school, uin):
        # inherit from parent object (Resident) 
        super(Student, self).__init__(firstName, lastName, gender, ssn)
        self.school = school
        self.uin = uin

    def recordGPA(self, gpa):
        self.gpa = gpa

    def quryGPA(self):
        print(self.gpa)

    # override the method from parent 
    def getName(self):
        print('The student is', self.firstName, self.lastName)



# ntudavid = Resident('WeiWen','Hsu','M', 123456789)
# smallWei = Student('WeiWen','Hsu','M', 123456789,'NTU',98922081)

    

    

    


            
        

