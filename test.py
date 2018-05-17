from __future__ import print_function
from yeelight import *
import mlbgame
import time


def goal_light():
    for line in range(15):
        bulb = Bulb("192.168.2.93")
        bulb.set_brightness(100)
        bulb.set_rgb(0, 0, 255)
        bulb.turn_on(effect="smooth", duration=50)
        time.sleep(1)
        bulb.turn_off()
        time.sleep(1)

run_history = 0

while True:
    day = mlbgame.day(2018, 5, 16, away='Astros', home='Astros')
    game = day[0]
    print(run_history)
    if int(game.away_team_runs) > run_history:
        print(game.away_team_runs)
        run_history = game.away_team_runs
        goal_light()

