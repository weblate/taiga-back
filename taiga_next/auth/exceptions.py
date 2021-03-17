from fastapi import HTTPException, status

invalid_credentials = (
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="API.AUTH.INVALID_CREDENTIALS",
    headers={"WWW-Authenticate": "Bearer"},
)
