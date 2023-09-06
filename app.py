from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import Config

config = Config()
config.read('.env')

app = Flask(__name__)

smtp_server = "smtp.gmail.com"
smtp_port = 587  # Puerto TLS

remiteEmail = "REMITENTE"
remitePass = "REMITENTE_PASS" #reemplazar por sistema de encriptacion.

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/contacto", methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        empresa = request.form['empresa']
        telefono = request.form['telefono']
        planes = request.form['planes']

        # Crea el mensaje de correo
        msg = MIMEMultipart()
        msg['From'] = remiteEmail
        msg['To'] = 'nunez.iba@gmail.com'
        msg['Subject'] = 'Solicitud Contacto EstateBox'
        msg.attach(MIMEText(empresa, 'plain')) #modificar luego para enviar todos los datos o campos del formulario

        # Inicia la conexión SMTP y envía el correo
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(remiteEmail, remitePass)
            #envio
            server.sendmail(remiteEmail, 'nunez.iba@gmail.com', msg.as_string())
            server.quit()

            return 'Correo enviado con éxito'
        except Exception as e:
            return 'Error al enviar el correo: ' + str(e)

if __name__ == '__main__':
    app.run(debug=True)
