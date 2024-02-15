from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends,HTTPException, status
from . import schemas,database,models
from pydantic import BaseModel,EmailStr
from typing import Optional
from sqlalchemy.orm import Session

# class TokenData(BaseModel):
#       id:Optional[str] = None

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict()):
    to_encode=data.copy()
    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encode_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

def verify_access_token(token:str,credentials_exception):
    
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id:str = payload.get('user_id')
        if id is None:
            raise credentials_exception
        token_data =schemas.TokenData(id=id)
        print(token_data)
    except JWTError:
        raise credentials_exception
    #user = get_user(fake_users_db, username=token_data.username)
    # if user is None:
    #     raise credentials_exception
    return token_data


def get_current_user(token:str=Depends(oauth2_scheme),db : Session=Depends(database.get_db)):
    credentials_exception=HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="could not validate",
                                        headers={"www-Authenticated":"Bearer"})

    token = verify_access_token(token,credentials_exception)
    print(token)
    #user=db.query(models.users).filter(models.users.id==token.id).first()
    return token