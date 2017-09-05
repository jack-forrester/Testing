import bs4 as bs
import urllib

#Open up beatiful soup
mainscoressauce = urllib.urlopen('http://yspl.play-cricket.com/website/web_pages/221190').read()
livescores = bs.BeautifulSoup(mainscoressauce, 'lxml')
listofteams = livescores.find_all('p')

print(listofteams)
i = []
for teams in listofteams:
	if i == 'true':
		frodframe = teams
		frodurl = frodframe.find('iframe').get('src')
		i = []
	team = teams.text
	if 'APPLEBY' not in team:
		continue
	else:
		i = 'true'

print(frodurl)

widgetsauce = urllib.urlopen(frodurl)
widget = bs.BeautifulSoup(widgetsauce, 'lxml')

print(widget)
