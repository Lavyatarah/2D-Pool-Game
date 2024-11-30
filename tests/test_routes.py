import unittest
from app import create_app, db

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_player(self):
        response = self.client.post("/players", json={"name": "John"})
        self.assertEqual(response.status_code, 201)

    def test_create_game(self):
        self.client.post("/players", json={"name": "John"})
        self.client.post("/players", json={"name": "Jane"})
        response = self.client.post("/games", json={"player1_id": 1, "player2_id": 2})
        self.assertEqual(response.status_code, 201)
