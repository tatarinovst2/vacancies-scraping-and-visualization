"""Creates urls based on given attributes"""
import json
import requests

from bs4 import BeautifulSoup

from core.exceptions import IncorrectLocationException
from core.headers_generation import get_random_headers


class URLGenerator:  # pylint: disable=too-few-public-methods
    """Creates urls based on given attributes"""
    def __init__(self, specializations: list = None,
                 locations: list = None):
        self.locations = locations
        self.specializations = specializations
        self._root_url = "https://career.habr.com/vacancies?"
        self._root_page_soup = self._get_root_page_soup()

    def get_url(self, page: int = 1) -> str:
        """Generates url of given page with current URLGenerator's attributes"""
        url_parts = []
        if self.specializations:
            url_parts.append(self._get_specialization_part())

        if self.locations:
            url_parts.append(self._get_location_url_part())

        if page > 1:
            url_parts.append(f"page={page}")

        url_parts.append("type=all")

        return "".join([self._root_url, "&".join(url_parts), '/'])

    def _get_root_page_soup(self) -> BeautifulSoup:
        """Returns the first page for URLGenerator with current attributes"""
        response = requests.get(self._root_url, headers=get_random_headers(), timeout=15)
        return BeautifulSoup(response.text, 'html.parser')

    def _get_specialization_part(self) -> str:
        """Returns specialization part of url's query string"""
        if not self.specializations:
            return ""

        data = json.loads(self._root_page_soup.find('script', type='application/json').text)

        specializations = []
        specialization_codes = []

        for group in data["search"]["groups"]:
            specializations.extend(group["children"])

        for specialization_data in specializations:
            for specialization in self.specializations:
                if specialization in (specialization_data["id"],
                                      specialization_data["title"],
                                      specialization_data["translation"]):
                    specialization_codes.append(f"s[]={specialization_data['id']}")

        if not specialization_codes:
            return ""

        return "&".join(specialization_codes)

    def _get_location_url_part(self) -> str:
        """Returns location part of url's query string"""
        if not self.locations:
            return ""

        location_url_parts = []

        for location in self.locations:
            response = requests.get(
                f"https://career.habr.com/api/frontend/suggestions/locations?term={location}",
                headers=get_random_headers(),
                timeout=15)
            results = json.loads(response.text)

            if not results["list"]:
                raise IncorrectLocationException()

            location_code = results["list"][0]['value']

            location_url_parts.append(f"locations[]={location_code}")

        if not location_url_parts:
            return ""

        return "&".join(location_url_parts)
