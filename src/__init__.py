from flask import Flask, render_template, request
from src.services import serviceSendEmail

app = Flask(__name__)

def init_app(config):
    app.config.from_object(config)
    return app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobrenosotros')
def aboutUs():
    return render_template('about.html')

@app.route('/contacto')
def contact():
    return render_template('contact.html', isMessage=False)

@app.route('/contacto', methods=['POST'])
def getInfoForm():
    try:
        nombre = request.form["nombre"]
        email = request.form["email"]
        mensaje = request.form["mensaje"]
        se = serviceSendEmail
        se.sendEmail(app, nombre, email, mensaje)
        return render_template('contact.html', isMessage=True, message=f"¡Gracias por tu mensaje, {nombre}!")
    except Exception as e:
        return render_template('contact.html', isMessage=True, message=f"Hubo un error en el proceso. Por favor {nombre}, intenta nuevamente más tarde.")


@app.errorhandler(500)
def base_error_handler(e):
    return render_template('500.html'), 500
@app.errorhandler(404)
def error_404_handler(e):
    return render_template('404.html'), 404

