import datetime
from pydantic import BaseModel

class Model(BaseModel):
    login: str
    password: str
    name: str
    birthDate: datetime.datetime