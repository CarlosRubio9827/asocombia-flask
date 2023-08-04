from flask import Flask, render_template, request
from src.services import serviceSendEmail
from flask_mysqldb import MySQL

app = Flask(__name__)


def init_app(config):
    print('Config -- ',config)
    app.config.from_object(config)
    print('App -- ',app)

    # app.config["MYSQL_HOST"] = "localhost"
    # app.config["MYSQL_PORT"] = 3306
    # app.config["MYSQL_USER"] = "root"
    # app.config["MYSQL_PASSWORD"] = ""
    # app.config["MYSQL_DB"] = "asocombia"
    # mysql = MySQL(app)
    # print('mysql -- ',type(mysql))
    # cur = mysql.connection.cursor()
    # cur.execute("""SELECT * from messages""")
    # rv = cur.fetchall()
    # print[(rv)]
    #return str(rv)

    return app

@app.route('/')
def index():
    # se = serviceSendEmail
    # se.sendEmail(app)
    return render_template('index.html')

@app.route('/sobrenosotros')
def aboutUs():
    return render_template('about.html')

@app.route('/contacto')
def contact():
    return render_template('contact.html', isMessage=False)

@app.route('/contacto', methods=['POST'])
def getInfoForm():
    
    nombre = request.form["nombre"]
    email = request.form["email"]
    mensaje = request.form["mensaje"]
    print("nombre: ", nombre)
    print("email: ", email)
    print("mensaje: ", mensaje)
    se = serviceSendEmail
    se.sendEmail(app, nombre, email, mensaje)
    
    return render_template('contact.html', isMessage=True, message="¡Gracias por tu mensaje!")

@app.errorhandler(500)
def base_error_handler(e):
    return render_template('500.html'), 500
@app.errorhandler(404)
def error_404_handler(e):
    return render_template('404.html'), 404