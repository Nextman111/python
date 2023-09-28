import uvicorn
from fastapi import FastAPI
from db import database
from routers import users
from routers import products
from routers import orders

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def startup():
    await database.disconnect()


# import routs
app.include_router(users.router, tags=["users"])
app.include_router(products.router, tags=["products"])
app.include_router(orders.router, tags=["orders"])


@app.get("/",)
async def root():
    return {"message": "Hello World!"}


# @app.get("/items/{item_id}")
# async def items(item_id:int):
#     return {"message": f"This is {item_id}"}

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )
