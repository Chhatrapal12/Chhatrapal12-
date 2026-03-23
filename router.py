from fastapi import APIRouter, Depends

from database.db import get_db
from . schemas import UserRead, UserCreate, UserUpdate
from . import views
from sqlalchemy.orm import Session
from . import crud


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


# get all users 
@router.get("/get-users", response_model=list[UserRead]) 
async def read_user(db:Session=Depends(get_db)):
    return crud.get_users(db)


# create user
@router.post("/create-user")
async def create_user( user:UserCreate,db:Session=Depends(get_db)):
    crud.create_user(db, user)
    return {"message": "User created successfully!"}


# updateUser 
@router.put("/update-user/{user_id}")
async def update_user(user_id:int,  userdata:UserUpdate, db:Session=Depends(get_db) ):
    updated_user = crud.update_user(db, user_id, userdata)
    if updated_user:
        return {"message": "User updated successfully!"}
    return {"message": "User not found!"}

# searchUser
@router.get('/search-user/{user_id}')
async def search(user_id:int, db:Session=Depends(get_db)):
    user = crud.search_user(db, user_id)
    if user:
        return user
    return {"message": "User not found!"}

@router.delete('/delete-user/{user_id}')
async def delete(user_id:int, db:Session=Depends(get_db)):
    user = crud.search_user(db,user_id)
    if user:
        crud.delete_user(db,user_id)
        return {"Delete User Sucessfully"}
    return {"User Not Found"}
