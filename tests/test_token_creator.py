import unittest
from graphlit.token_creator import create_token

class TestTokenCreator(unittest.TestCase):
    def test_create_token(self):
        token = create_token()
        self.assertIsNotNone(token)

if __name__ == '__main__':
    unittest.main()
