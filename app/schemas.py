from pydantic import BaseModel,EmailStr
from pydantic.types import conint
from datetime import datetime
from typing import Optional

class UserOut(BaseModel):
    id:int    
    email:EmailStr
    

class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    # created_at:datetime
    # id:int
    # owner_id:int
    # owner:UserOut

class Cpost(Post):
    created_at:datetime
    id:int
    owner_id:int
    owner:UserOut

class Postout(BaseModel):
    Post:Cpost
    votes:int

class Usercreate(BaseModel):
    email:EmailStr
    password:str
    

class UserLogin(BaseModel):
    email:EmailStr
    password:str
    
   
    
class Token(BaseModel):
    acess_token:str
    token_type:str



class TokenData(BaseModel):
      id:Optional[int] = None
      
      
class token(BaseModel):
    acess_token:str
    token_type:str

class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)
    #a