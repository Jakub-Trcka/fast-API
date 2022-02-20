from app import oath2
from .. import models, oath2, schemas
from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from typing import  List
from typing import Optional
from sqlalchemy import func

router = APIRouter(prefix="/posts", tags=['Posts'])


# get posts
# @router.get("/", response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ''):


    posts = db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    return posts


# create a new post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):

    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


# get post by id
@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, response: Response, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):

    post = db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")

    return post


# delete post by id
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, response: Response, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if not post:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not authorized to perform requested action')

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# update post by id
@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, response: Response,updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if not post:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not authorized to perform requested action')

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()