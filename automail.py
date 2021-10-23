import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('ravi21@gmail.com','hope you well there')
server.sendmail('ravi21@gmail.com','saitilak2002@gmail.com','hi dude im ok here i hope you safe there and very pleasant to talk with my dear.and one more thing')

