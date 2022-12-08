from pydantic import BaseModel
from typing import Union, List
import datetime

# КА
class KA(BaseModel):
    """
    Класс для отображения информации о покупателях/КА
    """
    id_KA: int
    name: str
    adress: str
    phone_number: str

# Мебель
class FurnModel(BaseModel):
    """
    Класс описания модели мебели
    """
    furn_model_name: str
    furn_model: str
    characteristics: str
    price: float

# Договор
class Doc_payment(BaseModel):
    """
    класс описания информации о договоре
    """
    doc_num: int
    id_KA: int
    date_create: datetime.datetime
    date: datetime.datetime

# продажа
class payment(BaseModel):
    """
    информация о продажах
    """
    id_payment: int
    doc_num: int
    furn_name: str
    furn_model: str
    amount: int

class ItemBase(BaseModel):
    """
    Базовый класс для Item
    """
    title: str
    description: Union[str,None] = None


class ItemCreate(ItemBase):
    """
    Класс для создания Item, наследуется от базового ItemBase, но не содержит
    дополнительных полей, пока что
    """
    pass


class Item(ItemBase):
    """
    Класс для отображения Item, наследуется от базового ItemBase
    поля значения для полей id и owner_id будем получать из БД
    """
    id: int
    owner_id: int

    class Config:
        """
        Задание настройки для возможности работать с объектами ORM
        """
        orm_mode = True


class UserBase(BaseModel):
    """
    Базовый класс для User
    """
    email: str


class UserCreate(UserBase):
    """
    Класс для создания User. Пароль мы не должны нигде отображать, поэтому
    это поле есть только в классе для создания.
    """
    password: str


class User(UserBase):
    """
    Класс для отображения информации о User. Все значения полей будут браться
    из базы данных
    """
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True