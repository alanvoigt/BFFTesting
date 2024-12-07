import pytest
import requests

BFF_URL = "http://127.0.0.1:5000/api/data"
USER_SERVICE_URL = "http://127.0.0.1:5001/users"
ORDER_SERVICE_URL = "http://127.0.0.1:5002/orders"

@pytest.fixture
def mock_user_service_response():
    return {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

@pytest.fixture
def mock_order_service_response():
    return [
        {"order_id": 101, "product": "Laptop", "quantity": 1},
        {"order_id": 102, "product": "Mouse", "quantity": 2},
    ]

def test_bff_integration():
    # Faça uma chamada real para o endpoint do BFF
    response = requests.get(BFF_URL)
    assert response.status_code == 200

    # Espera-se que a resposta seja uma combinação das respostas de ambos os microserviços
    expected_response = {
        "user": {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        },
        "orders": [
            {"order_id": 101, "product": "Laptop", "quantity": 1},
            {"order_id": 102, "product": "Mouse", "quantity": 2}
        ]
    }

    # Validar a resposta combinada
    assert response.json() == expected_response
