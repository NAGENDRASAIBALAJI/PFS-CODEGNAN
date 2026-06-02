''''
SMPT-simple mail transfer protocol
----------------------------------
-->this is used to send emails from server to servers to another...
NOTE:
-----
1.SMTP SSL port
---------------
465

2.SMTP TLS port
---------------
587

import smtlib

emailmessage class
------------------
msg['subject'] = 'SMTP on mail'
msg['from'] = 'sender@mail.com'
msg['to'] = 'receiver@mail.com'


----------------------------------------------------
import smtplib
from email.message import EmailMessage
sender = 'nagendrasaibalaji@gmail.com'
password = 'xhicrxxbbpqqiras'
msg = EmailMessage()

msg['Subject'] = 'welcome mail'
msg['From'] = sender
msg['To'] = 'swapnareddy.sonu@gmail.com'

msg.set_content('BAD GIRL')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()

---------------------------------------------------
import smtplib
from email.message import EmailMessage
sender = 'nagendrasaibalaji@gmail.com'
password = 'ksconjwntwppcish'
receiver_ = ['mudadlaharsha@gmail.com' ,'
             +@gmail.com']
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
for email in receiver_:
    msg = EmailMessage()

    msg['Subject'] = 'Welcome Mail'
    msg['From'] = sender
    msg['To'] = email
    msg.set_content('TOPPER OF UNIVERS')

    server.send_message(msg)
server.quit()






    




































