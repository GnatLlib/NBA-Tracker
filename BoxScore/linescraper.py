import requests
import datetime
from .game import Game


def getgames():
    date = datetime.datetime.now()
    # if it is before 6pm, use yesterday's date
    if date.hour < 18:
        date = datetime.datetime.now() - datetime.timedelta(1)

    # format url to grab data from
    url = "http://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate={}%2F{}%2F{}".format(date.month,
                                                                                                         date.day,
                                                                                                         date.year)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/54.0.2840.71 Safari/537.36', 'Referer': 'http://stats.nba.com/scores/'}

    raw = requests.get(url, headers=headers).json()

    linescores = raw['resultSets'][1]['rowSet']
    games = []

    # process data in sets of two since two teams to each game
    for i in range(0, len(linescores), 2):
        g = Game()
        g.id = linescores[i][2]
        g.t1_overview = {"team": linescores[i][4], "q1": linescores[i][7],
                         "q2": linescores[i][8], "q3": linescores[i][9], "q4": linescores[i][10],
                         "total": linescores[i][21] }
        g.t2_overview = {"team": linescores[i+1][4], "q1": linescores[i+1][7],
                         "q2": linescores[i+1][8], "q3": linescores[i+1][9], "q4": linescores[i+1][10],
                         "total": linescores[i+1][21]}
        games.append(g)

    return games

