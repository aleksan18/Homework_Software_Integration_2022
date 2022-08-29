import json
import yaml
txtData = open('birds.txt','r')
print('TXT')
print(txtData.read())
txtData.close()
jsonData = json.load(open('birds.json','r'))
print('JSON')
print(jsonData)
with open('birds.yaml','r') as stream:
    try:
        print('YAML')
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)
import csv
with open('birds.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    print('CSV')
    for row in spamreader:
        print(', '.join(row))
from bs4 import BeautifulSoup
with open('birds.xml', 'r') as f:
    data = f.read()
    Bs_data = BeautifulSoup(data, "xml")
    print('XML')
    print(Bs_data)