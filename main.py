from dotenv import load_dotenv
import os
import smtplib
import json
load_dotenv()
#_________________________________________________________________


with open("emails.json", "r") as my_file:
    file_contents = my_file.read()
emails_to = json.loads(file_contents)
#_________________________________________________________________

pochta = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
#_________________________________________________________________

neletter =f"""\
From:{pochta}
To: {emails_to}
Subject: Реклама
Content-Type: text/plain; charset="UTF-8";

"""
print(neletter)
#__________________________________________________________________
#Work with headers/Работа с заголовками

with open("txt.txt", "r" , encoding="UTF-8") as my_file:
  text = my_file.read()

#________________________________________________________________________________________________________=
email_to = input ("Кому:")
text = text.replace("%friend_name%" , email_to )
email_from = input ("От каго:")
text = text.replace("%my_name%", email_from)
website = "polus101.ru"
text = text.replace("%website%", website)
print(text)
#_________________________________________________________________________________________________=
letter= neletter + text
letter = letter.encode("UTF-8")
print(letter)
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(pochta, password)
server.sendmail(pochta, emails_to, letter)

def my_function(sending):

  server.quit()

