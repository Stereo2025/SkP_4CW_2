import requests

from api_classes.classes_for_processing import JobAPI
from utils.variables import API_KEY


class SuperJobAPI(JobAPI):
    """Работа с API платформы SuperJob"""

    def __init__(self, keyword: str):
        self.url = 'https://api.superjob.ru/2.0/vacancies'
        self.params = {
            'keyword': keyword,
            'countries': 1,
            'count': 100,
            'page': 0
        }

    def get_vacancies(self):
        """Возвращает вакансии по заданному параметру"""
        headers = {
            'X-Api-App-Id': API_KEY
        }
        response = requests.get(self.url, headers=headers, params=self.params)
        return response.json()['objects']