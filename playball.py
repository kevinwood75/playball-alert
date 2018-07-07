from __future__ import print_function
from yeelight import *
import mlbgame
import time
import datetime


def goal_light(green,red,blue,count):
    for line in range(count):
        bulb = Bulb("192.168.2.93")
        bulb.set_brightness(100)
        bulb.turn_on()
        bulb.set_rgb(green, red, blue)
        time.sleep(3)
        bulb.turn_off()
        time.sleep(1)

def logger(line,datestr):
    with open("playball.log", "a") as ballfile:
        ballfile.write("{0},{1}\n".format(datestr,line))


def check_winning(hruns,aruns,datestr):
    if int(aruns) < int(hruns):
       goal_light(255,0,0,3)
    else:
       goal_light(0,255,0,3)

    line = "{0},{1}".format(hruns,aruns)
    logger(line,datestr)



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
        if len(day) > 0:
           game = day[0]
           if 'Blue Jays' in game.away_team:
               if int(game.away_team_runs) > run_history:
                  logger(datestr,game.away_team_runs)
                  run_history = game.away_team_runs
                  try:
                     goal_light(0,0,255,5)
                  except main.BulbException:
                     time.sleep(5)
                     goal_light(0,0,255,5)
                  check_winning(game.home_team_runs,game.away_team_runs,datestr) 
           else:
               if int(game.home_team_runs) > run_history:
                  logger(datestr,game.home_team_runs)
                  run_history = game.home_team_runs
                  try:
                     goal_light(0,0,255,5)
                  except main.BulbException:
                     time.sleep(5)
                     goal_light(0,0,255,5)
                  check_winning(game.away_team_runs,game.home_team_runs,datestr)

           if int(current_hour) == 10:
               print("hello")
               run_history = 0
               logger(datestr,"reset")
               print("{0},{1}\n".format("reset",run_history))
           time.sleep(1)


if __name__ == "__main__":
    play_ball()
