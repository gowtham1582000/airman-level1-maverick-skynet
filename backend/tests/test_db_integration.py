from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_course_db():

    response = client.get("/")
    assert response.status_code == 200