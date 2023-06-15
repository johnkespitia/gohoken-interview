import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_images(self):
        with patch('app.main.generate_image_cache') as mock_generate_image_cache:
            mock_generate_image_cache.return_value = [('https://example.com/image1.jpg', 'Title 1'), ('https://example.com/image2.jpg', 'Title 2')]
            response = self.client.get("/images")
            mock_generate_image_cache.assert_called_once()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), [
                ['https://example.com/image1.jpg', 'Title 1'],
                ['https://example.com/image2.jpg', 'Title 2']
            ])


if __name__ == '__main__':
    unittest.main()
