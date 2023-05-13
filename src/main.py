from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import uvicorn

from typing import List

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/version")
def get_app_version():
    return {'version': 2.0}

if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0', port=8000) # pragma: no cover


tags_metadata = [
    {
        "name": "FurnitureModel",
        "description": "Работа с **FurnitureModel**",
    },
    {
        "name": "KA",
        "description": "Работа с **КА**",
    },
    {
        "name": "DocPayment",
        "description": "Работа с **DocPayment**",
    },
    {
        "name": "Payment",
        "description": "Работа с **Payment**",
    },
]

# dba = SessionLocal()
# item = crud.get_furniture_model(dba,"Ст-6")
# print(item.price)
# dba.close()

# Dependency
def get_db():# pragma: no cover
    """
    Задаем зависимость к БД. При каждом запросе будет создаваться новое
    подключение.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def res_to_lis(res):
    res2 = []
    for item in res:
        res2.append(item.to_dict())
    return res2

# +=================+
# |    FURNITURE    |
# +=================+

@app.post("/FurnitureModel/Create/", response_model=schemas.FurnModel,tags = ['FurnitureModel'])
def create_furniture_model(fm: schemas.FurnModel,db:AsyncSession = Depends(get_db)):
    """
    Создание новой модели мебели
    """
    fur_model = crud.get_furniture_model(db,fm.furn_model)
    if fur_model:
        raise HTTPException(status_code=400,detail='furniture model already exists') 
    return crud.create_furniture_model(db=db,fm=fm)

@app.get("/FurnitureModel/ReadByModel/", response_model=schemas.FurnModel,tags = ['FurnitureModel'])
def read_furniture_model(furn_model:str = '',db:AsyncSession = Depends(get_db)):
    """
    Получить модель мебели
    """
    fm = crud.get_furniture_model(db,furn_model)
    if len(fm) == 0: raise HTTPException(status_code=400,detail='furniture model not found') 
    return fm

@app.get('/FurnitureModel/ReadAll/', response_model=List[schemas.FurnModel],tags = ['FurnitureModel'])
def read_all_furniture_models(skip: int = 0, limit: int = 100, db:AsyncSession = Depends(get_db)):
    """
    Получить список всех моделей мебели со скипом первых и указанным лимитом
    """
    return res_to_lis(crud.get_all_furniture_models(db,skip,limit))

# +============+
# |     KA     |
# +============+

@app.post("/KA/Create/",response_model=schemas.KA,tags = ['KA'])
def create_KA(ka:schemas.KA, db:AsyncSession = Depends(get_db)):
    """
    Создание нового КА
    """
    kontr_agent = crud.get_KA(db=db,id_ka=ka.id_KA)
    if kontr_agent:
        raise HTTPException(status_code=400,detail='KA already exists') 
    return crud.create_KA(db,ka)

@app.post('/KA/AddNewDoc/',response_model=schemas.Doc_payment,tags=['KA'])
def add_doc_payment_to_ka(id_ka:int, dp:schemas.Doc_payment,db:AsyncSession = Depends(get_db)):
    """
    добавить КА с данныи ИД указанный договор оплаты
    """
    ka = crud.get_KA(db,id_ka)
    if not ka:
        raise HTTPException(status_code=400,detail='КА с этим кодом не существует')
    if dp.id_KA != id_ka:
        raise HTTPException(status_code=400,detail='номер КА принимающего не равен номеру КА в документе оплаты')
    doc_pay = crud.get_doc(db,dp.doc_num)
    if doc_pay:# pragma: no cover
        crud.update_doc_payment(db,dp)
        return dp
    else: return crud.create_doc_pay(db,dp)
    

@app.get('/KA/ReadByID/',response_model=schemas.KA, tags=['KA'])
def read_KA_by_id(id_KA:int = 0,db:AsyncSession = Depends(get_db)):
    """
    получить КА по его ИД
    """
    ka = crud.get_KA(db,id_KA)
    if len(ka) == 0: raise HTTPException(status_code=404,detail='KA not found')
    return ka

@app.get('/KA/ReadAll/', response_model=List[schemas.KA],tags = ['KA'])
def read_all_KA(skip: int = 0, limit: int = 100, db:AsyncSession = Depends(get_db)):
    """
    Получить список всех KA со скипом первых и указанным лимитом
    """
    return res_to_lis(crud.get_all_KA(db,skip,limit))

# +=====================+
# |     DOC PAYMENT     |
# +=====================+

@app.post("/DocPayment/Create/",response_model=schemas.Doc_payment,tags = ['DocPayment'])
def create_doc_payment(dp:schemas.Doc_payment,db:AsyncSession = Depends(get_db)):
    """
    Создание нового документа оплаты
    """
    doc_pay = crud.get_doc(db,dp.doc_num)
    if doc_pay:
        raise HTTPException(status_code=400,detail='payment document already exists')
    ka = crud.get_KA(db,dp.id_KA)
    if not ka:
        raise HTTPException(status_code=400,detail='этого КА не существует')
    return crud.create_doc_pay(db,dp)

@app.get('/DocPayment/ReadByNum/',response_model=schemas.Doc_payment,tags = ['DocPayment'])
def read_doc_payment_by_num(doc_num:str = '1', db:AsyncSession = Depends(get_db)):
    """
    Получить документ оплаты по его номеру
    """
    dp = crud.get_doc(db,doc_num)
    if len(dp) == 0 : raise HTTPException(status_code=400,detail='dp not exist')
    return dp

@app.get('/DocPayment/ReadByKA/',response_model=List[schemas.Doc_payment],tags = ['DocPayment'])
def read_doc_payment_by_KA(id_KA:int = 0, db:AsyncSession = Depends(get_db)):
    """
    Получить документы оплаты у КА
    """
    dpl = res_to_lis(crud.get_docs_by_KA(db,id_KA))
    if len(dpl) == 0: raise HTTPException(status_code=400,detail='dp not exist')
    return dpl

@app.get('/DocPayment/ReadAll/',response_model=List[schemas.Doc_payment],tags = ['DocPayment'])
def read_all_doc_payment(skip: int = 0, limit: int = 100, db:AsyncSession = Depends(get_db)):
    """
    Получить все документы оплаты
    """
    return res_to_lis(crud.get_all_docs(db,skip,limit))

# +=================+
# |     PAYMENT     |
# +=================+

@app.post("/Payment/Create/",response_model=schemas.payment,tags = ['Payment'])
def create_payment(pay:schemas.payment,db:AsyncSession = Depends(get_db)):
    """
    Создание новой оплаты
    """
    pa = crud.get_payment(db,pay.id_payment)
    if pa: raise HTTPException(status_code=400,detail='payment already exists')
    doc = crud.get_doc(db,pay.doc_num)
    if not doc: raise HTTPException(status_code=400,detail='have no doc by this num')
    model = crud.get_furniture_model(db,pay.furn_model)
    if not model: raise HTTPException(status_code=400,detail='have no model by this num')
    return crud.create_payment(db,pay)

@app.get('/Payment/ReadPayment/',response_model=schemas.payment,tags=['Payment'])
def read_payment_by_id(id_pay:int = 0, db:AsyncSession = Depends(get_db)):
    """
    Получить оплатe по её номеру
    """
    pay = crud.get_payment(db,id_pay)
    if len(pay) == 0: raise HTTPException(400,'no pay by this id')
    return pay

@app.get('/Payment/ReadByDoc/',response_model=List[schemas.payment],tags=['Payment'])
def read_payment_by_dock_num(doc_num:int = 0, db:AsyncSession = Depends(get_db)):
    """
    Получить оплаты по их номеру договора
    """
    plis = res_to_lis(crud.get_payments_by_doc_num(db,doc_num))
    if len(plis) == 0: raise HTTPException(400,'hove no pay by this doc')
    return plis

@app.get('/Payment/ReadByFurnitureModel/',response_model=List[schemas.payment],tags=['Payment'])
def read_payment_by_furn_model(model:str = 'Ст-1', db:AsyncSession = Depends(get_db)):
    """
    Получить оплаты по моделе мебели
    """
    fmlis = res_to_lis(crud.get_payments_by_furniture_model(db,model))
    if len(fmlis) == 0: raise HTTPException(400,'no pay by this model')
    return fmlis

@app.get('/Payment/ReadAll/',response_model=List[schemas.payment],tags=['Payment'])
def read_all_payment(skip: int = 0, limit: int = 100, db:AsyncSession = Depends(get_db)):
    """
    Получить все оплаты
    """
    return res_to_lis(crud.get_payments(db,skip,limit))
