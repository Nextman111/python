from pydantic import BaseModel
from pydantic import Field, EmailStr


# модель для добавления данных в базу
class UserIn(BaseModel):
    name: str
    email: EmailStr = Field(..., max_length=128)
    password: str = Field(..., min_length=6, max_length=8)


# модель для чтения из базы
class User(BaseModel):
    id: int
    name: str
    email: EmailStr = Field(..., max_length=128)
