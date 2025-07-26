from flask import Flask, render_template, request, redirect, url_for, flash
from src.services import serviceSendEmail

app = Flask(__name__)

print('app init - ')


def init_app(config):
    app.config.from_object(config)
    se = serviceSendEmail
    se.sendEmail(app)

    return app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sobrenosotros')
def aboutUs():
    return render_template('about.html')


@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Obtener datos del formulario
        print("request.form", request.form)
        nombre = request.form.get('nombre', '')
        email = request.form.get('email', '')
        telefono = request.form.get('telefono', '')
        mensaje = request.form.get('mensaje', '')

        # Validar datos
        if not nombre or not email or not mensaje:
            flash('Por favor complete todos los campos obligatorios', 'error')
            return render_template('contact.html')

        # Procesar el formulario (aquí puedes enviar email, guardar en BD, etc.)
        try:
            # Ejemplo: enviar email usando tu servicio
            # serviceSendEmail.sendEmail(app, nombre, email, mensaje)
            print(
                f"Formulario recibido - Nombre: {nombre}, Email: {email}, Mensaje: {mensaje}")

            flash(
                '¡Mensaje enviado correctamente! Nos pondremos en contacto contigo pronto.', 'success')
            return redirect(url_for('contact'))

        except Exception as e:
            flash('Error al enviar el mensaje. Por favor intente nuevamente.', 'error')
            print(f"Error: {e}")
            return render_template('contact.html')

    # Si es GET, mostrar el formulario
    return render_template('contact.html')
