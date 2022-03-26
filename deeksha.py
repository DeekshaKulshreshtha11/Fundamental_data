import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("emailId", "password")
server.sendmail('From', 'To', "Message")
server.quit()