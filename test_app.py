from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 500
    assert response.get_json() == {"status": "ok"}


def test_add_book():
    client = app.test_client()

    response = client.post(
        "/books/add",
        data={
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "genre": "Fiction"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True
    assert data["book"]["title"] == "The Great Gatsby"


def test_add_book_invalid():
    client = app.test_client()

    response = client.post(
        "/books/add",
        data={
            "title": "",
            "author": "",
            "genre": ""
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["success"] is False
