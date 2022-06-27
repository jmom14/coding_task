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
    processed = list()
    headers = set()
    sort_column = 'D1'
    sort_index = 0

    for element in data:
        headers.update(element.keys())

    processed.append(sorted(headers, key=lambda x: (x[0], int(x[1: len(x)])) ))
    sort_index = processed[0].index(sort_column)

    for index in range(0, len(data)):
        curr = data[index]
        row = []
        
        for element in processed[0]:
            cell = curr.get(element) if curr.get(element) is not None else ""
            row.append(cell)
        processed.append(row)
    
    header = processed.pop(0)
    processed = sorted(processed, key=lambda x: x[sort_index])
    processed.insert(0, header)
    
    return processed


def write(data):
    with open('file.tsv', 'w', encoding='utf8', newline='') as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter='|')
        
        for item in data:
            tsv_writer.writerow(list(item))  


def execute(args):
    data = read(args)
    proccessed_data = process(data)
    write(proccessed_data)