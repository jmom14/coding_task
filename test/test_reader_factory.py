from unittest import TestCase
from ..app.reader_factory import ReaderFactory
from ..app.models import CSVReader, JSONReader, XMLReader


class TestReaderFactory(TestCase):

    def test_get_reader_with_csv_file(self):
        file = 'csv_data_1.csv'

        csv_reader = ReaderFactory().get_reader(file)

        assert isinstance(csv_reader, CSVReader)


    def test_get_reader_with_json_file(self):
        file = 'json_data.json'

        json_reader = ReaderFactory().get_reader(file)

        assert isinstance(json_reader, JSONReader)


    def test_get_reader_with_xml_file(self):
        file = 'xml_data.xml' 

        xml_reader = ReaderFactory.get_reader(file)

        assert isinstance(xml_reader, XMLReader)
