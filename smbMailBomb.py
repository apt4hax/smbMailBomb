import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse
from colorama import Fore, Back, Style
ascii_art = """\
━━━━━━━━┏┓━━┏━┓┏━┓━━━━━━━┏┓━┏━━┓━━━━━━━━━┏┓━━
━━━━━━━━┃┃━━┃┃┗┛┃┃━━━━━━━┃┃━┃┏┓┃━━━━━━━━━┃┃━━
┏━━┓┏┓┏┓┃┗━┓┃┏┓┏┓┃┏━━┓━┏┓┃┃━┃┗┛┗┓┏━━┓┏┓┏┓┃┗━┓
┃━━┫┃┗┛┃┃┏┓┃┃┃┃┃┃┃┗━┓┃━┣┫┃┃━┃┏━┓┃┃┏┓┃┃┗┛┃┃┏┓┃
┣━━┃┃┃┃┃┃┗┛┃┃┃┃┃┃┃┃┗┛┗┓┃┃┃┗┓┃┗━┛┃┃┗┛┃┃┃┃┃┃┗┛┃
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
             ¯\_(ツ)_/¯
             """
print(Fore.RED + ascii_art)
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse
from colorama import Fore, Back, Style
parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, default='email_list.xlsx')
parser.add_argument('-e', type=str, default='from@gmail.com')
parser.add_argument('-p', type=str, default='password')
parser.add_argument('-ip', type=str, default='127.0.0.1')
args = parser.parse_args()
df = pd.read_excel(args.f)
ip = args.ip 
for i in range(len(df)):
    name = df.iloc[i]['Name']
    email = df.iloc[i]['Email']
    msg = MIMEMultipart()
    msg['From'] = args.e
    msg['To'] = email
    msg['Subject'] = 'Hi, ' + name
    message = f"""Hello {name}

<html>
  <head></head>
  <body>
    <p>Just wanted to quickly say thank you for all your help last week<br>
         <img src="file://{ip}/image/alt.jpg"><br></br> 
         Mike<br>
        </p>
      </body>
    </html>
"""
    msg.attach(MIMEText(message, 'html'))
    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(args.e, args.p)
    try:
        mailserver.sendmail(args.f,email,msg.as_string())
        print(Fore.GREEN + 'Success: ' + email)
    except:
        print(Fore.RED + 'Error: ' + email)
        parser.print_help()
    mailserver.quit()
