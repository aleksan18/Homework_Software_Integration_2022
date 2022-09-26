from datetime import datetime
from fastapi import FastAPI
app = FastAPI()
import datetime

@app.get("/timestamp")
def _():
    print(datetime.datetime.utcnow())
    return {"timestamp": datetime.datetime.utcnow().isoformat()[:-3]+'Z',"format":'ISO8601'}