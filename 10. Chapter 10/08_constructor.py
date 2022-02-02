class Employee:
    company = 'Google'

    def __init__(self, name, salary, subunit):
        print('Employee initialised!!!.')
        self.name = name
        self.salary = salary
        self.subunit = subunit

    def getDetails(self):
        print(f"The name of employee is {self.name}")
        print(f"The name of employee is {self.salary}")
        print(f"The name of employee is {self.subunit}")

    @staticmethod
    def greet():
        print('Good morning, Sir.')

    @staticmethod
    def time():
        print('Time is 9 AM in the morning.')

    def getSalary(self):
        print(
            f"Salary for this employee working in {self.company} is {self.salary}k")


erus = Employee('Erus', 100, 'Google')
# erus = Employee() # error:- missing 3 positional arguements
# erus.salary = 100
# erus.getSalary()
erus.getDetails()
# erus.greet()
