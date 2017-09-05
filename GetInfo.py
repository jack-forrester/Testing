import smtplib

#Open server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("jackforrester23@gmail.com", "030994Jf")

#Email formalities
From = 'jackforrester23@gmail.com'
To = 'jackforrester23@gmail.com'
Subject = "Jackkkkyyyyy"
header = 'To:' + From + '\n' + 'From:' + From + '\n' + 'Subject:' + Subject +'\n'

msg = header
server.sendmail(From, To, msg)
