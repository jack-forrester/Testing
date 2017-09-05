import bs4 as bs
import urllib
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

#Open up beatiful soup
sauce = urllib.urlopen('http://yspl.play-cricket.com/website/web_pages/221190').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
listofteams = soup.find_all('p')

print(listofteams)
i = []
for teams in listofteams:
	team = teams.text
	if i == 'true':
		frodframe = teams
		frod = frodframe.find('iframe').get('src')
		print(frod)
		i = []
	if 'APPLEBY' not in team:
		continue
	else:
		i = 'true'

frod = frodframe.find('iframe').get('src')
frod = 'hi'
msg = header + frod

print(msg)
server.sendmail(From, To, msg)
server.quit()
