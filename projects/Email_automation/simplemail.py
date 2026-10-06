'''
email automation using python-->first we need to turn on 2 step verification and then we need to create app password for our email account

smtplib-->simple mail transfer protocol
import smtplib
#first we need to connect to the  gmail server
server=smtplib.SMTP('smtp.gmail.com',587)
print(server)
#starting the connection
server.starttls()
server.login('sanjusanjay35945@gmail.com','wfjg pdwi fakx cuzh')
#give your desired message to send
message='chaduvu ko hoka'
server.sendmail('sanjusanjay35945@gmail.com','vegijaykumar@gmail.com',message)
server.quit()
print("email sent successfully")


#now we will add subject and proper to address to the mail using email

import email
import smtplib
import random

#MIME--> multipurpose mail extension
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
otp=random.randint(1000,9999)
msg=MIMEMultipart()
#print(msg)
#now add from ,to subject
From ="sanjusanjay35945@gmail.com"
To="vegijaykumar@gmail.com"
Subject="Email Automation project using python"
msg['From']=From
msg['To']=To
msg['Subject']=Subject
body=f"The otp is {otp}"
msg.attach(MIMEText(body))
#finally we will convert above as string
text =msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
#starting the connection
server.starttls()
server.login('sanjusanjay35945@gmail.com','wfjg pdwi fakx cuzh')
#give your desired message to send

server.sendmail(From,To,text)
server.quit()
print("email sent successfully")
input_otp=int(input("enter the otp sent to your mail"))
if input_otp==otp:
    print("otp verified successfully")
else:
    print("otp verification failed")
    '''
import email
import smtplib
#MIME--> multipurpose mail extension
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText
#now to add attchment
from email.mime.base import MIMEBase#to addup our attachment

