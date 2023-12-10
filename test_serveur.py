from fastapi.testclient import TestClient
from server.api import app
from server.database import engine
from sqlalchemy.orm import sessionmaker
import unittest
from server.models import Base

def setup_module(module):
    Base.metadata.create_all(bind=engine)

def teardown_module(module):
    Base.metadata.drop_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
client = TestClient(app)

class TestServer(unittest.TestCase):
    def test_get_artist(self):
        response = client.get("/artists/1")
        assert response.status_code == 200

    def test_get_album(self):
        response = client.get("/albums/1")
        assert response.status_code == 200

    def test_get_track(self):
        response = client.get("/tracks/1")
        assert response.status_code == 200
