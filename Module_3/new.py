from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str):
        self.name = name
        self.workplace = None

    @abstractmethod
    def calculate_salary(self):
        raise NotImplementedError("Метод calculate_salary нужно реализовать в подклассе")

    def display_info(self):
        status = self.workplace if self.workplace else "В поиске работы"
        print(f"Сотрудник: {self.name} | Компания: {status}")

class Developer(Employee):
    def __init__(self, name: str, experience_years: int, base_salary: int):
        super().__init__(name)
        self.experience_years = experience_years
        self._base_salary = base_salary
        self._bonus = 0
        self.__api_key = "Secret_123"  

    def calculate_salary(self):
        return self._base_salary + self._bonus

    @property
    def api_key(self):
        print("Получение API ключа")
        return self.__api_key

    @api_key.setter
    def api_key(self, new_key):
        if new_key.startswith("SECRET"):
            print("Rename API разрешен")
            self.__api_key = new_key
        else:
            print("Rename API запрещен")

class TeamLead(Developer):
    def __init__(self, name: str, experience_years: int, base_salary: int):
        super().__init__(name, experience_years, base_salary)
        self._bonus = 50000

class Designer(Employee):
    def calculate_salary(self):
        return 50000  

class Company:
    def __init__(self, name: str):
        self.name = name
        self.staff = []

    def hire(self, employee: Employee):
        self.staff.append(employee)
        employee.workplace = self.name
        print(f"[{self.name}] Нанят новый сотрудник: {employee.name}")

    def get_total_employees(self):
        return len(self.staff)

    def change_name(self, new_name: str):
        print(f"\n--- Компания {self.name} меняет название на {new_name}! ---")
        self.name = new_name
        for emp in self.staff:
            emp.workplace = new_name

tech_corp = Company("TechCorp")

dev = Developer("Алексей", 3, 100000)
lead = TeamLead("Дмитрий", 7, 150000)
design = Designer("Анна")

tech_corp.hire(dev)
tech_corp.hire(lead)
tech_corp.hire(design)

print(f"Всего сотрудников в компании: {tech_corp.get_total_employees()}")
print(f"Зарплата лида: {lead.calculate_salary()}")

dev.api_key = "HACKED_123"
dev.api_key = "SECRET_NEW_777"

tech_corp.change_name("MegaTech")
dev.display_info()
