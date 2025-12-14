from  pydantic import BaseModel

class EntrySchema(BaseModel):
    fname: str
    lname: str
    location: str