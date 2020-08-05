#   Assignment 3
#   CIS 231 / Cuesta College
#   Fall, 2019 / R. Scovil
#   Oliver Graham, olivergraham916@gmail.com
#   Due: October 31st, 2019

import json
import math


def getSummary(data):
    summaryList = []

    for day in data:
        aDay = dict()

        date = day['date']['weekday'] + "," + " " + day['date']['monthname'] + " " + \
               str(day['date']['day']) + " " + str(day['date']['year'])

        windSpd = str(day['avewind']['mph']) + "mph"

        windDir = day['avewind']['dir']

        humidity = str(day['avehumidity']) + "%"

        aDay['date'] = date
        aDay['conditions'] = day['conditions']
        aDay['highF'] = day['high']['fahrenheit']
        aDay['highC'] = day['high']['celsius']
        aDay['lowF'] = day['low']['fahrenheit']
        aDay['lowC'] = day['low']['celsius']
        aDay['windSpd'] = windSpd
        aDay['windDir'] = windDir
        aDay['humidity'] = humidity

        summaryList.append(aDay)

    return summaryList


def formatLR(lWord, rWord):
    rightSide = 60 - len(lWord) + len(rWord)  # 60 is longer than longest left string
    print(lWord, "{:>{rightSide}}".format(rWord, rightSide=rightSide))


def printHeader(word):
    print("\n", "".rjust(32, "-") + word.ljust(58, "-"), "\n")


def printDailyForecast(sumList):
    for day in sumList:
        printHeader(day['date'])

        formatLR("Conditions:", day['conditions'])

        formatLR("Highest temperature:", day['highF'] + " Fahrenheit " +
                 "(" + day['highC'] + " Celsius)")

        formatLR("Lowest temperature:", day['lowF'] + " Fahrenheit " +
                 "(" + "{:>2}".format(day['lowC']) + " Celsius)")

        formatLR("Average wind speed and direction:", str("{:>5}".format(day['windSpd'])) +
                 ", " + day['windDir'])

        formatLR("Average humidity:", day['humidity'])


def printHighLow(sumList):
    highF = -math.inf
    lowF = math.inf

    for day in sumList:
        if highF < int(day.get('highF')):
            highF = int(day.get('highF'))
            highC = day.get('highC')
            highDay = day.get('date')

        if lowF > int(day.get('lowF')):
            lowF = int(day.get('lowF'))
            lowC = day.get('lowC')
            lowDay = day.get('date')

    formatLR("Highest temperature occurs on " + highDay + ":", str(highF) + " Fahrenheit " +
             "(" + highC + " Celsius)")

    formatLR("Lowest temperature occurs on " + lowDay + ":", str(lowF) + " Fahrenheit " +
             "(" + "{:>2}".format(lowC) + " Celsius)\n")


def printHighLowAverage(sumList):
    highSum = 0
    lowSum = 0

    for day in sumList:
        highSum += int(day.get('highF'))
        lowSum += int(day.get('lowF'))

    formatLR("Average of high temperatures over forecast period:",
             str(highSum / len(sumList)) + " Fahrenheit")

    formatLR("Average of low temperatures over forecast period:",
             str(lowSum / len(sumList)) + " Fahrenheit\n")


def printConditions(sumList):
    conditions = dict()

    for day in sumList:
        conditions[day['conditions']] = conditions.get(day['conditions'], 0) + 1

    for key in conditions.keys():
        formatLR("The condition " + '"' + key + '"' + " appeared this many times:",
                 "{:>2}".format(str(conditions[key])))


def printReport():
    jsonFile = open('WU-SLO-forecast-10day.json', 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    summaryList = getSummary(data['forecast']['simpleforecast']['forecastday'])

    print("\n", "{:>75}".format("Oliver Graham - Assignment 3 - SLO 10-day Forecast Summary for"))
    print("{:>43}".format(summaryList[0]['date']), "--", summaryList[-1]['date'])

    printDailyForecast(summaryList)

    printHeader("------Summary")

    printHighLow(summaryList)

    printHighLowAverage(summaryList)

    printConditions(summaryList)


printReport()
