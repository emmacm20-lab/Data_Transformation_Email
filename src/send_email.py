# 📂 src/send_email.py - Envío de correos con reportes

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    from_email = "tuemail@ejemplo.com"
    to_email = "destinatario@ejemplo.com"
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Reporte de Ventas"
    with open("report.html", "r") as f:
        body = f.read()
    msg.attach(MIMEText(body, 'html'))
    server = smtplib.SMTP("smtp.ejemplo.com", 587)
    server.starttls()
    server.login("usuario", "contraseña")
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()
    print("Correo enviado.")

if __name__ == "__main__":
    send_email()
