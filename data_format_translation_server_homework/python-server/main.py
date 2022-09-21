from fastapi import FastAPI
from bs4 import BeautifulSoup
import csv
import yaml
import json
import xmltodict
app = FastAPI()
xmlParser = BeautifulSoup()
@app.get("/csvRoute")
def _():
    with open('birds.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        print('CSV')

        for row in spamreader:   
            a =', '.join(row)
        print(a)
    return {"ReturnData":a}

@app.get("/yamlRoute")
def _():
    with open('birds.yaml','r') as stream:
        try:
            print('YAML')
            returnValues = yaml.safe_load(stream)
            print(returnValues)
        except yaml.YAMLError as exc:
            print(exc)
            return {"error":FALSE}
    return {"ReturnData":returnValues}

@app.get("/xmlRoute")
def _():

    with open('birds.xml', 'r') as f:
        data_dict = xmltodict.parse(f.read())
        json_data = json.dumps(data_dict)
        print('XML')
        print(json_data)
        data= json.loads(json_data)
    return {"ReturnData":data}