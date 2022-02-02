# class Employee:
#     company = "Google"
#     def getSalary(self):
#         print(f"Salary for this employee working in {self.company} is {self.salary}")

# erus = Employee()
# erus.salary = 100000
# erus.getSalary() # Employee.getSalary(erus)

class Employee:
    company = 'Google'

    def getSalary(self):
        print(
            f"Salary for this employee working in {self.company} is {self.salary}k")


erus = Employee()
erus.salary = 100
# erus.company = 'Youtube' # changing the attribute 'company' of the class.
erus.getSalary()
a = erus.company  # accessing the variables of class
print(a)
