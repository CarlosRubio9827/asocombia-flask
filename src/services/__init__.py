from src.database import Database
from flask_mail import Mail

class serviceSendEmail:
    def sendEmail(app, nombre, email, mensaje):
        try:
            db = Database(app)
            mail = Mail()
            mail.init_app(app)
            query = """INSERT INTO messages (name,email,message_description) VALUES (%s,%s,%s)"""
            values = (nombre, email, mensaje)
            cur = db.execute_query(query, values)
            # print("este es el cur: ",cur)
            # res = db.fetch_all(cur)
        except Exception as e:
            print ("error en la conexion ", e) 
         