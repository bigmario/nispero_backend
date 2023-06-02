from .db_mock import test_db, test_client

client = test_client

subscription = {
    "email": "testuser@mail.com"
}


def test_home(test_db):
    """
    Assert home endopoint
    """
    response = client.get("/", headers={"Accept": "application/json"})
    assert response.status_code == 200
    assert response.json() == {
        "Framework": "FastAPI",
        "Message": "Welcome To Nispero API !!",
    }