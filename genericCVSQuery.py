import json
import time
from datetime import datetime
import requests

targetState="XX"                      # 2-letter state code, i.e. "NY"/"TX"/etc
targetCities=["XXXX","XXXX","XXXX"]   # city names

def updateLog(logTime, cityName):
  logFile = targetState + "-vac.log"
  fileOut=open(logFile,'a')
  fileOut.write(str(logTime) + ' ' + cityName + '\n')
  fileOut.close()
  return

def sendNotifications(cityName):
  
  # put code to send email/text/etc notifications here

  return

def checkCVS(state):
  print("Checking CVS website...")
  genInfo=requests.get("https://www.cvs.com/immunizations/covid-19-vaccine")
  cookies=genInfo.headers["Set-Cookie"]
  stateURL="https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status." + state + ".json?vaccineinfo"
  vaccineRequest = requests.get(stateURL, headers={
    "cookie": cookies,
    "authority": "www.cvs.com",
    "accept": "*/*",
    "sec-fetch-site": "same-origin",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "referer": "https://www.cvs.com/immunizations/covid-19-vaccine",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
  })
  return vaccineRequest.json()["responsePayloadData"]["data"][state]

def main():
  timeLogged={}
  timeNotified={}
  secondsPerMinute=60
  secondsPerHour=60*60

  needAppointment=True
  while needAppointment:
    cityData=checkCVS(targetState)

    printListOfCities=False  # set True to get a list of all tracked cities in the state
    if printListOfCities:
      for city in cityData:
        print(city["city"])

    for city in cityData:
      if city["status"]=="Available":
        name=city["city"]
        availTime=datetime.now()
        print("Vaccines available in " + name)

        # log all cities in state with available appointments, targeted or not
        if not name in timeLogged.keys():                  
          timeLogged[name]=availTime.timestamp()
          updateLog(availTime, name)
        elif availTime.timestamp() > timeLogged[name] + (secondsPerMinute * 10):  # update only if > 10 min has passed
          timeLogged[name]=availTime.timestamp()
          updateLog(availTime, name)

        # send notifications for targeted cities with available appointments
        if name in targetCities:
          print("Vaccines available in targeted city " + name + "!")
          if not name in timeNotified.keys():                  
            timeNotified[name]=availTime.timestamp()
            sendNotifications(name)
            # needAppointment=False   # use this to exit after 1 notification
          elif availTime.timestamp() > timeNotified[name] + (secondsPerHour * 1):   # update only if > 1 hour has passed
            timeNotified[name]=availTime.timestamp()
            sendNotifications(name)

    # needAppointment=False   # use this to exit after 1 check
    if needAppointment:
      print("Waiting 1 min...")
      time.sleep(secondsPerMinute * 1)

  return

if __name__ == "__main__":
  main()
