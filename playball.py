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


def play_ball():
    run_history = 0
    while True:
        now = datetime.datetime.now()
        current_year = now.year
        current_month = now.month
        current_day = now.day
        current_hour = now.hour
        day = mlbgame.day(current_year, current_month, current_day, away='Blue Jays', home='Blue Jays')
        game = day[0]
        print(run_history)
        if int(game.away_team_runs) > run_history:
            print(game.away_team_runs)
            run_history = game.away_team_runs
            goal_light()
        if int(current_hour) == 5:
            run_history = 0
        time.sleep(5)


if __name__ == "__main__":
    play_ball()



