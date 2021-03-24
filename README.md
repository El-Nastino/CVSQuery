# CVSQuery
CVS COVID-19 Vaccine Appointment Availability Finder

Current as of Mar 2021

This script polls the CVS website for availability of COVID-19 vaccine appointments, filtered by state and city.

Set targetState to the two-character state code, e.g. 'NY', 'TX', etc., and set targetCities to a list of desired cities. To see the city names available for a state, run queryCVS() on that state and print the return value, which is a list of objects containing several fields, including 'name' (of city) and 'status' ('Available' or 'Fully booked').

As written, the script queries the CVS site every minute, and prints a message for any city in the targetState found to have available appointments; it also appends the time and city name to a simple text file log (no more than once every 10 minutes) so you can review state-wide trends. The timing and criteria are pretty easy to change.

If any of the cities in the targetCities list have available appointments, it then calls sendNotifications() (no more than once an hour, also easy to change), which prints another message, and is where you can add code to send email/text/etc. notifications as desired. For instructions on how to do that, search "how to send email with Python", "how to send text messages with Python", and/or "how to send text messages with email".

dependency: Python package: 'request'
