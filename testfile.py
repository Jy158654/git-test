class Employee:
    raise_amt = 1.4
    num_employee = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_employee += 1

    @property
    def email(self):
        return self.first + self.last + "@gmail.com"

    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first,last = name.split(" ")
        self.first = first
        self.last = last
        print(first + last)

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print("Deleting")


emp_1 = Employee("John","Smith",50000)
print(emp_1.fullname)
emp_1.fullname = "Jun Yong"
del emp_1.fullname










