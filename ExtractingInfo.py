import LiveScoresAPI

URL = LiveScoresAPI.FindURL()
scoreInfo = LiveScoresAPI.getScoreInfo(URL)
rows = LiveScoresAPI.getRows(scoreInfo)
writer = LiveScoresAPI.openCSVWr('data.csv')

#Import titles
teams = rows[5].find_all('td')
LiveScoresAPI.writeLine(teams, writer)

#get totals
totals = rows[6].find_all('td')
score = LiveScoresAPI.getScore(totals)
LiveScoresAPI.writeLine(score, writer)
