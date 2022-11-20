"""Creates charts for results using matplotlib"""
from pathlib import Path
import json

import matplotlib.pyplot as plt

from core.exceptions import DatasetDirectoryEmpty


def visualize_dataset(file_path: Path | str, data_name: str, bars: list[str] = None) -> None:
    """Creates histogram for given data aspect"""
    data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        vacancies = json.load(file)

    for vacancy in vacancies:
        if vacancy.get(data_name):
            data.append(vacancy.get(data_name))

    if bars:
        data_counts = {x: data.count(x) for x in bars}
        column_names, counts = zip(*data_counts.items())
        plt.bar(column_names, counts)
    else:
        plt.hist(data)

    plt.show()


def visualize_latest_dataset(data_name: str, bars: list[str] = None) -> None:
    """Find the latest creates dataset and creates histogram for given data aspect"""
    files = (Path(__file__).parent / 'datasets').glob("*.json")

    if not files:
        raise DatasetDirectoryEmpty()

    latest_file_path = max(files, key=lambda x: x.stat().st_ctime)
    visualize_dataset(latest_file_path, data_name, bars=bars)
