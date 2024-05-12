
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_predict_endpoint_with_valid_text():
    item = {"text": "Я очень доволен этим продуктом!"}
    response = client.post("/predict/", json=item)
    assert response.status_code == 200
    # Проверяем, что ответ содержит ожидаемый результат анализа тональности
    # Здесь предполагается, что классификатор возвращает словарь с полями 'label' и 'score'
    # Например: {'label': 'POSITIVE', 'score': 0.9}
    assert isinstance(response.json(), dict)
    assert 'label' in response.json()
    assert 'score' in response.json()

def test_predict_endpoint_with_invalid_text():
    item = {"text": ""}  # Пустой текст
    response = client.post("/predict/", json=item)
    assert response.status_code == 200
    # Проверяем, что ответ содержит ожидаемый результат анализа тональности
    # Здесь предполагается, что классификатор возвращает словарь с полями 'label' и 'score'
    assert isinstance(response.json(), dict)
    assert 'label' in response.json()
    assert 'score' in response.json()



