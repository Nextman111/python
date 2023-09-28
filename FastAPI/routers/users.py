from fastapi import APIRouter
from fastapi import HTTPException
from db import database
from db import users
from models.user import UserIn, User

router = APIRouter()


# прочитать все записи
@router.get("/users/", response_model=list[User])
async def read_all():
    query = users.select()
    return await database.fetch_all(query)


# прочитать одну запись
@router.get("/users/{id}", response_model=User)
async def read(id: int):
    query = users.select().where(users.c.id == id)
    result = await database.fetch_one(query)

    if not result:
        raise HTTPException(status_code=404, detail=f"Id {id} not found")

    return result


# удалить одну запись
@router.delete("/users/{id}", response_model=dict)
async def delete(id: int):
    query = users.delete().where(users.c.id == id)

    if not await database.execute(query):
        raise HTTPException(status_code=404, detail=f"Id {id} not found")

    return {'Message': f'User with id {id} deleted'}


# добавить запись
@router.post("/users/", response_model=dict)
async def add(user: UserIn):
    query = users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password,
    )
    last_record_id = await database.execute(query)

    return {"message": f"New user added with id {last_record_id}"}


# редактировать запись
@router.put("/users/{id}", response_model=dict)
async def edit(id: int, new_user: UserIn):
    query = users.update().where(
        users.c.id == id,
    ).values(
        name=new_user.name,
        email=new_user.email,
        password=new_user.password,
    )
    last_record_id = await database.execute(query)

    if not last_record_id:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")

    return {"message": f"User with id {last_record_id} edit successfully"}
