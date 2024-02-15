from .. import models,schemas,utils,oauth2
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import engine, get_db
from typing import Optional,List
from sqlalchemy import func
from fastapi.encoders import jsonable_encoder

router=APIRouter(prefix="/posts",tags=['Posts'],redirect_slashes=False)
# router = APIRouter(redirect_slashes=False)
# app.include_router(router)

@router.get("/",response_model=List[schemas.Postout])   
def get_post(db: Session = Depends(get_db),get_current_user:int=Depends(oauth2.get_current_user),limit:int =10,
          skip:int=0, search:Optional[str]="" ):
           
    posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    result=db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).all()
    print(result)
    results= [
    {"post": post, "votes": vote_count} for post, vote_count in result
]
    
    return result

@router.get("/{id}",response_model=List[schemas.Postout])
def getposts(id:int,response:Response,db: Session = Depends(get_db),get_current_user:int=Depends(oauth2.get_current_user)):
    
    posts=db.query(models.Post).filter(models.Post.id ==id).first()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found bey")
    print(posts)
    if posts.owner_id !=get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="not authorized")
    #posts.update()    
    return posts

@router.post("/",response_model=schemas.Cpost)   
def create_post(post:schemas.Post,db: Session = Depends(get_db),
                get_current_user:int=Depends(oauth2.get_current_user)):
    #newpost=models.Post(title=post.title,content=post.content,published=post.published)
    #newpost=models.Post(title=post.title,content=post.content,published=post.published)
    data=post.dict()
    print(data)
    if get_current_user.id == 31 and data["title"].lower().startswith("sunny") == False :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="title shld be sunny")
            
    newpost=models.Post(**post.dict(),owner_id=get_current_user.id)
    print(get_current_user)
    db.add(newpost)
    db.commit()
    db.refresh(newpost)
    
    return newpost        
    
    
    

# @app.delete("/posts/{id}")
# def delete(id:int):
#     index=getindex(id)
#     if not index:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} does not exist")
#     l.pop(index)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


    

@router.delete("/{id}")
def delete(id:int,db:Session = Depends(get_db),get_current_user:int=Depends(oauth2.get_current_user)):
     post_query=db.query(models.Post).filter(models.Post.id==id)
     posts=post_query.first()
     #posts=post_query.first()
     if not posts:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found bey")
     if posts.owner_id != get_current_user.id:
                 raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="not authorized")

         
     
     post_query.delete(synchronize_session=False)
     db.commit()
     return Response(status_code=status.HTTP_200_OK)
4





@router.put("/{id}",response_model=schemas.Cpost)
def update(id:int,post:schemas.Post,db: Session = Depends(get_db),get_current_user:int=Depends(oauth2.get_current_user)):
    
       post_query=db.query(models.Post).filter(models.Post.id==id)
       posts=post_query.first()
       print(post_query)
       print()
       print(post.dict())
       owner_id={"owner_id":31}
       content=post.dict()
       updatedata={**owner_id,**content}
       print(updatedata)
       if not posts:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found bey")
       #return {"posts":posts}
       if posts.owner_id !=get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="not authorized")
       post_query.update(updatedata,synchronize_session=False)
       db.commit()
       
       return posts