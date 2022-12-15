from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class BaseModel(Base):
    """
    Абстрактный базовый класс, где описаны все поля и методы по умолчанию
    """
    __abstract__ = True

    def __repr__(self):
        return f"<{type(self).__name__}(id={self.id})>" # pragma: no cover

# class User(BaseModel):
#     __tablename__ = "users"

#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")


# class Item(BaseModel):
#     __tablename__ = "items"

#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")

class FurnitureModel(Base):
    __tablename__ = "FurnitureModel"

    furn_model = Column(String,index=True,primary_key=True)
    furn_model_name = Column(String,unique=True)
    characteristics = Column(String)
    price = Column(Float,nullable=False)
    def to_dict(self) -> dict:
        return {'furn_model':self.furn_model,
            'furn_model_name':self.furn_model_name,
            'characteristics':self.characteristics,
            'price':self.price} # pragma: no cover

class KA(Base):
    __tablename__ = "KA"

    id_ka = Column(Integer,index=True,primary_key=True)
    name = Column(String)
    adress = Column(String)
    phone = Column(String)
    def to_dict(self) -> dict:
        return {'id_KA':self.id_ka,
            'name':self.name,
            'adress':self.adress,
            'phone_number':self.phone} # pragma: no cover

class Doc_payment(Base):
    __tablename__ = "DocPayment"

    doc_num = Column(String,index=True,primary_key=True)
    id_KA = Column(Integer,ForeignKey("KA.id_ka"),nullable=False)
    date_create = Column(DateTime)
    date = Column(DateTime)
    def to_dict(self) -> dict:
        return {'doc_num':self.doc_num,
            'id_KA':self.id_KA,
            'date_create':self.date_create,
            'date':self.date} # pragma: no cover

class Payment(Base):
    __tablename__ = "Payment"

    id_payment = Column(Integer,primary_key=True)
    doc_num = Column(String,ForeignKey("DocPayment.doc_num"),nullable=False)
    furn_model = Column(String,ForeignKey("FurnitureModel.furn_model"),nullable=False)
    furn_name = Column(String)
    amount = Column(Integer,nullable=False)
    def to_dict(self) -> dict:
        return {'id_payment':self.id_payment,
            'doc_num':self.doc_num,
            'furn_model':self.furn_model,
            'furn_name':self.furn_name,
            'amount':self.amount} # pragma: no cover