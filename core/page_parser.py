"""Parses the search page for vacancies"""
import json
import requests

from bs4 import BeautifulSoup

from core.headers_generation import get_random_headers


class PageParser:
    """Parses the search page for vacancies"""
    def __init__(self, url: str, **restrictions):
        self._url = url
        self._vacancies_data = []
        self._last_vacancies_page_count = 0
        self._parse(**restrictions)

    def _parse(self, **restrictions) -> None:
        """Parses the page's html and stores the data that was found"""
        response = requests.get(self._url, headers=get_random_headers(), timeout=15)
        page_bs = BeautifulSoup(response.text, 'html.parser')

        data = json.loads(page_bs.find('script', type='application/json').text)

        vacancies_list = data["vacancies"]["list"]
        self._last_vacancies_page_count = len(vacancies_list)

        for vacancy_dict in vacancies_list:
            vacancy_data = {"title": vacancy_dict["title"],
                            "specialization": vacancy_dict["divisions"][0]["title"]
                            if vacancy_dict.get("divisions") else None,
                            "qualification": vacancy_dict["salaryQualification"]['title']
                            if vacancy_dict.get("salaryQualification") else None,
                            "location:": vacancy_dict["locations"][0]["title"]
                            if vacancy_dict.get("locations") else None}

            if restrictions.get("qualifications"):
                if vacancy_data["qualification"] not in restrictions["qualifications"]:
                    continue

            self._vacancies_data.append(vacancy_data)

    def get_parsed_data(self) -> list:
        """Returns the parsed data"""
        return self._vacancies_data

    def is_last_page(self, expected_results_amount: int) -> bool:
        """Checks whether the current page is the last one and scrapping should be stopped"""
        return self._last_vacancies_page_count < expected_results_amount
