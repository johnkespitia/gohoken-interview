import unittest
from requests import Response
from app.cache import process_image_cache

class ProcessImageCacheTestCase(unittest.TestCase):
    def test_process_image_cache(self):
        # Crear una respuesta simulada con datos de imágenes
        response = Response()
        response.status_code = 200
        response._content = b'{"photos":[{"description":"...","url":"https://api.slingacademy.com/public/sample-photos/25.jpeg","title":"Certainly than need enjoy understand right","user":15,"id":25}]}'

        # Llamar a la función para procesar la caché de imágenes
        result = process_image_cache(response)

        # Verificar los resultados esperados
        expected_result = [
            ("https://api.slingacademy.com/public/sample-photos/25.jpeg", "Certainly than need enjoy understand right"),
            ("https://api.slingacademy.com/public/sample-photos/asd.jpeg", "Failed Image 1"),
            ("https://api.slingacademy.com/public/sample-photos/dsa.jpeg", "Failed Image 2"),
            ("https://api.slingacademy.com/public/sample-photos/sad.jpeg", "Failed Image 3")
        ]
        self.assertEqual(len(result),4)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()