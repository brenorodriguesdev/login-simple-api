import jwt
import bcrypt

from repositories import loginRepository
from utils import httpHelper

def handle(signInModel):
    print(signInModel.login)
    login = loginRepository.findByLogin(signInModel.login)
    if login == None:
        return httpHelper.unathorized("Login or password are incorrect!")
    if not bcrypt.checkpw(signInModel.password.encode("utf-8"), login["password"]):
        return httpHelper.unathorized("Login or password are incorrect!")
    return jwt.encode({ "id": str(login["_id"]), "login": login["login"]  }, "secret", algorithm="HS256")