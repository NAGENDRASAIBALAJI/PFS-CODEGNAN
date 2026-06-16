'''
DAY- 14

TOPIC:  DATE AND TIME
DATE AND TIME:
-------------
-->PYTHON PROVIDES THE BUILT-IN DATATIME MODULE TO WORK WITH DATES AND TIME,,.


IMPORT DATETIME:
----------------
import datetime
today = datetime.date.today()
now = datetime.datetime.now()
print(now)
print(today)

-------------------------------
import datetime
now = datetime.datetime.now()
print(f"Year is:{now.year}")
print(f"month is:{now.month}")
print(f"day is:{now.day}")
print(f"hour is:{now.day}")
print(f"minutes is:{now.minute}")
print(f"second is:{now.second}")


FORMATING DATE AND TIME:
------------------------
-->STRFTIME()IS USED TO FORMATE DATE AND TIME

%d-->day
%m-->month
%y-->year
%h-->hour
%m-->min
%s-->sec

----------------
import datetime
now = datetime.datetime.now()
print(now.strftime("%d-%m-%y"))
print(now.strftime("%H-%M-%S"))
-------------------------------------
import datetime
date1 = datetime.date(2026,6,1)
date2 = datetime.date(2026,6,15)
diff = date1 - date2
print(f"difference is: {diff}")
--------------------------------------
TIME DELTA
-----------
import datetime
today = datetime.date.today()
future_ = today + datetime.timedelta(days=7)
print(future_)

-----------------------------------
import calendar
import datetime

today = datetime.date.today()
year = today.year
month = today.month
print(calendar.month(year,month))


CTTIME:
-------
import calendar
year = 2025
print(calendar.calendar(2025))

import smtplib
from email.message import Emailmessage
import time
from datetime import datetime

sender_mail = "nagendrasaibalaji@gmail.com"
password_ = 'rtcgyvwdrirhwzsx'
receiver_mail = '@gmail.com'
target_time = '10:15'

while True:
    now = datetime.now().strftime("%H:%M")
    if now == "10:38":
        sender = "
'''  
from datetime import datetime
import time
import smtplib
from email.message import EmailMessage
while True:
    now = datetime.now().strftime("%H:%M")
    if now == "10:45":
        sender = "nagendrasaibalaji@gmail.com"
        password = "rtcgyvwdrirhwzsx"
        msg = EmailMessage()
        msg["Subject"] = "Test Mail"
        msg["From"] = sender
        msg["To"] = "swapnareddy.sonu@gmail.com"
        msg.set_content("Dear Sir/Madam,\n\n" "This is a test email to verify sucessful email delivery.\n\n""Thank you.")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        print("Email Sent")
        break
    time.sleep(30)

































