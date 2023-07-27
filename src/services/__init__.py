from src.database import Database

class serviceSendEmail:
    def sendEmail(app):
        try:
            db = Database(app)
            cur = db.execute_query("SELECT * FROM asocombia")
            res = db.fetch_all(cur)
            print(res)
        except Exception as e:
            print ("error en la conexion ", e) 
        