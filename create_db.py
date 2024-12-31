import os
import MySQLdb
from django.conf import settings
import sys

# Asegúrate de que Django cargue las configuraciones
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_catalog.settings')


def create_database():
    try:
        # Conectar a MySQL sin especificar una base de datos
        db = MySQLdb.connect(
            host=settings.DATABASES['default']['HOST'],
            user=settings.DATABASES['default']['USER'],
            passwd=settings.DATABASES['default']['PASSWORD']
        )
        cursor = db.cursor()

        # Crear la base de datos si no existe
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{settings.DATABASES['default']['NAME']}`")
        db.commit()
        print(f"Base de datos '{settings.DATABASES['default']['NAME']}' verificada o creada.")
    except MySQLdb.Error as e:
        print(f"Error al crear la base de datos: {e}")
        sys.exit(1)
    finally:
        try:
            cursor.close()
            db.close()
        except UnboundLocalError:
            pass  # Si cursor no fue definido, no hacemos nada


if __name__ == "__main__":
    create_database()
