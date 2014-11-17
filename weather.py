import os
import pickle
import json
import urllib
import forecastio
import re
import datetime
from pprint import pprint

#vars
api_key = os.environ.get('FORECASTIO_API_KEY')
stl_lat = 38.624656
stl_lng = -90.187433

#API call to get forecast
#stl_forecast = forecastio.load_forecast(api_key, stl_lat, stl_lng)

#store objects
# current = stl_forecast.currently()
# minutely = stl_forecast.minutely().data
# hourly = stl_forecast.hourly().data
# daily = stl_forecast.daily().data


#pickle objects
# stlfile = open("stl.txt", "w")
# pickle.dump(stl_forecast, stlfile)
# stlfile.close

# currentfile = open("current.txt", "w")
# pickle.dump(current, currentfile)
# currentfile.close()
#
# minutelyfile = open("minutely.txt", "w")
# pickle.dump(minutely, minutelyfile)
# minutelyfile.close()
#
# hourlyfile = open("hourly.txt", "w")
# pickle.dump(hourly, hourlyfile)
# hourlyfile.close()
#
# dailyfile = open("daily.txt", "w")
# pickle.dump(daily, dailyfile)
# dailyfile.close()


stlfile = open("stl.txt", "r")
stl_forecast = pickle.load(stlfile)
stlfile.close()

daily = stl_forecast.daily().data

def slight():
    print str(day.time) + ": Slight chance of" + str(day.precipType)

def some():
    print str(day.time) + ": Some chance of" + str(day.precipType)

def likely():
    print str(day.time) + ": Likely chance of" + str(day.precipType)

def certain():
    print str(day.time) + ": Certain chance of" + str(day.precipType)

chance = {1:slight,
    2:slight,
    3:slight,
    4:some,
    5:some,
    6:some,
    7:likely,
    8:likely,
    9:likely,
    10:certain,
}

for day in daily:
    p = round(day.precipProbability,1) * 10
    if hasattr(day, "precipType") and p > 0:
            chance[p]()
            print
    else:
        print str(day.time) + ": No precipitation today."
        
    # if hasattr(day, "precipProbability"):
    #     print day.time
    #     print "Chance: " + str(day.precipProbability)
    #     if hasattr(day, "precipAccumulation"):
    #         print "Amount: " + str(day.precipAccumulation)
    #     if hasattr(day, "precipIntensityMax"):
    #         print "Intensity: " + str(day.precipIntensityMax)
    #     if hasattr(day, "precipIntensityMaxTime"):
    #         print "Intensity max time: " + str(datetime.datetime.fromtimestamp(
    #     int(day.precipIntensityMaxTime)
    # ).strftime('%Y-%m-%d %H:%M:%S'))