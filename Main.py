"""The first step is to create an SMTP object, each object is used for connection
with one server."""
# I'm learning python with pythonforbeginners
# REMEMBER TO SWITCH ON UNKNOWN FOR GOOGLE APPLICATIONS ON GMAIL TO AVOID THE SITUATION WHEN THIS ATTEMPT TO LOGIN IS REJECTED

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "xyz@gmail.com"
toaddr = "xxx@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python email"

body = "Python test mail. I'm learning how to send e-mail using Python."
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
# server.connect("smtp.gmail.com", 465) // THIS IS A PROBLEM, IT DISTURBS COMMUNICATION
server.ehlo()
server.starttls()
server.ehlo()
server.login("xyz@gmail.com", "password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)