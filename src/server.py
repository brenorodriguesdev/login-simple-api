from fastapi import FastAPI
from routes import login

app = FastAPI()

app.include_router(login.router)