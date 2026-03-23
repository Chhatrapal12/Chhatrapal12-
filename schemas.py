from pydantic import BaseModel
from typing import Optional
# User Create  schema 
class UserCreate(BaseModel):
    """ User Create Data """
    # id :int 
    product: str
    category: str
    quantity: int
    price: float
    
    class config:
        orm_mode = True


# User responce schema 
class UserRead(BaseModel):
    id : int
    product:str
    category: str
    quantity:int 
    price : float

    class config:
        orm_mode = True

# user Update Schema

class UserUpdate(BaseModel):
    product: Optional[str] = None
    category: Optional[str] = None
    quantity: Optional[int] = None
    price : Optional[float] = None

    class config:
        orm_mode = True