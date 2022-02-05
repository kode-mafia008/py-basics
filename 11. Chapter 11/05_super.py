
class Person:
    country = 'Nepal'

    def __init__(self):
        print('Initializing Person......\n')

    def takeBreath(self):
        print('I am breathing.....')


class Employee(Person):
    company = 'Honda'

    def __init__(self):
        # super().__init__()
        print('Initializing Employee... \n')

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print('I am an Employee so I am luckily breathing.... ')


class Programmer(Employee):
    company = 'Fiverr'

    def __init__(self):
        # super().__init__()
        print('Initializing Programmer...\n')

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        print('I am a Programmer so I am breathing++...')

# p = Person()
# p.takeBreath()
# e = Employee()
# e.takeBreath()


# pr = Programmer()
# pr.takeBreath()

p = Person()
p.takeBreath()
e =Employee()
e.takeBreath()

pr = Programmer()
pr.takeBreath()