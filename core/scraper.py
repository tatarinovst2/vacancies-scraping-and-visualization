"""Finds urls with URLGenerator and parses them with Parser, then saves results"""
from pathlib import Path

import json
import time
import datetime

from page_parser import PageParser
from url_generator import URLGenerator


class Scraper:  # pylint: disable=too-few-public-methods
    """Finds urls with URLGenerator and parses them with Parser, then saves results"""
    def __init__(self):
        self._vacancy_data = []

    def crawl(self, specializations: list = None,
              locations: list = None,
              qualifications: list = None,
              timeout: float = 1.0) -> None:
        """Finds """
        self._vacancy_data = []
        url_generator = URLGenerator(specializations=specializations, locations=locations)
        page = 1

        while True:
            parser = PageParser(url=url_generator.get_url(page), qualifications=qualifications)

            if parser.get_parsed_data():
                self._vacancy_data.extend(parser.get_parsed_data())

            page += 1
            time.sleep(timeout)

            if parser.is_last_page(expected_results_amount=25):
                break

        self._dump_results()

    def _dump_results(self) -> None:
        """Saves results to dataset in datasets folder"""
        if not Path(Path(__file__).parent / 'datasets').exists():
            Path(Path(__file__).parent / 'datasets').mkdir()

        with (Path(__file__).parent / 'datasets' / f'{datetime.datetime.now()}_dataset.json').\
                open("w", encoding='utf-8') as file:
            json.dump(self._vacancy_data, file, sort_keys=False,
                      indent=4, ensure_ascii=False, separators=(',', ': '))
