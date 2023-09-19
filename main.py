import os
import smtplib
import json
#
from dotenv import load_dotenv
#
load_dotenv()
#_________________________________________________________________


with open("emails.json", "r") as my_file:
    file_contents = my_file.read()
emails_to = json.loads(file_contents)
#_________________________________________________________________

mail = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
#_________________________________________________________________

heading =f"""\
From:{mail}
To: {emails_to}
Subject: Реклама
Content-Type: text/plain; charset="UTF-8";

"""
#__________________________________________________________________
#Work with headers/Работа с заголовками

with open("text_mail.txt", "r" , encoding="UTF-8") as my_file:
  text = my_file.read()

#________________________________________________________________________________________________________=
email_to = input ("Кому:")
text = text.replace("%friend_name%" , email_to )
email_from = input ("От кого:")
text = text.replace("%my_name%", email_from)
website = "polus101.ru"
text = text.replace("%website%", website)
#_________________________________________________________________________________________________=
letter = heading + text
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(mail, password)
server.sendmail(mail, emails_to, letter)
server.quit()

