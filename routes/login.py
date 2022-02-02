from fastapi import APIRouter
from models import signIn, signUp
from controllers import signUpController, signInController

router = APIRouter()

@router.post("/signIn/", tags=["login"])
async def signIn(signInModel: signIn.Model):
    return signInController.handle(signInModel)

@router.post("/signUp/", tags=["login"])
async def signUp(signUpModel: signUp.Model):
    return signUpController.handle(signUpModel)