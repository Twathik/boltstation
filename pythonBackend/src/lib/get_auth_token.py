from fastapi import HTTPException, Header


def get_auth_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    # Extract the token (remove "Bearer " prefix)
    token = authorization.split(" ")[1] if " " in authorization else authorization
    return token
