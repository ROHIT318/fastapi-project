from fastapi import FastAPI, HTTPException, Depends
from dotenv import load_dotenv
import os
import app.db_connection
from app.db_connection import engine, SessionCreator, Entry
from app.schemas import EntryCreate
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


load_dotenv('.\env_var.txt')
IMAGEKIT_PRIVATE_KEY = os.getenv("IMAGEKIT_PRIVATE_KEY")

fast_api = FastAPI()
app.db_connection.Base.metadata.create_all(bind=engine)

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

def create_db_conn():
    db = SessionCreator()
    try:
        yield db
        db.commit()
    finally:
        db.close()

# Store the data in Database
@fast_api.post('/store_data')
def store_data(db: Session = Depends(create_db_conn)):
    for i in all_data_json:
        db.add(Entry(id=i, fname=all_data_json[i]['fname'], lname=all_data_json[i]['lname']))
    raise HTTPException(status_code=200, detail="Execution Successful !!")


# Fetch all data from server
@fast_api.get('/get_all_entry/{limit}')
def get_all_entry(limit: int=None, db: Session=Depends(create_db_conn)):
    if limit:
        # return list(all_data_json.values())[:limit]
        return db.query(Entry).limit(limit).all()   
    return all_data_json


# Fetch particular data from server
@fast_api.get('/get_particular_entry/{id}')
def get_particular_entry(id: int=None, db: Session=Depends(create_db_conn)):
    product = db.query(Entry).filter(Entry.id == id).first()
    if product is not None:
        return product
    else:
        raise HTTPException(status_code=404, detail="Product Not Found !!")


# Create an entry in existing dictionary or JSON
@fast_api.post('/create_entry/')
def create_entry(data: EntryCreate, db: Session = Depends(create_db_conn)):
    try: 
    # all_data_json[len(all_data_json)+1] = {'fname': data.fname, 'lname': data.lname}
        db.add(Entry(
            id = data.id, 
            fname = data.fname,
            lname = data.lname,
            dp_url = data.dp_url
        ))
    except IntegrityError as e:
        raise HTTPException(status_code=404, detail='Unique id taken !!')
    except:
        raise HTTPException(status_code=404, detail='Entry not Created Successfully !!')
    

# Create an entry in existing dictionary or JSON
@fast_api.post('/update_entry/{id}')
def update_entry(id: int = None, fname: str = None, lname: str = None, dp_url: str = None, 
                 db: Session = Depends(create_db_conn)):
    try:
        entry = db.query(Entry).filter(Entry.id == id).first()
        if entry:
            db.query(Entry).filter(Entry.id == id).update({
                Entry.fname: fname, 
                Entry.lname: lname, 
                Entry.dp_url: dp_url
            })
            return {"msg": "Entry updated Successfully !!"}
        raise HTTPException(status_code=404, detail="Entry id doesn't exists !!")
    except:
        raise HTTPException(status_code=404, detail='Entry not updated Successfully !!')
    

# Delete existing entries
@fast_api.delete('/delete_entry/{id}')
def delete_entry(id: int=None, db: Session = Depends(create_db_conn)):
    try:
        db.query(Entry).filter(Entry.id == id).delete()
        return {"msg": "Entry removed Successfully !!"}
    except:
        raise HTTPException(status_code=404, detail="Error Happened !!")
    
# Drop a particular table from database
@fast_api.delete('/drop_table/{tbl_name}')
def delete_table(tbl_name: str = None):
    try:  
        tbl_obj = getattr(app.db_connection, tbl_name)
        tbl_obj.metadata.drop_all(bind=engine)   
        return {"msg": "Dropped table {tbl_name}"}
    except:
        raise HTTPException(status_code=404, detail="Error Happened !!")