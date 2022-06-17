from unittest import TestCase
from app.execute import execute, read, process, write
from os.path import exists
import os

valid_sample_array = [
    {
      "D1": "a",
      "D3": "a",
      "D2": "a",
      "M1": 0,
      "M2": 0,
      "M4": 0,
      "M3": 0
    },
    {
      "D1": "b",
      "D3": "b",
      "D2": "b",
      "M1": 1,
      "M2": 1,
      "M4": 1,
      "M3": 1
    },
    {
      "D1": "c",
      "D3": "c",
      "D2": "c",
      "M1": 2,
      "M2": 2,
      "M4": 2,
      "M3": 2
    }
  ]

class TestExecute(TestCase):

    def test_execute(self):
        
        if exists("file.tsv"):
            os.remove("file.tsv")
        
        sample_args = ['json_data.json']
        execute(sample_args)
        assert exists("file.tsv")

        os.remove("file.tsv")

    
    def test_read(self):

        sample_args = ["json_data.json"]
        read_data = read(sample_args)
        assert valid_sample_array == read_data


    def test_proccess(self):

        processed_data = process(valid_sample_array)
        assert processed_data == valid_sample_array


    def test_write(self):

        if exists("file.tsv"):
            os.remove("file.tsv")

        write(valid_sample_array)
        assert exists("file.tsv")
        
        os.remove("file.tsv")