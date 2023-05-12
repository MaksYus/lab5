from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def test_t():
    """
    заглушка
    """
    assert True

# from src.main import app, get_db
# from src.models import Base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Тестовая БД

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# TestingSessionLocal = sessionmaker(
#     autocommit=False, autoflush=False, bind=engine)

# Base.metadata.drop_all(bind=engine)  # Удалем таблицы из БД
# Base.metadata.create_all(bind=engine)  # Создаем таблицы в БД


# def override_get_db():
#     """
#     Данная функция при тестах будет подменять функцию get_db() в main.py.
#     Таким образом приложение будет подключаться к тестовой базе данных.
#     """
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()


# app.dependency_overrides[get_db] = override_get_db  # Делаем подмену

# client = TestClient(app)  # создаем тестовый клиент к нашему приложению





# def test_dp_get_all_NONE():
#     """
#     Проверка на получение всех дп - НЕУДАЧА
#     """
#     response = client.get("/DocPayment/ReadAll/?skip=0&limit=100")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert len(data) == 0

# def test_KA_get_all_NONE():
#     """
#     Проверка на получение всех дп - НЕУДАЧА
#     """
#     response = client.get("/KA/ReadAll/?skip=0&limit=100")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert len(data) == 0

# def test_fm_get_all_NONE():
#     """
#     Проверка на получение всех дп - НЕУДАЧА
#     """
#     response = client.get("/FurnitureModel/ReadAll/?skip=0&limit=100")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert len(data) == 0

# def test_pay_get_all_neg():
#     """
#     Проверка на получение всех payment - УСПЕХ
#     """
#     response = client.get("/Payment/ReadAll/")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert len(data) == 0

# # +========+
# # |   KA   |
# # +========+


# def test_create_KA():
#     """
#     Тест на создание нового КА
#     """
#     response = client.post(
#         "/KA/Create/",
#         json={"id_KA": 123, "name": "петя", "adress":"ул.пушкниа","phone_number":"9999"}
#     )
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["id_KA"] == 123
#     assert data["name"] == "петя"
#     assert data["adress"] == "ул.пушкниа"
#     assert data["phone_number"] == "9999"


# def test_create_exist_KA():
#     """
#     Проверка случая, когда мы пытаемся добавить существующего КА
#     в БД, т.е. когда данный id уже присутствует в БД.
#     """
#     response = client.post(
#         "/KA/Create/",
#         json={"id_KA": 123, "name": "петя", "adress":"ул.пушкниа","phone_number":"9999"}
#     )
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == "KA already exists"


# def test_get_all_KA():
#     """
#     Тест на получение списка КА из БД
#     """
#     response = client.get("/KA/ReadAll/")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data[0]["id_KA"] == 123
#     assert data[0]["name"] == "петя"
#     assert data[0]["adress"] == "ул.пушкниа"
#     assert data[0]["phone_number"] == "9999"


# def test_get_KA_by_id():
#     """
#     Тест на получение KA из БД по его id
#     """
#     response = client.get("/KA/ReadByID/?id_KA=123")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["id_KA"] == 123
#     assert data["name"] == "петя"
#     assert data["adress"] == "ул.пушкниа"
#     assert data["phone_number"] == "9999"


# def test_KA_not_found():
#     """
#     Проверка случая, если KA с таким id отсутствует в БД
#     """
#     response = client.get("/KA/ReadByID/?id_KA=999")
#     assert response.status_code == 404, response.text
#     data = response.json()
#     assert data["detail"] == "KA not found"


# def test_add_doc_payment_to_ka_1():
#     """
#     проверка на добавление нового дока к КА - УСПЕХ
#     """
#     response = client.post(
#         "/KA/AddNewDoc/?id_ka=123",
#         json={"doc_num": 123, "id_KA": 123, "date_create":"2022-12-16T21:29:15.365Z","date":"2022-12-16T21:29:15.365Z"}
#     )
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["id_KA"] == 123

# def test_add_doc_payment_to_ka_2():
#     """
#     проверка на добавление нового дока к КА - НЕТ КА
#     """
#     response = client.post(
#         "/KA/AddNewDoc/?id_ka=9123",
#         json={"doc_num": 9123, "id_KA": 9123, "date_create":"2022-12-16T21:29:15.365Z","date":"2022-12-16T21:29:15.365Z"}
#     )
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == "КА с этим кодом не существует"

# def test_add_doc_payment_to_ka_3():
#     """
#     проверка на добавление нового дока к КА - КА НЕ СОВПАДАЕТ
#     """
#     response = client.post(
#         "/KA/AddNewDoc/?id_ka=123",
#         json={"doc_num": 12, "id_KA": 1234, "date_create":"2022-12-16T21:29:15.365Z","date":"2022-12-16T21:29:15.365Z"}
#     )
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == "номер КА принимающего не равен номеру КА в документе оплаты"


# # +================+
# # |   DocPayment   |
# # +================+

# def test_create_DP():
#     """
#     Тест на создание нового docpay УСПЕХ
#     """
#     response = client.post(
#         "/DocPayment/Create/",
#         json={"doc_num": 1, "id_KA": 123, "date_create":"2022-12-16T21:29:15.365Z","date":"2022-12-16T21:29:15.365Z"}
#     )
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["id_KA"] == 123


# def test_create_DP_NEG():
#     """
#     Тест на создание нового docpay КА нет
#     """
#     response = client.post(
#         "/DocPayment/Create/",
#         json={"doc_num": 2, "id_KA": 99123, "date_create":"2022-12-16T21:29:15.365Z","date":"2022-12-16T21:29:15.365Z"}
#     )
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == "этого КА не существует"

# def test_create_DP_NEG_2():
#     """
#     Тест на создание нового docpay док уже есть
#     """
#     response = client.post(
#         "/DocPayment/Create/",
#         json={"doc_num": 1, "id_KA": 123, "date_create":"2022-12-16T21:29:15.365Z","date":"2022-12-16T21:29:15.365Z"}
#     )
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == "payment document already exists"

# def test_DP_get_by_num():
#     """
#     Проверка получения документа по его номеру
#     """
#     response = client.get("/DocPayment/ReadByNum/?doc_num=1")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["id_KA"] == 123

# def test_DP_not_found():
#     """
#     Проверка случая, если docpay с таким id отсутствует в БД
#     """
#     response = client.get("/DocPayment/ReadByNum/?doc_num=999")
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == "dp not exist"


# def test_DP_get_by_ka():
#     """
#     Проверка получения документа по его ka
#     """
#     response = client.get("/DocPayment/ReadByKA/?id_KA=123")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data[0]["id_KA"] == 123

# def test_DP_ka_not_found():
#     """
#     Проверка случая, если docpay с таким ka отсутствует в БД
#     """
#     response = client.get("/DocPayment/ReadByKA/?id_KA=999")
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == "dp not exist"

# def test_dp_get_all():
#     """
#     Проверка на получение всех дп - УСПЕХ
#     """
#     response = client.get("/DocPayment/ReadAll/?skip=0&limit=100")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data[0]["id_KA"] == 123

# # +=================+
# # |    FURNITURE    |
# # +=================+

# def test_create_FM():
#     """
#     Тест на создание нового fm УСПЕХ
#     """
#     response = client.post(
#         "/FurnitureModel/Create/",
#         json={"furn_model_name": "fm1", "furn_model": "fm-1", "characteristics":"ch","price":1}
#     )
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["furn_model_name"] == "fm1"
#     assert data["furn_model"] == "fm-1"
#     assert data["characteristics"] == "ch"
#     assert data["price"] == 1

# def test_create_FM_NEG():
#     """
#     Тест на создание нового FM нет
#     """
#     response = client.post(
#         "/FurnitureModel/Create/",
#         json={"furn_model_name": "fm1", "furn_model": "fm-1", "characteristics":"ch","price":1}
#     )
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == "furniture model already exists"

# def test_fm_get():
#     """
#     Проверка получения fm
#     """
#     response = client.get("/FurnitureModel/ReadByModel/?furn_model=fm-1")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["furn_model_name"] == "fm1"
#     assert data["furn_model"] == "fm-1"
#     assert data["characteristics"] == "ch"
#     assert data["price"] == 1

# def test_fm_not_found():
#     """
#     Проверка случая, если docpay с таким ka отсутствует в БД
#     """
#     response = client.get("/FurnitureModel/ReadByModel/?furn_model=fm-2")
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == "furniture model not found"

# def test_fm_get_all():
#     """
#     Проверка на получение всех fm - УСПЕХ
#     """
#     response = client.get("/FurnitureModel/ReadAll/?skip=0&limit=100")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data[0]["furn_model_name"] == "fm1"
#     assert data[0]["furn_model"] == "fm-1"
#     assert data[0]["characteristics"] == "ch"
#     assert data[0]["price"] == 1


# # +=================+
# # |     PAYMENT     |
# # +=================+

# def test_create_pay_positive():
#     """
#     Тест на создание нового fpeyment УСПЕХ
#     """
#     response = client.post(
#         "/Payment/Create/",
#         json={"id_payment": 1, "doc_num": 1, "furn_name":"string","furn_model":"fm-1","amount":1}
#     )
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["amount"] == 1
#     assert data["id_payment"] == 1
#     assert data["doc_num"] == 1
#     assert data["furn_model"] == "fm-1"

# def test_create_pay_negative_1():
#     """
#     Тест на создание нового fpeyment провал
#     """
#     response = client.post(
#         "/Payment/Create/",
#         json={"id_payment": 1, "doc_num": 1, "furn_name":"string","furn_model":"fm-1","amount":1}
#     )
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == "payment already exists"

# def test_create_pay_negative_2():
#     """
#     Тест на создание нового fpeyment провал
#     """
#     response = client.post(
#         "/Payment/Create/",
#         json={"id_payment": 2, "doc_num": 999, "furn_name":"string","furn_model":"fm-1","amount":1}
#     )
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == "have no doc by this num"

# def test_create_pay_negative_3():
#     """
#     Тест на создание нового fpeyment провал
#     """
#     response = client.post(
#         "/Payment/Create/",
#         json={"id_payment": 2, "doc_num": 1, "furn_name":"string","furn_model":"kjbjnjnjnj","amount":1}
#     )
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == "have no model by this num"

# def test_pay_get_all():
#     """
#     Проверка на получение всех payment - УСПЕХ
#     """
#     response = client.get("/Payment/ReadAll/")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data[0]["amount"] == 1
#     assert data[0]["id_payment"] == 1
#     assert data[0]["doc_num"] == 1
#     assert data[0]["furn_model"] == "fm-1"

# def test_pay_get_id():
#     """
#     Проверка на получение payment by id - УСПЕХ
#     """
#     response = client.get("/Payment/ReadPayment/?id_pay=1")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["id_payment"] == 1
#     assert data["doc_num"] == 1
#     assert data["furn_model"] == "fm-1"
#     assert data["amount"] == 1

# def test_pay_get_id_neg():
#     """
#     Проверка на получение payment by id - negative
#     """
#     response = client.get("/Payment/ReadPayment/?id_pay=99")
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == 'no pay by this id'

# def test_pay_get_doc():
#     """
#     Проверка на получение payment by id - УСПЕХ
#     """
#     response = client.get("/Payment/ReadByDoc/?doc_num=1")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data[0]["id_payment"] == 1
#     assert data[0]["doc_num"] == 1
#     assert data[0]["furn_model"] == "fm-1"
#     assert data[0]["amount"] == 1

# def test_pay_get_doc_neg():
#     """
#     Проверка на получение payment by id - negative
#     """
#     response = client.get("/Payment/ReadByDoc/?doc_num=99")
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == 'hove no pay by this doc'

# def test_pay_get_fm():
#     """
#     Проверка на получение payment by id - УСПЕХ
#     """
#     response = client.get("/Payment/ReadByFurnitureModel/?model=fm-1")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data[0]["id_payment"] == 1
#     assert data[0]["doc_num"] == 1
#     assert data[0]["furn_model"] == "fm-1"
#     assert data[0]["amount"] == 1

# def test_pay_get_fm_neg():
#     """
#     Проверка на получение payment by id - negative
#     """
#     response = client.get("/Payment/ReadByFurnitureModel/?furn_model=fm-1")
#     assert response.status_code == 400, response.text
#     data = response.json()
#     assert data["detail"] == 'no pay by this model'

