from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_api_works():
    with open("sample_questions.txt", "w") as f:
        f.write("Test question")
    with open("sample_questions.txt", "rb") as q_file:
        response = client.post("/", files={"questions": q_file})
    assert response.status_code == 200
