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
score = []
for total in totals:
    runs = total.text.split(' for')
    wickets = runs[1].split('(')
    overs = wickets[1].split('o')
    runs = runs[0].lstrip()
    wickets = wickets[0].lstrip()
    overs = overs[0].lstrip()
    score.append(runs)
    score.append(wickets)
    score.append(overs)
LiveScoresAPI.writeLine(score, writer)
