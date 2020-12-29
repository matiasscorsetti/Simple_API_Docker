from fastapi import FastAPI
from pydantic import BaseModel
from random import choice
from json import load
from os import environ

class ProcessConfig(BaseModel):
    file_name: str

dir_config = "dir_config/"

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Simple API with Docker"}

@app.post("/processrandom/")
async def process(process_config: ProcessConfig):
    '''
    perform a random process according to a configuration file and an environment variable
    '''

    # access environment variable values
    site_name = environ['SITENAME']

    # read configuration file
    config_file_path = dir_config + process_config.file_name

    try:
        with open(config_file_path, 'r', encoding='latin-1') as f:
            config = load(f)
        config_file_loaded = True

    except FileNotFoundError:
        config = "configuration file not found"
        config_file_loaded = False

    # generate a random process result
    result = choice(["ok", "fail"])

    return {"name": site_name,
            "config_file_loaded": config_file_loaded,
            "config": config,
            "result": result,
            }