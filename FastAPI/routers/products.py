from fastapi import APIRouter
from fastapi import HTTPException
from db import database
from db import products
from models.product import ProductIn, Product

router = APIRouter()


# прочитать все записи
@router.get("/products/", response_model=list[Product])
async def read_all():
    query = products.select()
    return await database.fetch_all(query)


# прочитать одну запись
@router.get("/products/{id}", response_model=Product)
async def read(id: int):
    query = products.select().where(products.c.id == id)
    result = await database.fetch_one(query)

    if not result:
        raise HTTPException(status_code=404, detail=f"Id {id} not found")

    return result


# удалить одну запись
@router.delete("/products/{id}", response_model=dict)
async def delete(id: int):
    query = products.delete().where(products.c.id == id)

    if not await database.execute(query):
        raise HTTPException(status_code=404, detail=f"Id {id} not found")

    return {'Message': f'Products with id {id} deleted'}


# добавить запись
@router.post("/products/", response_model=dict)
async def add(product: ProductIn):
    query = products.insert().values(
        name=product.name,
        description=product.description,
        price=product.price,
    )
    last_record_id = await database.execute(query)

    return {"message": f"New Products added with id {last_record_id}"}


# редактировать запись
@router.put("/products/{id}", response_model=dict)
async def edit(id: int, new_product: ProductIn):
    query = products.update().where(
        products.c.id == id,
    ).values(
        name=new_product.name,
        description=new_product.description,
        price=new_product.price,
    )
    last_record_id = await database.execute(query)

    if not last_record_id:
        raise HTTPException(status_code=404, detail=f"Products with id {id} not found")

    return {"message": f"Products with id {last_record_id} edit successfully"}
