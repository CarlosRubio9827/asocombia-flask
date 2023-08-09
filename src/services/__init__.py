from src.database import Database
import logging

# Configurar el logger
logging.basicConfig(filename='baseDatos.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Configurar el codificador para manejar las tildes
logging.getLogger().handlers[0].setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger = logging.getLogger(__name__)

class serviceSendEmail:
    def sendEmail(app, nombre, email, mensaje):
        try:
            db = Database(app)
            query = """INSERT INTO messages (name,email,message_description) VALUES (%s,%s,%s)"""
            values = (nombre, email, mensaje)
            cur = db.execute_query(query, values)
            app.logger.info("Mensaje insertado en la base de datos correctamente: Nombre=%s, Email=%s", nombre, email)    
        except Exception as e:
            app.logger.error("Error en la conexion a BD %s", e) 
         