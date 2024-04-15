from .. import models,schemas,utils
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import engine, get_db
from typing import Optional,List

router=APIRouter(prefix="/users",tags=["User"])

@router.get("/")   
def get_users(db: Session = Depends(get_db)):
    users=db.query(models.users).all()
    #print(users)
    if not users:
        return {"status":"Not a single users in database"}
    return {"status":users} 

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut) 
def create_user(user:schemas.Usercreate,db: Session = Depends(get_db)):
     hash_password=utils.hash(user.password)
     user.password=hash_password
     newuser=models.users(**user.dict())
    
    
     db.add(newuser)
     db.commit()
     db.refresh(newuser)
    
     return newuser
    
@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id:int,response:Response,db: Session = Depends(get_db)):
    users=db.query(models.users).filter(models.users.id ==id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found bey")
    return users