class Employee:
    company = "Rumpum"
    salary = 100
    location = "Itahari"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(self, sal):
        self.salary = sal


e = Employee()
print(e.salary)
e.changeSalary(355)
print(e.salary)
print(Employee.salary)
