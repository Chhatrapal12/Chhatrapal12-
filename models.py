from sqlalchemy.orm import Mapped, mapped_column
from database.db import Base

class Users(Base):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(unique=True, primary_key=True, index=True)
    product:Mapped[str] = mapped_column(nullable=False)
    category:Mapped[str] = mapped_column(nullable=False)
    quantity:Mapped[int] = mapped_column(nullable=False)
    price:Mapped[float] = mapped_column(nullable=False)
