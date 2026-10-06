import email
import smtplib 
from email import encoders
#MIME--> multipurpose mail extension
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText
#now add attchment
from email.mime.base import MIMEBase
import os    

attach="simplemail.py"
msg=MIMEMultipart()

#now add from ,to subject
From ="sanjusanjay35945@gmail.com"
To="vegijaykumar@gmail.com"
Subject="Email Automation project using python"
msg['From']=From
msg['To']=To
msg['Subject']=Subject
body="The file is attached"
#we will be using mimebase and encoders to attach the file
msg.attach(MIMEText(body))
part=MIMEBase('application','octet-stream')
part.set_payload(open(attach,'rb').read())
#now we will use encoders to encode the file
encoders.encode_base64(part)
#now to add header the file
part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
msg.attach(part)
text=msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(From,'wfjg pdwi fakx cuzh')
server.sendmail(From,To,text)
server.quit()   
print("email sent successfully")
