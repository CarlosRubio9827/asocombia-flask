from flask import Flask, render_template
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

@app.route('/contacto')
def contact():
    return render_template('contact.html')