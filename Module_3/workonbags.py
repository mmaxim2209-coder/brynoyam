from abc import ABC, abstractmethod

class Employee(ABC):
    company_name = "TechCorp"
    total_employees = 0
    name_employee = []

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name
        print(f"Компания {cls.company_name} изменила название на: {new_name}")

    def __init__(self, name: str):
        self.name = name
        type(self).total_employees += 1
        type(self).name_employee.append(name)

    @abstractmethod
    def calculate_salary(self):
        raise NotImplementedError("Метод calculate_salary нужно реализовать в подклассе")

    def display_info(self):
        print(f"Сотрудник: {self.name}, Компания: {self.company_name}")

print(f"Всего сотрудников: {Employee.total_employees}")
print(f"Название компании: {Employee.company_name}")
print(f"Имена сотрудников: {Employee.name_employee}")
print("-" * 30)


class Developer(Employee):
    total_employees = 0  # Счетчик для разработчиков
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
    total_employees = 0  # Счетчик для тимлидов
    def __init__(self, name: str, experience_years: int, base_salary: int):
        super().__init__(name, experience_years, base_salary)
        self._bonus = 50000

class Designer(Employee):
    total_employees = 0  # Счетчик для дизайнеров
    def calculate_salary(self):
        return 50000  

          # 1. Создаем правильных сотрудников
dev = Developer("Алексей", 3, 100000)
lead = TeamLead("Дмитрий", 7, 150000)
design = Designer("Анна")

# 2. Проверяем, что счетчики сработали отдельно для каждого класса
print(f"Разработчиков: {Developer.total_employees}")  # Выведет: 1
print(f"Тимлидов: {TeamLead.total_employees}")        # Выведет: 1
print(f"Дизайнеров: {Designer.total_employees}")       # Выведет: 1

# 3. Проверяем расчет зарплаты Тимлида (с учетом бонуса 50000)
print(f"Зарплата лида: {lead.calculate_salary()}")     # Выведет: 200000

# 4. Проверяем работу приватного ключа и сеттера
dev.api_key = "HACKED_123"      # Выведет: Rename API запрещен
dev.api_key = "SECRET_NEW_777"  # Выведет: Rename API разрешен
print(dev.api_key)              # Получение API ключа -> SECRET_NEW_777  
