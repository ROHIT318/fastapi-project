from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from dotenv import load_dotenv
import os
from app.schemas import EntrySchema
from app.db import Entry, create_db_and_tables, get_async_session

from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

load_dotenv('.\env_var.txt')
IMAGEKIT_PRIVATE_KEY = os.getenv("IMAGEKIT_PRIVATE_KEY")

fast_api = FastAPI()

@fast_api.get("/start_app")
def start_app():
    return {"msg": "App is up and running...."}


all_data_json = {
    1: {"fname": "Rohit", "lname": "Sharma", "location": "US"},
    2: {"fname": "Virat", "lname": "Kohli", "location": "PH"},
    3: {"fname": "Rahul", "lname": "Verma", "location": "AU"},
    4: {"fname": "Aditya", "lname": "Agrawal", "location": "BHR"},
    5: {"fname": "Amit", "lname": "Ashara", "location": "CHN"},
    6: {"fname": "Anil", "lname": "Singh", "location": "JAP"}
}

# Fetch all data from server
@fast_api.get('/get_all_entry/{limit}')
def get_all_entry(limit: int=None) -> dict():
    if limit:
        return list(all_data_json.values())[:limit]
    return all_data_json


# Fetch particular data from server
@fast_api.get('/get_particular_entry/{id}')
def get_particular_entry(id: int=None) -> dict():
    if id in all_data_json:
        return all_data_json[id]
    else:
        return HTTPException(status_code=404, detail="Error Happened !!")


# Create an entry in existing dictionary or JSON
@fast_api.post('/create_entry/')
def create_entry(data: EntrySchema):
    try: 
        all_data_json[len(all_data_json)+1] = {'fname': data.fname, 'lname': data.lname, 'location': data.location}
        return HTTPException(status_code=200, detail='Post Created Successfully')
    except:
        return HTTPException(status_code=404, detail='Post not Created Successfully')
    

# Delete existing entries
@fast_api.delete('/delete_entry/{id}')
def delete_entry(id: int=None):
    try:
        output = all_data_json.pop(id)
        return HTTPException(status_code=200, detail=output)
    except:
        return HTTPException(status_code=404, detail=f"Error Happened !!")
    
# File uploads
@fast_api.post('/file_upload/')
async def file_upload(file: UploadFile=File(...), caption:str=Form(''), session:AsyncSession=Depends(get_async_session)):
    pass

        