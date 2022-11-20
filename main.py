"""Main"""
from scraper import Scraper
from visualizer import visualize_latest_dataset


if __name__ == "__main__":
    scrapper = Scraper()
    scrapper.crawl(locations=['Москва',
                              'Московская область',
                              'Нижний Новгород',
                              'Нижегородская область'],
                   specializations=['Фронтенд разработчик'],
                   qualifications=['Младший (Junior)',
                                   'Средний (Middle)',
                                   'Старший (Senior)'])
    visualize_latest_dataset('qualification', bars=['Младший (Junior)',
                                                    'Средний (Middle)',
                                                    'Старший (Senior)'])
