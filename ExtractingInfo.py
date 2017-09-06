import LiveScoresAPI
import csv

URL = LiveScoresAPI.FindURL()
scoreInfo = LiveScoresAPI.getScoreInfo(URL)
rows = LiveScoresAPI.getRows(scoreInfo)

    #Import titles
teams = rows[5].find_all('td')
LiveScoresAPI.writeLine(teams)
