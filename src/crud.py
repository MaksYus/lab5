from sqlalchemy.orm import Session

from src import models, schemas

# вспомогательный метод для уменьшения кода
def acr(db:Session,item):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

#  +===================+
#  |      CREATE       |
#  +===================+

def create_user(db: Session, user: schemas.UserCreate):# pragma: no cover
    """
    Добавление нового пользователя
    """
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user 

def create_KA(db: Session,ka:schemas.KA):
    """
    Добавление нового кнтрагента/покупателя
    """
    kontrA = models.KA(id_ka=ka.id_KA, name=ka.name, adress=ka.adress, phone=ka.phone_number)
    return acr(db,kontrA).to_dict() # pragma: no cover

def create_furniture_model(db:Session,fm:schemas.FurnModel):# pragma: no cover
    """
    Создание новой модели мебели
    """
    fur_model = models.FurnitureModel(furn_model = fm.furn_model, furn_model_name = fm.furn_model_name, 
    characteristics = fm.characteristics, price = fm.price)
    fur_model = acr(db,fur_model)
    return fur_model.to_dict() # pragma: no cover

def create_doc_pay(db:Session,dp:schemas.Doc_payment):
    """
    Создание нового документа оплаты
    """
    doc_pay = models.Doc_payment(doc_num = dp.doc_num, id_KA = dp.id_KA, date_create = dp.date_create, 
    date = dp.date)
    return acr(db,doc_pay).to_dict() # pragma: no cover

def create_payment(db:Session, pa:schemas.payment):# pragma: no cover
    """
    Создание новой оплаты
    """
    pay = models.Payment(doc_num = pa.doc_num, furn_model = pa.furn_model,
    furn_name = pa.furn_name, amount = pa.amount)
    return acr(db,pay).to_dict() # pragma: no cover

def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):# pragma: no cover
    """
    Добавление нового Item пользователю
    """
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item # pragma: no cover

#  +===================+
#  |        GET        |
#  +===================+

def get_f(item):
    if item :
        return item.to_dict()
    else: return {}

# def get(db:Session):
#     """
    
#     """
#     return db.query().filter()

def get_payment(db:Session,id_payment:int = 0):
    """
    получить оплату по её ид
    """
    return get_f(db.query(models.Payment).filter(models.Payment.id_payment == id_payment).first())# pragma: no cover

def get_payments_by_doc_num(db:Session, doc_num:int = 0):
    """
    Получить все оплаты по номеру документа
    """
    return db.query(models.Payment).filter(models.Payment.doc_num == doc_num).all()# pragma: no cover

def get_payments_by_furniture_model(db:Session, furn_model:str = ''):
    """
    Получить оплаты по модели мебели
    """
    return db.query(models.Payment).filter(models.Payment.furn_model == furn_model).all()# pragma: no cover

def get_payments_by_model_doc(db:Session,doc_num:int = 0,furn_model:str = ''):
    """
    Получить все оплаты по номеру договора и модели мебели
    """
    return db.query(models.Payment).filter((models.Payment.doc_num == doc_num) and (models.Payment.furn_model == furn_model)).all()# pragma: no cover

def get_payments(db:Session,skip: int = 0, limit:int = 200):
    """
    получить все платежи
    """
    return db.query(models.Payment).offset(skip).limit(limit).all()# pragma: no cover

def get_doc(db:Session, doc_num:str = ''):
    """
    Получить документ по его номеру
    """
    return get_f(db.query(models.Doc_payment).filter(models.Doc_payment.doc_num == doc_num).first())# pragma: no cover

def get_docs_by_KA(db:Session, id_ka:int = 0):
    """
    Получить документ по КА
    """
    return db.query(models.Doc_payment).filter(models.Doc_payment.id_KA == id_ka).all()# pragma: no cover

def get_all_docs(db:Session,skip: int = 0, limit: int = 100):
    """
    Получить все документы
    """
    return db.query(models.Doc_payment).offset(skip).limit(limit).all()# pragma: no cover

def get_KA(db:Session,id_ka:int = 0):
    """
    Получить КА по его ИД
    """
    return get_f(db.query(models.KA).filter(models.KA.id_ka == id_ka).first())# pragma: no cover

def get_all_KA(db:Session,skip: int = 0, limit: int = 100):
    """
    Получить список всех КА
    """
    return db.query(models.KA).offset(skip).limit(limit).all()# pragma: no cover

def get_furniture_model(db:Session, furn_model:str = ''):
    """
    Получить модель мебели  
    """
    return get_f(db.query(models.FurnitureModel).filter(models.FurnitureModel.furn_model == furn_model).first())# pragma: no cover

def get_all_furniture_models(db:Session,skip: int = 0, limit: int = 100):
    """
    Получить все модели мебели
    """
    return db.query(models.FurnitureModel).offset(skip).limit(limit).all()# pragma: no cover

def get_user(db: Session, user_id: int):
    """
    Получить пользователя по его id
    """
    return get_f( db.query(models.User).filter(models.User.id == user_id).first())# pragma: no cover


def get_user_by_email(db: Session, email: str):
    """
    Получить пользователя по его email
    """
    return get_f(db.query(models.User).filter(models.User.email == email).first())# pragma: no cover


def get_items(db: Session, skip: int = 0, limit: int = 100):
    """
    Получить список предметов из БД
    skip - сколько записей пропустить
    limit - маскимальное количество записей
    """
    return db.query(models.Item).offset(skip).limit(limit).all()# pragma: no cover


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Получить список пользователей из БД
    skip - сколько записей пропустить
    limit - маскимальное количество записей
    """
    return db.query(models.User).offset(skip).limit(limit).all()# pragma: no cover

# +==========+
# |  UPDATE  |
# +==========+

def update_doc_payment(db:Session,dp:schemas.Doc_payment):# pragma: no cover
    """
    Обновление документа оплаты
    """
    doc_pay = models.Doc_payment(doc_num = dp.doc_num, id_KA = dp.id_KA, date_create = dp.date_create, 
    date = dp.date)
    text = f"""
    UPDATE DocPayment
    SET id_KA = {dp.id_KA}, date_create = {dp.date_create}, date = {dp.date}
    WHERE doc_num = {dp.doc_num}
    """
    with db.connection() as con:
        res = con.execute(text)
    return res # pragma: no cover
    