from django.apps import AppConfig
from django.db import connection
from django.db.utils import OperationalError

class BooksConfig(AppConfig):
    name = 'books'

    def ready(self):
        # Verificar si la base de datos está vacía y cargar los libros si es necesario
        if self.is_database_empty():
            from management.commands.load_books import main
            main()

    def is_database_empty(self):
        """
        Verifica si la tabla de libros está vacía.
        """
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM books_book")  # Reemplaza 'books_book' con el nombre de tu tabla
                count = cursor.fetchone()[0]
                return count == 0
        except OperationalError:
            print("Error al verificar la base de datos.")
            return False
