import pytest
from fastapi.testclient import TestClient

import models
from database import SessionLocal
from main import app


@pytest.fixture(autouse=True)
def clean_db():
    """Empty the items table before and after every test so tests don't see each other's data."""
    db = SessionLocal()
    db.query(models.Item).delete()
    db.commit()
    db.close()
    yield
    db = SessionLocal()
    db.query(models.Item).delete()
    db.commit()
    db.close()


@pytest.fixture
def client():
    return TestClient(app)
