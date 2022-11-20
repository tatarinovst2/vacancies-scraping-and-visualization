# Vacancies scraping and visualization

A project for scraping https://career.habr.com for vacancies.

It allows to search vacancies using different options:
specializations, locations and qualifications.

## Test task code

To run example code which downloads and visualizes front-end vacancies in Moscow and Nizhny Novogorod make sure you are located in the project's directory in terminal or command line, then run:
```commandline
pip3 install -r requirements.txt
python3 main.py
```

## Usage

### Scraping

Import and initialize the scraper.

Then call `crawl()` and set parameters for scraping.

```py
from core.scraper import Scraper

if __name__ == "__main__":
    scrapper = Scraper()
    scrapper.crawl(locations=['Москва'],
                   specializations=['Фронтенд разработчик'],
                   qualifications=['Средний (Middle)'])
```

### Configuring crawling

| Parameter         | Description                                        | Possible values                                                                                                                              |
|:------------------|:---------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| `specializations` | Job types                                          | A `list` of `strings` corresponding to specializations on https://career.habr.com, for example `["Фронтенд разработчик", "Веб-разработчик"]` |
| `locations`       | Locations of the employer                          | A `list` of `strings`, for example `["Москва", "Санкт-Петербург"]`                                                                           |
| `qualifications`  | Required qualification                             | A `list` of `strings`, for example `["Средний (Middle)", "Старший (Senior)"]`                                                                |
| `timeout`         | Time required to wait before parsing the next page | A `float`, for example `1.0`                                                                                                                 |

### Expected results

Results in a json file stored in `\datasets\` folder.

```json
[
  {
        "id": 1000000000,
        "url": "https://career.habr.com/vacancies/1000000000",
        "title": "Frontend-разработчик",
        "specialization": "Фронтенд разработчик",
        "qualification": "Старший (Senior)",
        "location:": "Москва"
  },
  {
        "id": 1000000001,
        "url": "https://career.habr.com/vacancies/1000000001",
        "title": "Frontend-разработчик",
        "specialization": "Фронтенд разработчик",
        "qualification": "Старший (Senior)",
        "location:": "Санкт-Петербург"
  }
]
```

### Visualization

Vacancy parameters can be visualized  with `Visualizer`.

```py
from core.visualizer import visualize_latest_dataset

visualize_latest_dataset('qualification', bars=['Младший (Junior)',
                                                'Средний (Middle)',
                                                'Старший (Senior)'])
```

### Configuring visualization

`visualize_latest_dataset` – used to visualize the latest created dataset

| Parameter        | Description                                                      | Possible values                                                                      |
|:-----------------|:-----------------------------------------------------------------|:-------------------------------------------------------------------------------------|
| `data_name`      | Parameter to visualize                                           | A `string` that corresponds to field in the dataset, for example `"qualification"`   |
| `bars`           | Custom set bars that correspond to possible values of parameters | A `list` of `strings`, for example `["Младший (Junior)", "Средний (Middle)"]`        |

`visualize_dataset` – used to visualize the dataset based on given `file_name`

| Parameter   | Description                                                      | Possible values                                                                      |
|:------------|:-----------------------------------------------------------------|:-------------------------------------------------------------------------------------|
| `file_path` | Path to dataset                                                  | A `string` or a `Path` object that represents a path to the dataset                  |
| `data_name` | Parameter to visualize                                           | A `string` that corresponds to field in the dataset, for example `"qualification"`   |
| `bars`      | Custom set bars that correspond to possible values of parameters | A `list` of `strings`, for example `["Младший (Junior)", "Средний (Middle)"]`        |
