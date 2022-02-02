from pydantic import BaseModel

class Model(BaseModel):
    login: str
    password: str