import unittest
from unittest.mock import MagicMock, patch

from app.cache import generate_image_cache
from app.redis import redis_client

class GenerateImageCacheTestCase(unittest.TestCase):
    @patch("app.redis.redis_client", redis_client)
    @patch("app.cache.session.get")
    def test_generate_image_cache(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "photos": [
                {
                    "url": "https://example.com/image1.jpg",
                    "title": "Image 1",
                },
                {
                    "url": "https://example.com/image2.jpg",
                    "title": "Image 2",
                },
            ]
        }
        mock_get.return_value = mock_response

        result = generate_image_cache()
        offset = len(result)-5
        self.assertEqual(result[offset][0], "https://example.com/image1.jpg")
        self.assertEqual(result[offset][1], "Image 1")
        self.assertEqual(result[offset+1][0], "https://example.com/image2.jpg")
        self.assertEqual(result[offset+1][1], "Image 2")
        self.assertEqual(result[offset+2][0], "https://api.slingacademy.com/public/sample-photos/asd.jpeg")
        self.assertEqual(result[offset+2][1], "Failed Image 1")
        self.assertEqual(result[offset+3][0], "https://api.slingacademy.com/public/sample-photos/dsa.jpeg")
        self.assertEqual(result[offset+3][1], "Failed Image 2")
        self.assertEqual(result[offset+4][0], "https://api.slingacademy.com/public/sample-photos/sad.jpeg")
        self.assertEqual(result[offset+4][1], "Failed Image 3")
        self.assertEqual(len(mock_get.call_args_list), 1)
        self.assertEqual(
            mock_get.call_args_list[0][0][0],
            f"https://api.slingacademy.com/v1/sample-data/photos?offset={offset}&limit=20",
        )

if __name__ == "__main__":
    unittest.main()
