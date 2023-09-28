from pydantic import BaseModel
from pydantic import Field

# • Таблица товаров должна содержать следующие поля:
# id (PRIMARY KEY), название, описание и цена.

# модель для добавления данных в базу
class ProductIn(BaseModel):
    name: str = Field(..., min_length=3, max_length=128)
    description: str = Field(max_length=256)
    price: float = Field(..., gt=0)


# модель для чтения из базы
class Product(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=128)
    description: str = Field(max_length=256)
    price: float = Field(..., gt=0)
