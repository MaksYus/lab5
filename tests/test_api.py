from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app, get_db
from src.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Тестовая БД

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)  # Удалем таблицы из БД
Base.metadata.create_all(bind=engine)  # Создаем таблицы в БД


def override_get_db():
    """
    Данная функция при тестах будет подменять функцию get_db() в main.py.
    Таким образом приложение будет подключаться к тестовой базе данных.
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db  # Делаем подмену

client = TestClient(app)  # создаем тестовый клиент к нашему приложению


def test_create_KA():
    """
    Тест на создание нового КА
    """
    response = client.post(
        "/KA/Create/",
        json={"id_KA": 123, "name": "петя", "adress":"ул.пушкниа","phone_number":"9999"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "петя"


def test_create_exist_KA():
    """
    Проверка случая, когда мы пытаемся добавить существующего КА
    в БД, т.е. когда данный id уже присутствует в БД.
    """
    response = client.post(
        "/KA/Create/",
        json={"id_KA": 123, "name": "петя", "adress":"ул.пушкниа","phone_number":"9999"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "KA already exists"


def test_get_all_KA():
    """
    Тест на получение списка КА из БД
    """
    response = client.get("/KA/ReadAll/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["name"] == "петя"


def test_get_KA_by_id():
    """
    Тест на получение KA из БД по его id
    """
    response = client.get("/KA/ReadByID/?id_KA=123")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "петя"


def test_KA_not_found():
    """
    Проверка случая, если KA с таким id отсутствует в БД
    """
    response = client.get("/KA/ReadByID/?id_KA=999")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "KA not found"