from src.database import Database

class serviceSendEmail:
    def sendEmail(app, nombre, email, mensaje):
        try:
            db = Database(app)
            query = """INSERT INTO messages (name,email,message_description) VALUES (%s,%s,%s)"""
            values = (nombre, email, mensaje)
            cur = db.execute_query(query, values)
            # print("este es el cur: ",cur)
            # res = db.fetch_all(cur)
        except Exception as e:
            print ("error en la conexion ", e) 
         