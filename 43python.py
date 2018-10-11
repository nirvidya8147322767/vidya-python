import smtplib
s= smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("pandithnsbv27@gmail.com", "dancevidya")
message="hi"
s.sendmail("pandithnsbv27@gmail.com","syedafshana4812@gmail.com",message)
print("Sent")
s.quit()

