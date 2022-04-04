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


def auth_required(handler):
    async def wrapper(*args, **kwargs):
        return await handler(*args, is_auth=Depends(is_authenticated), **kwargs)

    import inspect

    wrapper.__signature__ = inspect.Signature(
        parameters=[
            *inspect.signature(handler).parameters.values(),
            *filter(
                lambda p: p.kind
                not in (
                    inspect.Parameter.VAR_POSITIONAL,
                    inspect.Parameter.VAR_KEYWORD,
                ),
                inspect.signature(wrapper).parameters.values(),
            ),
        ],
        return_annotation=inspect.signature(handler).return_annotation,
    )

    return wrapper
