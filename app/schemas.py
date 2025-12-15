from  pydantic import BaseModel

class EntrySchema(BaseModel):
    id: int
    fname: str
    lname: str
    location: str