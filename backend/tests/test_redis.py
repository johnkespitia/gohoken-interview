import unittest
from unittest.mock import patch, call
from app.redis import store_image_cache, get_all_images

class RedisCacheTestCase(unittest.TestCase):
    @patch('app.redis.redis_client')
    def test_store_image_cache(self, mock_redis_client):
        url = "https://example.com/image.jpg"
        title = "Example Image"
        store_image_cache(url, title)

        mock_redis_client.set.assert_called_once_with(url, title)

    @patch('app.redis.redis_client')
    def test_get_all_images(self, mock_redis_client):
        keys = [b'https://example.com/image1.jpg', b'https://example.com/image2.jpg']
        values = [b'Title 1', b'Title 2']

        mock_redis_client.keys.return_value = keys
        mock_redis_client.get.side_effect = values

        expected_result = [
            ('https://example.com/image1.jpg', 'Title 1'),
            ('https://example.com/image2.jpg', 'Title 2')
        ]

        result = get_all_images()

        mock_redis_client.keys.assert_called_once_with('*')
        mock_redis_client.get.assert_has_calls([
            unittest.mock.call('https://example.com/image1.jpg'),
            unittest.mock.call('https://example.com/image2.jpg')
        ])

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
