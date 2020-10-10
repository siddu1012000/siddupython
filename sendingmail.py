import smtplib
m=smtplib.SMTP('smtp.gmail.com', 587)
m.starttls()
m.login("siddu1012000@gmail.com","1029384756")
content="whats up"
m.sendmail("siddu1012000@gmail.com","hemanthkori007@gmail.com",content)
print("Sent")
m.quit()
