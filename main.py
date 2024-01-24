import os.path
import datetime as DT
import calendar 

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def whatDay(x):
    if(x == 0):
        return "Monday"
    elif(x==1):
        return "Tueday"
    elif(x==2):
        return "Wednesday"
    elif(x==3):
        return "Thurday"
    elif(x==4):
        return "Friday"
    elif(x == 5):
        return "Saturday"
    elif(x == 6):
        return "Sunday"


def main():
    #automatically sets the credential to none to have a variable that we can work with.
    creds = None

    #checks if the path token exists to prove that we do have credentials to work with
    if os.path.exists("token.json"):
        #If the credentials exist then we will assign them to the variable 
        creds = Credentials.from_authorized_user_file("token.json",SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json","w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        createEvent  = {
            "summary": "My Python Event",
            "location" : "The Battle Bus",
            "description" : "I LOVE FORTNITE",
            "colorId" : 1,
            "start": {
                "dateTime" : "2023-12-26T17:00:00-08:00",
                "timeZone": "America/Los_Angeles"
            },
            "end" : {
                "dateTime" : "2023-12-26T17:00:00-08:00",
                "timeZone": "America/Los_Angeles"
            },
            "recurrence": [
                "RRULE:FREQ=DAILY;COUNT=3"
            ],
            "attendances": [
                {"email":"example@example.com"}
            ]


        }
        day0Events = []
        day0Date = 0
        day1Events = []
        day1Date = 0 
        day2Events = []
        day2Date = 0 
        day3Events = []
        day3Date = 0 
        day4Events = []
        day4Date = 0 
        day5Events = []
        day5Date = 0 
        day6Events = []
        day6Date = 0 
        now = DT.datetime.now().isoformat() + "Z"

        event_result = service.events().list(calendarId="primary", timeMin=now, maxResults=80, singleEvents=True, orderBy ="startTime").execute()
        # createEventExecute = service.events().insert(calendarId = "primary", body = createEvent).execute()
        events = event_result.get("items",[])

        if not events:
            print("No upcoming events MAKE SOME PLANS!")
            return
        
        day1Date = str(events[0]["start"].get("dateTime", events[0]["start"].get("date")))
        day1Year = day1Date[0:4]
        day1Month = day1Date[5:7]
        day1Day = day1Date[8:10]
        print(day1Date)
        print(day1Year)
        print(day1Month)
        print(day1Day)
        print("this is me trying to find the first index")
        print("this is the date of " , day1Month, " - ",day1Day, "   : \n" )
        print("the day of the week is :" , whatDay(calendar.weekday(int(day1Year),int(day1Month), int(day1Day))))
        
        print(calendar.weekday(int(day1Year),int(day1Month), int(day1Day)))
        for event in events:
            #start = event["start"].get("dateTime", event["start"].get("date"))
            start = event["start"].get("dateTime", event["start"].get("date"))
            arrDate = event["start"].get("dateTime")[0:10]
            if(len(day0Events)==0):
                day0Date = arrDate
                day0Events.append(start + "   "+event["summary"])
            elif(day0Date == arrDate):
                day0Events.append(start + "   "+event["summary"])
            elif(len(day1Events)==0):
                day1Date = arrDate
                day1Events.append(start + "   " + event["summary"])
            elif(day1Date == arrDate):
                day1Events.append(start + "   " + event["summary"])
            elif(len(day2Events)==0):
                day2Date = arrDate
                day2Events.append(start+"   "+event["summary"])
            elif(day2Date == arrDate):
                day2Events.append(start+"   "+event["summary"])
            elif(len(day3Events)==0):
                day3Date = arrDate
                day3Events.append(start+"   " + event["summary"])
            elif(day3Date == arrDate):
                day3Events.append(start+"   " + event["summary"])
            elif(len(day4Events)==0):
                day4Date = arrDate
                day4Events.append(start+"   " + event["summary"])
            elif(day4Date == arrDate):
                day4Events.append(start+"   " + event["summary"])            
            elif(len(day5Events)==0):
                day5Date = arrDate
                day5Events.append(start+"   " + event["summary"])
            elif(day5Date == arrDate):
                day5Events.append(start+"   " + event["summary"])                
            elif(len(day6Events)==0):
                day6Date = arrDate
                day6Events.append(start+"   " + event["summary"])
            elif(day6Date == arrDate):
                day6Events.append(start+"   " + event["summary"])
            else:
                break
            print(arrDate, " This is the date",start, event["summary"])

        print("this is testing the first day function")
        print(day0Events)
        print("this is testing the second day")
        print(day1Events)
        print("this is me testing the third day")
        print(day2Events)
        print("this is me testing the fourth day")
        print(day3Events)
        print("this is me testing the fifth day")
        print(day4Events)
        print("this is my testing the sixth day")
        print(day5Events)
        print("this is me testing the seventh day")
        print(day6Events)
    except HttpError as error:
        print("An error has occured: ", error)




if __name__ =="__main__":
    main()


