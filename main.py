import os.path
import datetime as DT
import calendar 
from tkinter import*
from tkinter import ttk

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]
def openNewWindow(day0,day1,day2,day3,day4,day5,day6):
    appWindow = Tk()
    appWindow.title("Application")
    val = True
    if val:
        appWindowLabel = Label(appWindow, text="Credentails recgonized going to next screen")
        appWindowLabel.pack()
        appWindow.destroy()
        calendarWindow = Tk()
        calendarWindow.title("This should be your calendar ")
        calendarWindow.configure(bg="#83a6eb")
        LabelStart =  Label(calendarWindow, text="Here are your tasks for the next 7 days")
        LabelStart.pack()
        table = ttk.Treeview(calendarWindow, columns=('first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh'), show='headings')
        table.heading('first', text=returnDates(day0))
        table.heading('second', text=returnDates(day1))
        table.heading('third', text=returnDates(day2))
        table.heading('fourth', text= returnDates(day3))
        table.heading('fifth', text= returnDates(day4))
        table.heading('sixth',text=returnDates(day5))
        table.heading('seventh', text=returnDates(day6))

        table.pack()
        



    else:
        appWindowLabel = Label(appWindow,text="Please give credentials to continue")
        appWindowLabel.pack()

    
def printDayEvents(x):
    date = x[0][0:10]
    dayYear = date[0:4]
    dayMonth = date[5:7]
    dayDay = date[8:10]
    day = whatDay(calendar.weekday(int(dayYear),int(dayMonth), int(dayDay)))
    month  = whatMonth(dayMonth)
    print(date)
    print(day,",",month,dayDay,",",dayYear)
    for y in x:
        print(y[11:len(y)])

def returnDates(x):
    date = x[0][0:10]
    dayYear = date[0:4]
    dayMonth = date[5:7]
    dayDay = date[8:10]
    day = whatDay(calendar.weekday(int(dayYear),int(dayMonth), int(dayDay)))
    month  = whatMonth(dayMonth)
    return day,",",month,dayDay,",",dayYear

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
    
def whatMonth(x):
    if(x == "01"):
        return "January"
    elif(x== "02"):
        return "Feburary"
    elif(x== "03"):
        return "March"
    elif(x== "04"):
        return "April"
    elif(x== "05"):
        return "May"
    elif(x== "06"):
        return "June"
    elif(x== "07"):
        return "July"
    elif(x== "08"):
        return "August"
    elif(x== "09"):
        return "September"
    elif(x== "10"):
        return "October"
    elif(x== "11"):
        return "November"
    elif(x== "12"):
        return "December"

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
        allEvents = [day0Events, day1Events, day2Events, day3Events,day4Events, day5Events, day6Events]
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
            end = event["end"].get("dateTime",event["end"].get("date"))
            arrDate = event["start"].get("dateTime")[0:10]
            if(len(day0Events)==0):
                day0Date = arrDate
                day0Events.append(start + "  --  "+end+"   "+event["summary"])
            elif(day0Date == arrDate):
                day0Events.append(start + "  --  "+end+ "   "+event["summary"])
            elif(len(day1Events)==0):
                day1Date = arrDate
                day1Events.append(start + "  --  "+end+ "   " + event["summary"])
            elif(day1Date == arrDate):
                day1Events.append(start + "  --  "+end+ "   " + event["summary"])
            elif(len(day2Events)==0):
                day2Date = arrDate
                day2Events.append(start+ "  --  "+end+"   "+event["summary"])
            elif(day2Date == arrDate):
                day2Events.append(start+ "  --  "+end+"   "+event["summary"])
            elif(len(day3Events)==0):
                day3Date = arrDate
                day3Events.append(start+ "  --  "+end+"   " + event["summary"])
            elif(day3Date == arrDate):
                day3Events.append(start+ "  --  "+end+"   " + event["summary"])
            elif(len(day4Events)==0):
                day4Date = arrDate
                day4Events.append(start+ "  --  "+end+"   " + event["summary"])
            elif(day4Date == arrDate):
                day4Events.append(start+ "  --  "+end+"   " + event["summary"])            
            elif(len(day5Events)==0):
                day5Date = arrDate
                day5Events.append(start+ "  --  "+end+"   " + event["summary"])
            elif(day5Date == arrDate):
                day5Events.append(start+ "  --  "+end+"   " + event["summary"])                
            elif(len(day6Events)==0):
                day6Date = arrDate
                day6Events.append(start+ "  --  "+end+"   " + event["summary"])
            elif(day6Date == arrDate):
                day6Events.append(start+ "  --  "+end+"   " + event["summary"])
            else:
                break
            print(arrDate, " This is the date",start,"- ",end, event["summary"])




        root = Tk()
        root.geometry("800x500")
        root.title("Calendar Automation App")
        root.configure(bg="#83a6eb")

        #creating the title label for this GUI
        myLabel = Label(root, text="Python Calendar Automation")
        myLabel.place(relx=0.5,rely=0.025,anchor=CENTER)
        myLabel.grid(row=0,column=0, padx=300, pady=50)

        myButtonStart = Button(root, text="Start Application",height=5,width=25,command=lambda: (openNewWindow(day0Events,day1Events,day2Events,day3Events,day4Events,day5Events,day6Events))).grid(row=1,column=0, pady=10)
        myButtonExit = Button(root, text="Exit Application",height=5,width=25).grid(row=2,column=0, pady=10)        
        root.mainloop()
        printDayEvents(day0Events)
        printDayEvents(day1Events)
        printDayEvents(day2Events)
        printDayEvents(day3Events)
        printDayEvents(day4Events)
        printDayEvents(day5Events)
        printDayEvents(day6Events)
    except HttpError as error:
        print("An error has occured: ", error)




if __name__ =="__main__":
    main()


