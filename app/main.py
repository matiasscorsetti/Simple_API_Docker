from fastapi import FastAPI
from pydantic import BaseModel
from random import choice
from json import load
from os import environ

class ProcessFile(BaseModel):
    '''
    the file to process
    '''
    file_name: str # name of the file to process

app = FastAPI()

# access environment variable values
site_name = environ['SITENAME']

# read configuration file
try:
    with open("config_file.json", 'r', encoding='latin-1') as f:
        config = load(f)

except FileNotFoundError:
    config = "configuration file not found"


@app.get("/")
async def root():
    '''
    root path with site name
    '''

    # access environment variable values
    return {"message": "Simple API with Docker to site: {}".format(site_name)}


@app.post("/processrandom/")
async def process(process_file: ProcessFile):
    '''
    read a file from the "data/" folder and perform a random process according to a configuration file and environment variable
    '''

    # read file from data folder
    process_file_name = process_file.file_name
    process_file_name_path = "data/" + process_file_name
    try:
        with open(process_file_name_path, 'r', encoding='latin-1') as f:
            data = load(f)

    except FileNotFoundError:
        data = "data file not found"

    # generate a random process result
    result = choice(["ok", "fail"])

    return {"name": site_name,
            "config": config,
            "data": data,
            "result": result,
            }