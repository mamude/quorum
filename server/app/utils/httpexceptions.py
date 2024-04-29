from fastapi import HTTPException


def not_found(status_code: int = 404, message: str = None):
    raise HTTPException(status_code=status_code, detail=message)
