from .models import Users
from .schemas import UserCreate, UserRead, UserUpdate
from sqlalchemy.orm import Session
from . import views

def create_user(db: Session, user_data: UserCreate):
    new_user = Users(
        product=user_data.product,
        category=user_data.category,
        quantity=user_data.quantity,
        price=user_data.price
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



def get_users(db: Session):
    return views.get_users(db)


def update_user(db:Session, user_id:int, user_data:UserUpdate):
    user = db.query(Users).filter(Users.id ==  user_id).first()
    if not user:
        return None
    
    user.product = user_data.product
    user.category = user_data.category
    user.quantity = user_data.quantity
    user.price = user_data.price
    db.commit()
    db.refresh(user)
    return user

def search_user(db:Session, user_id:int):
    user = db.query(Users).filter(Users.id == user_id).first()
    return user

def delete_user(db:Session, user_id:int):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
