import os
import json
import argparse
#_____________________________=
from dotenv import load_dotenv
#_____________________________=
from send_mail import send_mail
#_____________________________=
load_dotenv()
#_____________________________=
parser = argparse.ArgumentParser(
        description="This bot is spamming emails"
)
#parser - Сборщик флагов из терминала
parser.add_argument(
    '--emails',
    help='файл с почтами для рассылки только в расширении .json / file with for newsletter in .json extension only',
    default='emails.json'
)
#
parser.add_argument(
    '--text',
    help='тект для рассылки только в расширении .txt / text for newsletter in .txt extension only',
    default='text_mail.txt'
)
#
parser.add_argument(
    '--subject',
    help='Введите текст для темы письма-рассылки / Enter the text for the subject of the newsletter email',
    default='Реклама'
)
#
subject =  parser.parse_args().subject
#
text_file = parser.parse_args().text
#
emails_file = parser.parse_args().emails
#________________________________________________________________________________________________________=

try:
    with open(emails_file, "r") as my_file:
        file_contents = my_file.read()
    emails_to = json.loads(file_contents)
except FileNotFoundError:
    print(f'При запуске не был найден файл "{emails_file}"')
    exit()

#________________________________________________________________________________________________________=

mail = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

#Work with headers/Работа с заголовками
#________________________________________________________________________________________________________=

try:
    with open(text_file, "r" , encoding="UTF-8") as my_file:
        text = my_file.read()
except FileNotFoundError:
    print(f'При запуске не был найден файл "{text_file}"')
    exit()
#Обработка ошибок
#________________________________________________________________________________________________________=

email_to = input ("Кому:")
text = text.replace("%friend_name%" , email_to )
email_from = input ("От кого:")
text = text.replace("%my_name%", email_from)
website = "polus101.ru"
text = text.replace("%website%", website)

#Работа с текстом
#________________________________________________________________________________________________________=

send_mail(text, mail, password, emails_to, subject)

#________________________________________________________________________________________________________=