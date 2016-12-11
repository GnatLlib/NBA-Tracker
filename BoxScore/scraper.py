import psycopg2 as p
import requests
import datetime

try:
    con = p.connect(database="nba", user="postgres", password="970118tawny")
except:
    print("Can't connect to database")


def getgames():
    date = datetime.datetime.now().date()
    # if it is before 6pm, use yesterday's date
    #if date.hour < 18:
       # date = datetime.datetime.now() - datetime.timedelta(1)

    # format url to grab data from



    url = "http://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate={}%2F{}%2F{}".format(date.month,
                                                                                                         date.day,
                                                                                                         date.year)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/54.0.2840.71 Safari/537.36', 'Referer': 'http://stats.nba.com/scores/'}

    raw = requests.get(url, headers=headers).json()

    linescores = raw['resultSets'][1]['rowSet']

    curr = con.cursor()

    for i in range(0, len(linescores), 2):

        game_id = linescores[i][2]
        t1 = linescores[i][4]
        t1q1 = linescores[i][7]
        t1q2 = linescores[i][8]
        t1q3 = linescores[i][9]
        t1q4 = linescores[i][10]
        t1final = linescores[i][21]
        t2 = linescores[i+1][4]
        t2q1 = linescores[i+1][7]
        t2q2 = linescores[i+1][8]
        t2q3 = linescores[i+1][9]
        t2q4 = linescores[i+1][10]
        t2final = linescores[i+1][21]



        data = (t1, t2, t1q1, t1q2, t1q3, t1q4, t2q1, t2q2, t2q3, t2q4, t1final, t2final, date, game_id)
        SQL = "insert into \"BoxScore_quarterscore\" values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        try:
            curr.execute(SQL,data)
        except:
            print("injection failed")

        con.commit()
    curr.close()
    con.close()


getgames()
