class Employee:
    company = 'Google'

    @staticmethod
    def greet():
        print('Good morning, Sir')
        
    @staticmethod
    def time():
        print('Time is 9 AM in the morning.')    

    def getSalary(self):
        print(
            f"Salary for this employee working in {self.company} is {self.salary}k")


erus = Employee()
erus.salary = 100
erus.getSalary()
erus.greet()
erus.time()
