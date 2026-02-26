from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.auth import verify_token

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):

    token = credentials.credentials

    user_data = verify_token(token)

    return user_data

def require_role(required_role: str):

    def role_checker(user = Depends(get_current_user)):

        if user["role"] != required_role:
            raise HTTPException(status_code=403, detail="Forbidden")

        return user

    return role_checker