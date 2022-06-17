import csv
from typing import List
from .reader_factory import ReaderFactory


def read(files: List[str]) -> List[dict]:
    read_data = []
    for file in files:
        reader = ReaderFactory.get_reader(file)
        read_data.extend(reader.read(file))
    return read_data


def process(data: List[dict]) -> List[dict]:
    return data


def write(data: List[dict]):
    with open('file.tsv', 'w', encoding='utf8', newline='') as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter='|')
        tsv_writer.writerow(list(data[0].keys()))
        
        for item in data:
            tsv_writer.writerow(list(item.values()))  


def execute(args):
    data = read(args)
    proccessed_data = process(data)
    write(proccessed_data)