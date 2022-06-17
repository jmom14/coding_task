
## CODING TEST

This project read from xml, csv json files, process the data then finally writes the resulst in 'file.tsv'


## How to install

```
python3 -m pip install -r requirements.txt
```


## Run Examples

```
python3 main.py --files 'xml_data.xml'
python3 main.py --files 'csv_data_1.csv, csv_data_1.csv'
python3 main.py --files 'csv_data_1.csv, csv_data_1.csv, xml_data.xml, json_data.json'
```


## How to run tests

```
python3 -m pytest
```