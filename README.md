# CVSQuery
## CVS COVID-19 Vaccine Appointment Availability Finder
Current as of Mar 2021

### TL;DR:
Go on the CVS Vaccine website (https://www.cvs.com/immunizations/covid-19-vaccine) around 6:05AM eastern time, pick your state, and start clicking "Schedule Appointment" every 30 seconds or so.

### Dependency:
Python package: 'request'

### Description:
This script polls the CVS website for availability of COVID-19 vaccine appointments, filtered by state and city.

Set targetState (line 6) to the two-character state code, e.g. 'NY', 'TX', etc, and set targetCities (line 7) to a list of desired cities. To see the city names available for a state, set printListOfCities to True (line 49). Not all states/cities are covered; you can check the CVS website map/list to see which ones are.

As written, the script queries the CVS site every minute (can change on line 82), and prints a message for any city in the targetState found to have available appointments; it also appends the time and city name to a simple text file log (no more than once every 10 minutes) so you can review state-wide trends. The timing can be changed (line 64).

If any of the cities in the targetCities list have available appointments, it prints another message and calls sendNotifications() (no more than once an hour, can be changed on line 75), which is where you can add code to send email/text/etc notifications as desired (line 18). For notification instructions search "how to send email with Python", "how to send text messages with Python", and/or "how to send text messages with email".

Spoiler: As far as I can tell from running this on various states for about a week (late March 2021), CVS adds appointments to their central scheduling site every night around 4AM eastern time. However, the website says something along the lines of "We're updating, check back later" for approximately the next two hours, even though the appointments are listed as theoretically "available".  If you set this program up to send you notifications, you're likely to start getting those notifications in the middle of the night, about two hours before you can actually book an appointment. On the other hand, if you get a notification any other time for a city that is usually not available, you can probably book that appointment right away. 
