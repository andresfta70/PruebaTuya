# Prueba Tuya

## Procesamiento de archivos HTML en Python

Consta de dos archivos: el primero es html_proccesor.py. Este script es el encargado de dar solución a los numerales propuestos. Dentro de este, se encontrará la explicación de cada objeto. El otro archivo es tests.py. Este script es el que contiene los test para probar el funcionamiento de html_processor.py. Para correr los test se recomienda ejecutar: python -m unittest test_html_processor.py.

## Preferencias de consumo

### Preprocesamiento de datos

La solución de este punto fue realizada con la versión 8.4.0 de MySQL. Para cargar los datos a MySQL, se hizo un preprocesamiento en Python. El notebook Preprocesamiento.ipynb toma el archivo de excel 'bd.xlsx' y genera tres archivos .csv: "CLIENTES.CSV", "TRANSACCIONES.CSV", "CATEGORIAS_CONSUMO.CSV". Estos son los tres archivos que cargamos al motor de base de datos. Al cargarlos, ejecutamos el script "Limpieza_datos.sql", que se encarga de transformar el tipo de datos de las fechas de 'text' a 'date'. Con esto, ya tenemos toda la parte de preprocesamiento.

Nota: El script 'Limpieza_datos.sql' lo desarollé debido a la máquina en la que trabajé. Si no se considera necesario, una vez cargados los archivos .csv se puede ejecutar directamente el script 'Preferencias_consumo.sql"

### Solución

El script que da solución a este punto es Preferencias_consumo.sql. La consulta que da solución a este punto usa tres parámetros: 'Fecha_desde', 'Fecha_hasta' y 'n'. Los primeros dos parámetros corresponden al intervalo de tiempo en el que vemos las fechas de las transacciones. El parámetro 'n' se refiere al filtro de las primeras n categorías de preferencia. La consulta tiene una sub-consulta en la que se hizo uso de una Window Function para extraer aquellas categorías en las que un cliente acumuló más cantidad de transacciones. La consulta más externa extrae la fecha de la última transacción en cada categoría preferida.
