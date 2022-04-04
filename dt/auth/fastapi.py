import os
import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

base_auth = HTTPBasic()


def is_authenticated(credentials: HTTPBasicCredentials = Depends(base_auth)) -> bool:
    username = secrets.compare_digest(credentials.username, os.environ["API_USERNAME"])
    password = secrets.compare_digest(credentials.password, os.environ["API_PASSWORD"])

    if not (username and password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True
