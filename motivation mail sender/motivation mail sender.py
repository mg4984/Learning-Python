import smtplib
import datetime as dt
import random

email = "ydma0019@gmail.com"
password = "xohxeq-kagbot-jEbka6"

dt.datetime.now()
weekday= now.weekday() 
if weekday== 3:
    with open("/Users/mohit/Desktop/PYTHON !/motivation mail sender/quotes.txt") as quote_file:
        all_quotes= quote_file.readlines()
        quote= random.choice(all_quotes)
        
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email , password)
        connection.sendmail(
            from_addr= email  ,
            
            to_addrs= "mohit.gupta.5102002@gmail.com",
            msg=f"subject: Monday motivation\n\n{quote}" )