import FindStuff
import CSV

URL = FindStuff.FindURL()
scoreInfo = FindStuff.getScoreInfo(URL)
rows = FindStuff.getRows(scoreInfo)

teams = rows[5].find_all('td')

for team in teams:
    print(team.text)

with open('csvfile.csv','wb') as file:
csvRows = CSV.reader(File)
