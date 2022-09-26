from datetime import datetime
from fastapi import FastAPI
app = FastAPI()
import datetime
import requests
@app.get("/timestamp")
def _():
    print(datetime.datetime.utcnow())
    return {"timestamp": datetime.datetime.utcnow().isoformat()[:-3]+'Z',"format":'ISO8601'}

@app.get("/requestTimestamp")
def _():
    response = requests.get(url ='http://localhost:8000/timestamp')
    return response.json()