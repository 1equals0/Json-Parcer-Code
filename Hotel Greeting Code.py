#### This program will assume that the stff member knows the id of the company and the guests
import json
from pprint import pprint
import sys
from datetime import datetime
import time

##Parse company.json and identify company of interest

businessID = dict()

with open('Companies.json') as json_data:
    companies = json.load(json_data)
    json_data.close()
    for organiz in companies:
        companyID = organiz['id']
        company = organiz['company']
        city = organiz['city']
        timeZone = organiz['timezone']
        businessID[companyID] = company,city,timeZone

compMax = len(companies)
compID = input("Please enter the company ID: ")
if compID.isdigit() == False or int(compID) > compMax:
    while compID.isdigit() == False:    ## Both booleans and floats aren't accepted
        compID = input("Please enter the company ID as an integer: ")
    while int(compID) > compMax:
        compID = input("That company ID doesn't exist, please enter another: ")
compID = int(compID)

## coi = (company of interest)
coiCompany = businessID[compID][0]
coiCity = businessID[compID][1]
coiTimezone = businessID[compID][2]


## Parse Guest.json and identify guest of interest

personID = dict()
with open('Guests.json') as jsonData:
    guestData = json.load(jsonData)
    jsonData.close()
for guests in guestData:
    firstName = guests['firstName']
    lastName = guests['lastName']
    guestID = guests['id'] 
    reservation = guests['reservation']
    roomNum = guests['reservation']['roomNumber']
    Tstart = guests['reservation']['startTimestamp']
    Tend = guests['reservation']['endTimestamp']
    personID[guestID] = firstName,lastName,roomNum,Tstart,Tend
    
guestMax = len(guestData)
inputID = input("Please enter the guest id: ")
if inputID.isdigit() == False or int(inputID) > guestMax:
    while inputID.isdigit() == False:    ## Both booleans and floats aren't accepted
        inputID = input("Please enter the guest ID as an integer: ")
    while int(inputID) > guestMax:
        inputID = input("That guest ID doesn't exist, please enter another: ")
inputID = int(inputID)

## poi = (person of interest)
poiFirstname = personID[inputID][0]
poiLastname = personID[inputID][1]
poiRoom = personID[inputID][2]
poiTstart = datetime.fromtimestamp(personID[inputID][3])
poiTend = datetime.fromtimestamp(personID[inputID][4])


## Message Template

response = input("Do you want to use the standard message template(Y/N)? ")
if response != "Y" and response != "N":
    while response != "Y" or response != "N":
        response = input("Standard message template(Y/N)? ")
        if response == "Y" or response == "N":
            break
if response == "Y":
    templateID = dict()
    with open('Message2.json') as json_Data:
        messageData = json.load(json_Data)
    for message in messageData:
        messageID = message['id']
        greeting = message['greeting']
        intro = message['intro']
        room = message['room']
        end = message['end']
        templateID[messageID] = greeting,intro,room,end

    templateMax = len(messageData)
    inputID = input("Please enter the message ID: ")
    if inputID.isdigit() == False or int(inputID) > templateMax:
        while inputID.isdigit() == False:    ## Both booleans and floats aren't accepted
            inputID = input("Please enter the message ID as an integer: ")
        while int(inputID) > templateMax:
            inputID = input("That message ID doesn't exist, please enter another: ")
    inputID = int(inputID)

    ## toi = (template of interest)
    toiGreeting = templateID[inputID][0]
    toiIntro = templateID[inputID][1]
    toiRoom = templateID[inputID][2]
    toiEnd = templateID[inputID][3]
    
    current = time.strftime("%H:%M:%S")
    hour = int(current[0:2])
    if hour > 19 or hour < 6:
        timeGreeting = "night,"
    elif hour < 17 and hour < 19:
        timeGreeting = "evening,"
    elif hour > 12 and hour < 15:
        timeGreeting = "afternoon,"
    elif hour > 6 and hour < 12:
        timeGreeting = "morning,"
    else:
        timeGreeting = "day,"
    print("\n")
    print(toiGreeting, timeGreeting, toiIntro,coiCompany + ",", poiFirstname,poiLastname + "!",toiRoom,poiRoom,toiEnd)
else:
    print("\n")
    print("All relevant guest data is displayed, type in your custom message.")
    print("\n")
    print("Name:", poiFirstname,poiLastname, " Room:", poiRoom, "  Arrival:", poiTstart,"  Departure:", poiTend)
    print("Company:", coiCompany, " City:", coiCity, "  Timezone", coiTimezone)
    print("\n")
    finalMessage = input()
    print(finalMessage)


