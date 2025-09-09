import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello from Flask on Kubernetes!")

    def test_load(self):
        response = self.client.get('/load')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "CPU load triggered!")

if __name__ == '__main__':
    unittest.main()
