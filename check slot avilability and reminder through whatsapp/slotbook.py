

from datetime import datetime
import pywhatkit

import requests
print("----------------------WELCOME TO VACCINE TARACKER---------------------")
age=int (input("Enter the age you want to search vaccine for :- "))
ditri=int (input("Enter your district id :-    state_id:28,state_name:Punjab,state_id:29,state_name:Rajasthan"))
def create_session_info(center, session):
    return {"name": center["name"],
            "date": session["date"],
            "capacity": session["available_capacity"],
            "age_limit": session["min_age_limit"]}

def get_sessions(data):
    for center in data["centers"]:
        for session in center["sessions"]:
            yield create_session_info(center, session)

def is_available(session):
    return session["capacity"] > 0

def is_eighteen_plus(session):
    return session["age_limit"] == age

def get_for_seven_days(start_date):
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
    params = {"district_id":ditri, "date": start_date.strftime("%d-%m-%Y")}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    resp = requests.get(url, params=params, headers=headers)
    data = resp.json()
    return [session for session in get_sessions(data) if is_eighteen_plus(session) and is_available(session)]

def create_output(session_info):
    return f"{session_info['date']} - {session_info['name']} ({session_info['capacity']})"
mess=get_for_seven_days(datetime.today())
print(mess)
print(" Press 1.To send the data to any one through whatsApp")
x=int(input("Option :-  "))
if (x==1):
    print("ENTER THE TIME AT WHICH YOU WANT TO SEND THE MESSAGE :- ")
    mphone=input("\t Please enter your Contact number :- ")
    fphone=str("+91"+mphone)
    hour=int(input("Enter the Hour( in 24 format ):-  "))
    minu=int(input("Enter the minute :-  "))
    # pywhatkit.sendwhatmsg(receiver=fphone,mess,hour,minu,10,'true','chrome')
    pywhatkit.sendwhatmsg(fphone,str(mess),hour,minu)
    print(" MESSAGE SUCCESFULLY SENT ")
    # 9412229666