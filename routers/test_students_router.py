from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)
# A student can be created successfully
def test_create_student():
    response = client.post('/students', json={'first_name': 'John', 'last_name': 'Doe', 'age': 10})
    assert response.status_code == 201
    assert response.json() == {
        'messages': 'Student created successfully.', 'data': {
            'first_name': 'John', 'last_name': 'Doe', 'age': 10
        }
    }

# All students can be fetched
def test_get_all_students():
    response = client.get('/students')
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_edit_student():
    response = client.put('/students/John', json={'first_name': 'John', 'last_name': 'Doe', 'age': 20})
    assert response.status_code == 200
    assert response.json() == {'message': 'Success', 'data': {'first_name': 'John', 'last_name': 'Doe', 'age': 20}}

def test_edit_student_not_found():
    response = client.put('/students/Janet', json={'first_name': 'John', 'last_name': 'Doe', 'age': 20})
    assert response.status_code == 404
    assert response.json() == {'detail': 'Student not found.'}
    