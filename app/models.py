from abc import ABC, abstractmethod
from typing import List
import csv
import json
import xmltodict


class IReader(ABC):

    @abstractmethod
    def read(self, file: str) -> List[dict]:
        pass


class CSVReader(IReader):
    
    def read(self, file: str) -> List[dict]:
        csv_data = []
        data = open(file)

        reader = csv.DictReader(data)
        for row in reader:
            csv_data.append(row)

        data.close()
        return csv_data


class JSONReader(IReader):
    def read(self, file: str) -> List[dict]:
        json_data = open(file)

        data = json.load(json_data)
        
        json_data.close()

        if 'fields' in data:
            return data['fields']
        
        return [{}]



class XMLReader(IReader):

    def postprocessor(path, key, value, l):
        print(key, value)
        return key, value
    
    def read(self, file: str) -> List[dict]:
        
        data = open(file)
        xml_data = []
        parse_data = xmltodict.parse(xml_input=data.read())
        
        try:
            objects = parse_data['root']['objects']
        except KeyError:
            raise Exception("Wrong format")

        for values in objects.values():
            item = {}
            for element in values:
                key = element['@name']
                value = element['value']
                item[key] = value
            xml_data.append(item)


        data.close()        
        return xml_data


