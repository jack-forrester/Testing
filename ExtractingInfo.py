import LiveScoresAPI
import csv

URL = LiveScoresAPI.FindURL()
scoreInfo = LiveScoresAPI.getScoreInfo(URL)
rows = LiveScoresAPI.getRows(scoreInfo)

#Import titles
teams = rows[5].find_all('td')
LiveScoresAPI.writeLine(teams)

#get totals
totals = rows[6].find_all('td')
score = []
for total in totals:
    runs = total.text.split(' for')
    print(runs[0])
