import urllib
import bs4 as bs

def FindURL():
	#Open up beatiful soup
	mainscoressauce = urllib.urlopen('http://yspl.play-cricket.com/website/web_pages/221190').read()
	livescores = bs.BeautifulSoup(mainscoressauce, 'lxml')

	#each team and URL is stored within a paragraph
	listofteams = livescores.find_all('p')

	i = []

	for teams in listofteams:
	#As the url we need is stored in the line after the title,
	#if the title is correct then set a flag high and jump into this if statement
	#This if statement looks at the next line and extracts the URl from the iframe
		if i == 'true':
			frodframe = teams
			frodurl = frodframe.find('iframe').get('src')
			#set flag low so that URL isnt overwritten
			i = []

		#Does this line contain the correct team
		#if yes set flag high
		team = teams.text
		if 'APPLEBY' not in team:
			continue
		else:
			i = 'true'

	#frodurl is a url to the widget page
	#open a soup object to the widget page
	widgetsauce = urllib.urlopen(frodurl)
	widget = bs.BeautifulSoup(widgetsauce, 'lxml')

	#Our id is stored within a table
	tables = widget.find_all('table')

	# tables[0] is a table containing the id we need our data is stored in
	# one line of the table
	cells = tables[0].find_all('tr')
	cells = cells[9].find_all('td')
	cells = cells[0].find_all('table')
	cells = cells[0].find_all('tr')
	cell = cells[1].find_all('td')
	longID = cell[1].find('a').get('href')
	ID = longID.split('=')
	scorecardURL = 'https://www.totalcricketscorer.com/TCSLive/TCSScorecard.aspx?id='+ ID[1]
	#print(scorecardURL)
	#for each cell find the one containing the URL
	return scorecardURL

def getScoreInfo(URL):
    scorecardURL = urllib.urlopen(URL).read()
    scorecard = bs.BeautifulSoup(scorecardURL,'lxml')
    tables = scorecard.find_all('table')
    row = tables[3].find_all('tr')
    row = row[3].find_all('tr')
    cell = row[2].find('td')
    table = cell.find('span')
    return table

def getRows(scoreInfo):
	rows = scoreInfo.find_all('tr')
	return rows

def writeLine(resultSet):
    string = ''
    for result in resultSet:
        string = string + str(result.text) + ','
    string += '\n'
    with open('data.csv','wb') as csvfile:
        csvfile.write(string)