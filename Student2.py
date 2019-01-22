class Student:
    def __init__(self,name,major,gpa):
        self.name=name
        self.major=major
        self.gpa=gpa
    def info(self):
        print ('Hello %s'%self.name)