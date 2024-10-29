import sys
from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def root():
    return {"message" : 'hello world'}
items = ['맥','애플','아이폰','갤럭시']
@app.get('/home/{hell}')
def home(hell):
    return {'message' : int(hell)}

@app.get('/items')
def read_items(skip:int = 0, limit:int = 10):
    return items[skip:skip+limit]
