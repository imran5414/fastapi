from fastapi import FastAPI,Response,status,HTTPException,Depends
from pydantic import BaseModel

from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
from . database import engine,SessionLocal
from sqlalchemy.orm import Session
from . import models,utils
from . import schemas
from . database import get_db
from .routers import posts,users,auth,votes
from fastapi.middleware.cors import CORSMiddleware



models.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)



# app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

@app.get("/")
def root():
    return {"mssg":"hello worldsss"}


    



# try:
#     conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='root',cursor_factory=RealDictCursor)
#     corsor=conn.cursor()
#     print("connection successful")
# except Exception as error:
#     print("connection failed")
#     print("eroor was",error)



l = [  
    {"name":"RRR","adress":"HYD","id":1}, {"name":"XXX","address":"BAN","id":2},
    {"name":"imu","address":"pun","id":3},{"name":"sunny","address":"MUM","id":4}


]

def post(id):
    for x in l:
        if x["id"]==id:
            return x
        
    
def getindex(id):
     for x,y in enumerate(l):
         if y ["id"]==id:
             return x
# @app.post("/poster")
# def rec(post:Post):
#     data=post.dict()
#     l2=[]
#     # for x in l:
#     #     l2.append(x["id"])
#     if data["id"]==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Enter id field")
#     elif data["id"] in l2:
#         x=data["id"]
#         raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,detail=f"id with num {x} already exist")
#     print(data["id"])
#     l.append(data)

#     return {"result":l}      
             






