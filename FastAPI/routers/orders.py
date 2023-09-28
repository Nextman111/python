from datetime import datetime

from fastapi import APIRouter
from fastapi import HTTPException
from db import database
from db import orders
from models.order import OrderIn, Order

router = APIRouter()


# прочитать все записи
@router.get("/orders/", response_model=list[Order])
async def read_all():
    query = orders.select()
    return await database.fetch_all(query)


# прочитать одну запись
@router.get("/orders/{id}", response_model=Order)
async def read(id: int):
    query = orders.select().where(orders.c.id == id)
    result = await database.fetch_one(query)

    if not result:
        raise HTTPException(status_code=404, detail=f"Id {id} not found")

    return result


# удалить одну запись
@router.delete("/orders/{id}", response_model=dict)
async def delete(user_id: int):
    query = orders.delete().where(orders.c.id == id)

    if not await database.execute(query):
        raise HTTPException(status_code=404, detail=f"Id {id} not found")

    return {'Message': f'Order with id {id} deleted'}


# добавить запись
@router.post("/orders/", response_model=dict)
async def add(order: OrderIn):
    query = orders.insert().values(
        user_id=order.user_id,
        product_id=order.product_id,
        order_date=datetime.now().strftime("%d/%m/%y, %H:%M:%S"),
        status=order.status,
    )
    last_record_id = await database.execute(query)

    return {"message": f"New Order added with id {last_record_id}"}


# редактировать запись
@router.put("/orders/{id}", response_model=dict)
async def edit(id: int, new_order: OrderIn):
    query = orders.update().where(
        orders.c.id == id,
    ).values(
        user_id=new_order.user_id,
        product_id=new_order.product_id,
        order_date=datetime.now().strftime("%d/%m/%y, %H:%M:%S"),
        status=new_order.status,
    )
    last_record_id = await database.execute(query)

    if not last_record_id:
        raise HTTPException(status_code=404, detail=f"Order with id {id} not found")

    return {"message": f"Order with id {last_record_id} edit successfully"}
