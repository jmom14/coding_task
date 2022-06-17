import os
from .models import CSVReader, JSONReader, XMLReader


class ReaderFactory():

    @staticmethod
    def get_reader(file):
        file_name, file_extension = os.path.splitext(file)
        if file_extension == '.csv':
            return CSVReader()
        if file_extension == '.json':
            return JSONReader()
        if file_extension == '.xml':
            return XMLReader()
