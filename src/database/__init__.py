from flask_mysqldb import MySQL
from decouple import config
import pymysql


class Database:
    def __init__(self, app):
        app.config["MYSQL_HOST"] = config('MYSQL_HOST')
        app.config["MYSQL_PORT"] = config('MYSQL_PORT')
        app.config["MYSQL_USER"] =config('MYSQL_USER')
        app.config["MYSQL_PASSWORD"] =config('MYSQL_PASSWORD')
        app.config["MYSQL_DB"] = config('MYSQL_DB')
        self.connection = pymysql.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            db=app.config['MYSQL_DB']
        )

        if pymysql.Error is not None:
            print("Conexión a la base de datos establecida correctamente.")
        else:
            print("¡Error al establecer la conexión a la base de datos!")

    def execute_query(self, query, values):
        
        cur = self.connection.cursor()
        cur.execute(query, values)
        data = cur.fetchall()
        self.connection.commit()
        cur.close()
        return cur

    def fetch_all(self, cur):
        rv = cur.fetchall()
        cur.close()
        return rv

