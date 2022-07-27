class Employer:
    first_name = None
    last_name = None

    def __init__(self, first_name, last_name, age, job, salary, bonus=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.salary = salary
        self.bonus = bonus
        self.total_salary = salary + bonus

    def apply_bonus(self, bonus):
        self.bonus = bonus
        self.total_salary = self.salary + self.bonus

    def __str__(self):
        return (f'First name: {self.first_name}\n'
                f'Last name: {self.last_name}\n'
                f'Age: {self.age}\nJob: {self.job}\n'
                f'Salary: {self.salary}\n'
                f'Bonus: {self.bonus}\n'
                f'Total salary: {self.total_salary}')


