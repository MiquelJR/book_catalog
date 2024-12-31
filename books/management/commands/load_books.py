import os
import xml.etree.ElementTree as ET
from books.models import Book
from django.db import IntegrityError
from datetime import datetime


def load_books_from_xml():
    """
    Carga libros desde el archivo XML a la base de datos.
    """
    xml_file = os.path.join(os.path.dirname(__file__), 'data', 'books.xml')  # Ajusta la ruta si es necesario
    if not os.path.exists(xml_file):
        print(f"El archivo {xml_file} no existe.")
        return

    # Parsear el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for book_elem in root.findall('book'):  # Los libros están dentro de 'book'
        book_id = book_elem.get('id')  # ID es un atributo del libro
        author = book_elem.find('author').text
        title = book_elem.find('title').text
        genre = book_elem.find('genre').text
        price = book_elem.find('price').text
        publish_date = book_elem.find('publish_date').text
        description = book_elem.find('description').text

        # Convertir los datos según sea necesario (por ejemplo, fecha y precio)
        try:
            publish_date = datetime.strptime(publish_date, "%Y-%m-%d").date()  # Formato de la fecha
            price = float(price)  # Convertir precio a número flotante

            # Crear el libro en la base de datos
            Book.objects.create(
                id=book_id,
                author=author,
                title=title,
                genre=genre,
                price=price,
                publish_date=publish_date,
                description=description
            )
            print(f"Libro '{title}' cargado correctamente.")
        except IntegrityError:
            print(f"El libro '{title}' ya existe en la base de datos.")
        except Exception as e:
            print(f"Error al cargar el libro '{title}': {e}")


def main():
    # Llamamos a la función para cargar los libros
    load_books_from_xml()
