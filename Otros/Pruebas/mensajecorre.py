import smtplib
from email.message import EmailMessage

message= EmailMessage()

email_subject= "Email test from python"
sender_email_addres= "gabrieluezas@gmail.com"
receiver_email_addres= "gabrieluezas@gmail.com"

message['Subject'] = email_subject 
message['From'] = sender_email_addres 
message['To'] = receiver_email_addres

message.set_content("Hello from Python!")

email_smtp = "smtp.gmail.com"
server = smtplib.SMTP(email_smtp, '587')
server.ehlo()
server.starttls()

server.send_message

server.quit