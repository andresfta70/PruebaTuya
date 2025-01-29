import unittest
import os
import shutil
from html_processor import process_html, process_directory


class TestHTMLProcessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Crear un entorno de prueba con archivos HTML e imágenes
        cls.test_dir = 'test_directory'
        os.makedirs(cls.test_dir, exist_ok=True)

        # Crear un archivo HTML de prueba
        cls.html_content = """
        <html>
            <body>
                <img src="image1.png">
                <img src="image2.png">
            </body>
        </html>
        """
        cls.html_file_path = os.path.join(cls.test_dir, 'test.html')
        with open(cls.html_file_path, 'w', encoding='utf-8') as f:
            f.write(cls.html_content)

        # Crear imágenes de prueba
        cls.image1_path = os.path.join(cls.test_dir, 'image1.png')
        cls.image2_path = os.path.join(cls.test_dir, 'image2.png')
        with open(cls.image1_path, 'wb') as f:
            f.write(b'fake_image_data1')
        with open(cls.image2_path, 'wb') as f:
            f.write(b'fake_image_data2')

    @classmethod
    def tearDownClass(cls):
        # Eliminar el entorno de prueba
        shutil.rmtree(cls.test_dir)

    def test_process_html(self):
        # Procesar el archivo HTML
        result = process_html(self.html_file_path)
        self.assertTrue(result['success'])
        self.assertEqual(len(result['processed_images']), 2)

        # Verificar que se creó un nuevo archivo HTML
        new_html_file_path = self.html_file_path.replace('.html', '_base64.html')
        self.assertTrue(os.path.exists(new_html_file_path))

        # Leer el nuevo archivo HTML y verificar que las imágenes fueron reemplazadas
        with open(new_html_file_path, 'r', encoding='utf-8') as f:
            new_content = f.read()
            self.assertIn('data:image/png;base64,', new_content)

    def test_process_directory(self):
        # Procesar el directorio de prueba
        results = process_directory(self.test_dir)
        self.assertEqual(len(results), 1)
        self.assertTrue(results[0]['success'])


if __name__ == "__main__":
    unittest.main()