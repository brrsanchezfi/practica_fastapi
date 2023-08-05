from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Text

class Obra(BaseModel):
    id:Optional[str]
    autor:str
    title:str
    year:datetime
    gender:str
    abstract:Text
    
