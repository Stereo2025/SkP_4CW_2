import requests

from api_classes.classes_for_processing import JobAPI


class HeadHunterAPI(JobAPI):
    """Работа с API платформы HeadHunter"""

    def __init__(self, keyword: str):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {
            'text': keyword,
            'area': 113,
            'only_with_salary': True,
            'page': 0,
            'per_page': 100,
            'search_field': 'name'
        }

    def get_vacancies(self):
        """Возвращает вакансии по заданному параметру"""

        response = requests.get(self.url, params=self.params)
        return response.json()['items']