import csv
from typing import List
from .reader_factory import ReaderFactory

def get_row(columns, current):
    row = []
    for cell in columns:
        row_temp = current.get(cell) if current.get(cell) is not None else ""
        row.append(row_temp)
    return row

def read(files: List[str]) -> List[dict]:
    read_data = []
    for file in files:
        reader = ReaderFactory.get_reader(file)
        read_data.extend(reader.read(file))
    return read_data


def process(data: List[dict]) -> List[dict]:
    processed = list()
    header = set()
    sort_column = 'D1'
    sort_index = 0

    for element in data:
        header.update(element.keys())

    sorted_header = (sorted(header, key=lambda x: (x[0], int(x[1: len(x)]))))

    sort_index = sorted_header.index(sort_column)

    for index in range(len(data)):
        curr = data[index]
        row = get_row(sorted_header, curr)
        
        if len(processed) == 0:
            processed.append(row)
        else:
            start = 0
            end = len(processed) - 1
            pos = 0
            
            while start <= end:
                mid = start + (end -start) // 2
                if processed[mid][sort_index] == data[index].get(sort_column):
                    processed.insert(max(0, mid + 1), row)
                    break
                    
                elif processed[mid][sort_index] >  data[index].get(sort_column):
                    pos = end = mid - 1

                else:
                    pos = start = mid + 1

                if start > end:
                    pos = start
                    processed.insert(max(0, pos), row)
                    break

    processed.insert(0, sorted_header)
    
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