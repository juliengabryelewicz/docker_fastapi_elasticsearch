from typing import Union
from elasticsearch import Elasticsearch
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
es = Elasticsearch(["http://elasticsearch:9200/"])

@app.get("/")
def hello_world():
    return {"Hello": "World"}

@app.get("/elasticsearch/info")
def elasticsearch_details():
    return JSONResponse(dict(es.info()))

@app.get("/elasticsearch/health")
def elasticsearch_health():
    return JSONResponse(dict(es.cluster.health()))