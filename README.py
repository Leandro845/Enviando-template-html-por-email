# Enviando-template-html-por-email
Enviando um template básico html por email
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


email = 'email' #Source email
password = 'password' #Source password

#Opening the html template
with open('template.html', 'r') as html:
    template = Template(html.read())
    nomear = template.substitute(test='test')

#Head
menssagem = MIMEMultipart()
menssagem['from'] = '...' #Source host
menssagem['to'] = '...' #Destination email
menssagem['subject'] = '...' #Email title


msg = MIMEText(nomear, 'html')
menssagem.attach(msg)


with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as smtp:
    smtp.ehlo() #Sending a hello to the server
    smtp.login(email, password) #Login
    smtp.send_message(menssagem) #Submitting to the template

