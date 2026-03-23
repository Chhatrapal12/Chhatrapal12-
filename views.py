from .models import Users
from sqlalchemy.orm  import Session 

def get_users(db:Session):
    users_list = db.query(Users).all() #ORM
    return users_list