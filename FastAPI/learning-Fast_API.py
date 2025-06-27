from fastapi import FastAPI
import os 
import json


def load_data():
    with open('patients.json', "r") as f:
        data = json.load(f)
    
    return data


app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, World!"}


@app.get("/about")
def about():
    return {"message": "I will be the first Trillionare in the world!"}


@app.get("/view")
def view():
    data = load_data()

    return data
