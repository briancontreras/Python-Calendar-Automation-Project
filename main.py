import os.path
import datetime as DT

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]

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

        now = DT.datetime.now().isoformat() + "Z"

        event_result = service.events().list(calendarId="primary", timeMin=now, maxResults=10, singleEvents=True, orderBy ="startTime").execute()
        # createEventExecute = service.events().insert(calendarId = "primary", body = createEvent).execute()
        events = event_result.get("items",[])

        if not events:
            print("No upcoming events MAKE SOME PLANS!")
            return
        
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])

    except HttpError as error:
        print("An error has occured: ", error)




if __name__ =="__main__":
    main()


