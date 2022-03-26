import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("shreshthatechd@gmail.com", "Deetech#3")
server.sendmail('shreshthatechd@gmial.com', 'deekshakulshrestha11@gmail.com', "Hello")
server.quit()