import requests
from datetime import datetime
import smtplib
import time

my_email = "ydma0019@gmail.com"
my_pass = "xohxeq-kagbot-jEbka6"


my_lat= 11.867351
my_long= 79.662181

def is_iss_overhead():

    response= requests.get(url = "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json() 
    
    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])
    
    if my_lat-5 <= iss_lat <= my_lat+5 and my_long-5 <= iss_long <= my_long+5:
        return True 
        
def is_night():
    
    parameters = {
        "lat": my_lat,
        "lng": my_long,
        "formatted": 0,
        
        
    }
    
    response = requests.get("https://api.sunrise-sunset.org/json" , params=parameters) 
    response.raise_for_status() 
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    print(sunrise)
    print(sunset)

    time_now = datetime.now()
    print(time_now.hour)
 
    if time_now >= sunset or time_now<= sunrise:
        return True 
 
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email , my_pass) 
        connection.sendmail(
            from_addr= my_email,
            to_addrs= my_email,
            msg= "Subject: Look Up\n\nThe ISS is above you"
        )
        
    