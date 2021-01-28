import socket             
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

##Configuración->

#-Socket
ip = "" #IP a la que bindear el socket
puerto = 83 #Puerto a escuchar

#-Mail
mail = "@gmail.com" #Email desde el que se envía el aviso
mailPw = "" #Contraseña
mailR = "@gmail.com" #Email que recivirá el aviso
smtpIp = "smtp.gmail.com"
smtpPuerto = 587
aTitulo = "El Honeypot ha recibido una conexión" #Título del email de aviso
aContenido = "Conexión recibida en el honeypot desde " #Contenido del email de aviso, a continuación se adjunta la IP
espera = 60 #Segundos a esperar para volver a aceptar conexiones después de enviar el aviso

##<-Configuración

def avisoMail():
    m = MIMEMultipart()
    m['From'] = mail
    m['To'] = mailR
    m['Subject'] = aTitulo
    m.attach(MIMEText(aContenido + str(addr), 'plain'))
    sesion = smtplib.SMTP(smtpIp, smtpPuerto)
    sesion.starttls()
    sesion.login(mail, mailPw)
    text = m.as_string()
    sesion.sendmail(mail, mailR, text)
    sesion.quit()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, puerto))
s.listen(5)

while True:  
    c, addr = s.accept()
    avisoMail()
    c.close()
    time.sleep(espera)
