from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import uvicorn

from typing import List

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0', port=8000)

# dba = SessionLocal()
# item = crud.get_furniture_model(dba,"Ст-6")
# print(item.price)
# dba.close()

# Dependency
def get_db():
    """
    Задаем зависимость к БД. При каждом запросе будет создаваться новое
    подключение.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/FurnitureModel/", response_model=schemas.FurnModel)
def create_furniture_model(fm: schemas.FurnModel,db:AsyncSession = Depends(get_db)):
    """
    Создание новой модели мебели
    """
    fur_model = crud.get_furniture_model(db,fm.furn_model)
    if fur_model:
        print(fur_model.price)
        raise HTTPException(status_code=400,detail='furniture model already exists')
    created_FM = crud.create_furniture_model(db=db,fm=fm)
    print(created_FM)
    return {'res':created_FM}


@app.post("/KA/",response_model=schemas.KA)
def create_KA(ka:schemas.KA, db:AsyncSession = Depends(get_db)):
    """
    Создание нового КА
    """
    kontr_agent = crud.get_KA(db=db,id_ka=ka.id_KA)
    if kontr_agent:
        raise HTTPException(status_code=400,detail='KA already exists')
    return crud.create_KA(db,ka)

@app.post("/doc_payment/",response_model=schemas.Doc_payment)
def create_doc_payment(dp:schemas.Doc_payment,db:AsyncSession = Depends(get_db)):
    """
    Создание нового документа оплаты
    """
    doc_pay = crud.get_doc(db,dp.doc_num)
    if doc_pay:
        raise HTTPException(status_code=400,detail='payment document already exists')
    return crud.create_doc_pay(db,dp)

@app.post("/payment/",response_model=schemas.payment)
def create_payment(pay:schemas.payment,db:AsyncSession = Depends(get_db)):
    """
    Создание новой оплаты
    """
    pa = crud.get_payment(db,pay.id_payment)
    if pa: raise HTTPException(status_code=400,detail='payment already exists')
    return crud.create_payment(db,pay)

@app.get("/FurnitureModel/", response_model=schemas.FurnModel)
def read_furniture_model(furn_model:str = '',db:AsyncSession = Depends(get_db)):
    """
    Получить модель мебели
    """
    fm = crud.get_furniture_model(db,furn_model)
    return fm

# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     """
#     Создание пользователя, если такой email уже есть в БД, то выдается ошибка
#     """
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     """
#     Получение списка пользователей
#     """
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     """
#     Получение пользователя по id, если такого id нет, то выдается ошибка
#     """
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     """
#     Добавление пользователю нового предмета
#     """
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     """
#     Получение списка предметов
#     """
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items