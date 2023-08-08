from flask_mysqldb import MySQL
from decouple import config
import pymysql
from flask_mail import Mail, Message
from smtplib import SMTPException
from threading import Thread
from flask import current_app



class Database:
    def __init__(self, app):
        app.config["MYSQL_HOST"] = config('MYSQL_HOST')
        app.config["MYSQL_PORT"] = config('MYSQL_PORT')
        app.config["MYSQL_USER"] =config('MYSQL_USER')
        app.config["MYSQL_PASSWORD"] =config('MYSQL_PASSWORD')
        app.config["MYSQL_DB"] = config('MYSQL_DB')
        app.config["MAIL_SERVER"] = config('MAIL_SERVER')
        app.config["MAIL_PORT"] = config('MAIL_PORT')
        app.config["MAIL_USERNAME"] =config('MAIL_USERNAME')
        app.config["MAIL_PASSWORD"] =config('MAIL_PASSWORD')
        app.config["DONT_REPLY_FROM_EMAIL"] =config('DONT_REPLY_FROM_EMAIL')
        app.config["ADMINS"] =config('ADMINS')
        app.config["MAIL_USE_TLS"] = config('MAIL_USE_TLS')
        # Copnexion a la BD
        self.connection = pymysql.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            db=app.config['MYSQL_DB']
        )

        self.mail= Mail(app)
        self.app = app

        if pymysql.Error is not None:
            print("Conexión a la base de datos establecida correctamente.")
        else:
            print("¡Error al establecer la conexión a la base de datos!")

    
    def _send_async_email(self, msg):
        with self.app.app_context():
            try:
                self.mail.send(msg)
            except SMTPException as e:
                print("¡Error en el envío del correo! ", str(e))

    def execute_query(self, query, values):
        recipient = config('RECIPIENT_MAIL')
        cur = self.connection.cursor()
        cur.execute(query, values)
        data = cur.fetchall()
        self.connection.commit()
        cur.close()
        msg = Message('Nuevo mensaje en la página de Asocombia', sender = ('Info Asocombia','info@asocombia.com'), recipients = [recipient])
        msg.body = "This is the email body"
        msg.html = f"<ul style='list-style-type: none;'><li><strong>Nombre:</strong> {values[0]}</li><li><strong>Email:</strong> {values[1]}</li><li><strong>Mensaje:</strong> {values[2]}</li></ul>"
       
        Thread(target=self._send_async_email, args=(msg, )).start()
       
        return cur

    def fetch_all(self, cur):
        rv = cur.fetchall()
        cur.close()
        return rv

