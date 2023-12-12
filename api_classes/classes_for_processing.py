from abc import ABC, abstractmethod


class UrlError(Exception):
    """Класс ошибки в URL адресе"""
    def __init__(self, msg):
        super.__init__(msg)


class JobAPI(ABC):
    """Работа с API платформ по поиску работы"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class Vacancy:
    """Создания экземпляров вакансий и работы с ними"""
    __slots__ = {'name', 'url', 'salary', 'requirement'}

    def __init__(self, name: str, url: str, salary: int, requirement: str):
        self.name = name
        if not isinstance(self.name, str):
            raise TypeError("Название вакансии должно быть типа 'str'")
        self.url = url
        if self.url[:8] != 'https://':
            raise UrlError("Ссылка должна начинаться с https://")
        self.salary = salary
        if self.salary is None:
            raise AttributeError('Поле не может быть пустым')
        self.requirement = requirement
        if self.requirement is None:
            raise AttributeError('Поле не может быть пустым')

    def __str__(self):
        return f'Название вакансии - {self.name}\n' \
               f'Ссылка - {self.url}\n' \
               f'З/п до {self.salary} RUR\n' \
               f'Требования - {self.requirement}\n'

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary