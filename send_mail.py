import smtplib

def send_mail(text, mail, password, emails_to):
  server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
  server.login(mail, password)
  for email in emails_to:
    heading =f"""\
From:{mail}
To: {email}
Subject: Реклама
Content-Type: text/plain; charset="UTF-8";

    """
    letter = heading + text
    letter = letter.encode("UTF-8")
    server.sendmail(mail, email, letter)
  server.quit()