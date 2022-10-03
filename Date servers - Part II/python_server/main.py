from datetime import datetime
from fastapi import FastAPI
app = FastAPI()
import datetime
import requests
@app.get("/timestamp",responses={
    200:{"description":"Gives a timestamp of the current time in ISO format"}
})
def _():
    print(datetime.datetime.utcnow())
    return {"timestamp": datetime.datetime.utcnow().isoformat()[:-3]+'Z',"format":'ISO8601'}

@app.get("/requestTimestamp",responses={
    200:{"description":"Requests and returns a timestamp from a node server in ISO format"}
})
def _():
    response = requests.get(url ='http://localhost:8000/timestamp')
    return response.json()