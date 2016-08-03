from __future__ import print_function

from twisted.mail.smtp import sendmail
from twisted.internet.task import react

from email.mime.text import MIMEText

def main(reactor):
    bot_owner = "alice@gmail.com"
    to = ["victim@addr.net"]

    message = MIMEText("Attachments incoming...!")
    message["Subject"] = "Stolen Files"
    message["From"] = bot_owner
    message["To"] = ", ".join(to)

    d = sendmail("smtp.gmail.com", bot_owner, to, message,
                 port=587, username=me, password="*********",
                 requireAuthentication=True,
                 requireTransportSecurity=True)

    d.addBoth(print)
    return d

react(main)
