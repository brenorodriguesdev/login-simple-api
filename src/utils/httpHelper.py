from fastapi import HTTPException


def unathorized(message):
    raise HTTPException(401, message)