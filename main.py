import upload
import os
import GRABBER
import FileManagement
import sys

if len(sys.argv) > 1:   
    term = ""
    for x in range((len(sys.argv))-1):
        term = term + " " + sys.arg8v[x+1]
    term = term.strip()
else:
    term = "Cute Animal"

#Day Grabber
day = GRABBER.dayCount()


print("BOBLYBOT DAY " + str(day))



GRABBER.images(day, term)
upload.send(day, term)
FileManagement.deletefiles(term)
GRABBER.newDay(day)




