import os
import base64
import re


def read_file(file_path, mode='r', encoding='utf-8'):
    """
    Lee un archivo y devuelve su contenido.

    Args:
        file_path (str): Ruta del archivo.
        mode (str): Modo de apertura del archivo.
        encoding (str): Codificación del archivo.

    Returns:
        str: Contenido del archivo.
    """
    with open(file_path, mode, encoding=encoding) as file:
        return file.read()


def write_file(file_path, content, mode='w', encoding='utf-8'):
    """
    Escribe contenido en un archivo.

    Args:
        file_path (str): Ruta del archivo.
        content (str): Contenido a escribir.
        mode (str): Modo de apertura del archivo.
        encoding (str): Codificación del archivo.
    """
    with open(file_path, mode, encoding=encoding) as file:
        file.write(content)


def convert_image_to_base64(image_path):
    """
    Convierte una imagen a base64.

    Args:
        image_path (str): Ruta de la imagen.

    Returns:
        str: Imagen en formato base64.
    """
    with open(image_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')


def process_html(file_path):
    """
    Procesa un archivo HTML para convertir las imágenes a base64.

    Args:
        file_path (str): Ruta del archivo HTML.

    Returns:
        dict: Resultados del procesamiento.
    """
    try:
        content = read_file(file_path)
        images = re.findall(r'<img[^>]+src="([^">]+)"', content)
        processed_images = []

        for img in images:
            try:
                img_path = os.path.join(os.path.dirname(file_path), img)
                img_base64 = convert_image_to_base64(img_path)
                content = content.replace(f'src="{img}"', f'src="data:image/png;base64,{img_base64}"')
                processed_images.append(img)
            except Exception as e:
                print(f"Error processing image {img}: {e}")

        new_file_path = file_path.replace('.html', '_base64.html')
        write_file(new_file_path, content)

        return {'success': True, 'file_path': file_path, 'processed_images': processed_images}
    except Exception as e:
        return {'success': False, 'file_path': file_path, 'error': str(e)}


def process_directory(directory_path):
    """
    Procesa todos los archivos HTML en un directorio.

    Args:
        directory_path (str): Ruta del directorio.

    Returns:
        list: Resultados del procesamiento.
    """
    results = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.html'):
                full_path = os.path.join(root, file)
                results.append(process_html(full_path))
    return results


def main(paths):
    """
    Función principal que procesa las rutas proporcionadas.

    Args:
        paths (list): Lista de rutas de archivos o directorios.
    """
    results = {'success': [], 'fail': []}
    for path in paths:
        if os.path.isfile(path) and path.endswith('.html'):
            result = process_html(path)
            if result['success']:
                results['success'].append(result)
            else:
                results['fail'].append(result)
        elif os.path.isdir(path):
            directory_results = process_directory(path)
            for res in directory_results:
                if res['success']:
                    results['success'].append(res)
                else:
                    results['fail'].append(res)

    print(results)


if __name__ == "__main__":
    paths = ['path/to/file.html', 'path/to/directory']
    main(paths)
