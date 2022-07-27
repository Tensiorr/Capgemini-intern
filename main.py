from employer import Employer
from department import Department


def create_employer(first_name, last_name, age, job, salary, bonus=0):
    return Employer(first_name, last_name, age, job, salary, bonus)


def remove_employer(department, employer):
    company.remove_employer(department, employer)


def apply_bonus(employer, bonus):
    employer.apply_bonus(bonus)


def add_department(name, users):
    if type(users) is list:
        return Department(name, users)
    else:
        return Department(name, [users])


def remove_department(name):
    company.remove_department(name)


def apply_bonus_in_department(department, bonus):
    for user in company.departments[department]:
        apply_bonus(user, bonus)


def save_to_file(employer):
    with open(f'{employer.first_name}_{employer.last_name}.txt', 'w') as text_file:
        text_file.write(employer.__str__())

if __name__ == '__main__':
    company = Department()

    emp_a = create_employer("Robert", "Lewandowski", 33, "Footballer", 8000, 0)
    emp_b = create_employer("Zygmunt", "Chajzer", 68, "Actor", 4500, 0)
    emp_c = create_employer("Dorota", "Wellman", 59, "Actor", 4000, 200)
    emp_d = create_employer("Adrian", "Nowak", 33, "Influencer", 5000, 500)


    add_department("IT", [emp_b, emp_c])
    add_department("Accountancy", [emp_b, emp_d])
    add_department("Other", emp_a)

    company.display_employers("IT")
    company.display_employers("Accountancy")
    company.display_employers("Other")

    company.display_departments()

    remove_department("Accountancy")

    company.display_departments()

    print(emp_a)
    apply_bonus_in_department("Other", 100)
    print(emp_a)

    save_to_file(emp_d)
