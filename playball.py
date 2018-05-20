from __future__ import print_function
from yeelight import *
import mlbgame
import time
import datetime


def goal_light():
    for line in range(15):
        bulb = Bulb("192.168.2.93")
        bulb.set_brightness(100)
        bulb.set_rgb(0, 0, 255)
        bulb.turn_on(effect="smooth", duration=50)
        time.sleep(1)
        bulb.turn_off()
        time.sleep(1)


def logger(line,datestr):
    with open("playball.log", "a") as ballfile:
        ballfile.write("{0},{1}".format(datestr,line))


def play_ball():
    run_history = 0
    while True:
        now = datetime.datetime.now()
        current_year = now.year
        current_month = now.month
        current_day = now.day
        current_hour = now.hour
        current_minute = now.minute
        datestr = "{0}-{1}-{2}-{3}:{4}".format(current_year,current_month,current_day,current_hour,current_minute)
        day = mlbgame.day(current_year, current_month, current_day, away='Blue Jays', home='Blue Jays')
        game = day[0]
        if int(game.home_team_runs) > run_history:
            logger(datestr,game.home_team_runs)
            run_history = game.home_team_runs
            try:
               goal_light()
            except main.BulbException:
               time.sleep(5)
               goal_light()
        if int(current_hour) == 5:
            run_history = 0
        time.sleep(5)


if __name__ == "__main__":
    play_ball()



