import unittest
from site_jujutsu.app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, World!", response.data)  # Ajuste conforme o conteúdo do index.html

if __name__ == "__main__":
    unittest.main()
