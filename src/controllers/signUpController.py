import bcrypt
from repositories import loginRepository

def handle(signUpModel):
    passwordHash = bcrypt.hashpw(signUpModel.password.encode("utf-8"), bcrypt.gensalt())
    signUpModel.password = passwordHash
    loginRepository.insert({ 
        "login": signUpModel.login,
        "password": signUpModel.password,
        "name": signUpModel.name,
        "birthDate": signUpModel.birthDate
    })
    return signUpModel