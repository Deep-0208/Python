class Employee:
    def __init__(self, salary):
        self.salary = salary
        self.incremnet = 0.1

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.incremnet)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.incremnet = (new_salary - self.salary)/self.salary

    def display(self):
        print(f"Current Salary: {self.salary}")
        print(f"Increment: {self.incremnet * 100:.2f}%")
        print(f"Salary After Increment: {self.salaryAfterIncrement}")


emp = Employee(10000)
emp.display()
