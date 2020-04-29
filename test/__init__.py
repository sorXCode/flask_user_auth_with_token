from unittest import TestCase
from flask_app import app, db
from config import config

class BaseAPITestCase(TestCase):
    user_data = {
            "email": "testUser@test.com",
            "password": "test123"
        }

    def setUp(self):
        super().setUp()
        app.config.from_object(config['test'])
        self.app_context = app.app_context()
        self.app_context.push()
        self.app = app.test_client()
        
    def tearDown(self):
        super().tearDown()
        self.app_context.pop()
