from  pydantic import BaseModel, Field
from typing import Annotated

class EntryCreate(BaseModel):
    id: Annotated[int, Field(strict=True)]
    fname: Annotated[str, Field(strict=True)]
    lname: Annotated[str, Field(strict=True)]
    dp_url: Annotated[str, Field(strict=True)]