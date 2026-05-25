class Employee:
    def __init__(self, name, identifier, **kwargs):
        self.name = name
        self.identifier = identifier
        super().__init__(**kwargs)

    def get_info(self):
        return f"name {self.name}, ID {self.identifier}"

class Manager(Employee):
    def __init__(self, name, identifier, department, **kwargs):
        super().__init__(name, identifier, **kwargs)
        self.department = department

    def manage_project(self):
        print("символизирующим управление проектами.")

class Technician(Employee):
    def __init__(self, name, identifier, specialization, **kwargs):
        super().__init__(name, identifier, **kwargs)
        self.specialization = specialization

    def perform_maintenance(self):
        print("означающим выполнение технического обслуживания.")

class TechManager(Manager, Technician):
    def __init__(self, name, identifier, department, specialization, **kwargs):
        super().__init__(name=name, identifier=identifier,
                         department=department,
                         specialization=specialization, **kwargs)
        self.team = []
    def add_employee(self,identifier):
        self.team.append(identifier)

    def get_team_info(self):
        return print(f"Подчиненные сотрудники: {self.team}")



user = Employee(
    name="Dima",
    identifier="123")

print(user.get_info())

main_guy = TechManager(
    name="Vasya",
    identifier="124",
    department="IT",
    specialization="Software")
print(main_guy.get_info())

main_guy.add_employee(input("Введите номер сотрудника:"))
main_guy.get_team_info()