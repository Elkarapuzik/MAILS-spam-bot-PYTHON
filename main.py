import os
import json
#_____________________________=
from dotenv import load_dotenv
#_____________________________=
from send_mail import send_mail
#_____________________________=
load_dotenv()
#________________________________________________________________________________________________________=

with open("emails.json", "r") as my_file:
    file_contents = my_file.read()
emails_to = json.loads(file_contents)

#________________________________________________________________________________________________________=

mail = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

#Work with headers/Работа с заголовками
#________________________________________________________________________________________________________=

with open("text_mail.txt", "r" , encoding="UTF-8") as my_file:
  text = my_file.read()

#________________________________________________________________________________________________________=

email_to = input ("Кому:")
text = text.replace("%friend_name%" , email_to )
email_from = input ("От кого:")
text = text.replace("%my_name%", email_from)
website = "polus101.ru"
text = text.replace("%website%", website)

#________________________________________________________________________________________________________=

send_mail(text, mail, password, emails_to)

#________________________________________________________________________________________________________=