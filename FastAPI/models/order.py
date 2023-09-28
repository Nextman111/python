from pydantic import BaseModel


# • Таблица заказов должна содержать следующие поля:
# id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.

# модель для добавления данных в базу
class OrderIn(BaseModel):
    user_id: int
    product_id: int
    status: str


# модель для чтения из базы
class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    status: str
    order_date: str
