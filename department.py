class Department:
    departments = {}

    def __init__(self, name=None, users=None):
        if name is None and users is None:
            return
        if name in self.departments.keys():
            self.departments[name] = list(set(self.departments[name] + users))
        else:
            self.departments[name] = users

    def display_employers(self, name):
        user_list = [f"{user.first_name} {user.last_name}" for user in self.departments[name]]
        print(f"User list of {name} department:", ", ".join(user_list))

    def display_departments(self):
        print("Departments list:", ", ".join(self.departments.keys()))

    def remove_department(self, name):
        del self.departments[name]

    def remove_employer(self, department, employer):
        if employer in self.departments[department]:
            self.departments[department].remove(employer)
