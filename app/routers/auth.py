from .. import models,schemas,utils,database,oauth2
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import engine, get_db
from typing import Optional,List
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
router=APIRouter(tags=["Authentication"])

@router.post('/login',response_model=schemas.token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=db.query(models.users).filter(models.users.email ==user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="credentials invalid")
    
    if not utils.verify(user_credentials.password,user.password):
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="credentials invalid")
   
    access_token=oauth2.create_access_token(data={"user_id":user.id})
    print(access_token)
    
    return {"acess_token": access_token,"token_type":"bearer"}



        
