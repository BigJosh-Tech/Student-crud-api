import unittest
from app import app, db

class TestStudentAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_healthcheck(self):
        response = self.app.get('/api/v1/healthcheck')
        self.assertEqual(response.status_code, 200)
