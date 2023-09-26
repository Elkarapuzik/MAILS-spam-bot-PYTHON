import smtplib

def send_mail(text, mail, password, emails_to):
  heading =f"""\
From:{mail}
To: {emails_to}
Subject: Реклама
Content-Type: text/plain; charset="UTF-8";

  """
  letter = heading + text
  letter = letter.encode("UTF-8")
  server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
  server.login(mail, password)
  server.sendmail(mail, emails_to, letter)
  server.quit()