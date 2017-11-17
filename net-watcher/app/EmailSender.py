import smtplib
import logging


class EmailSender():

    def __init__(self,
                 user,
                 pwd,
                 server="smtp.gmail.com",
                 port=587):
        self.user = user
        self.pwd = pwd
        self.server = server
        self.port = int(port)

    def send_email(self,
                   recipient,
                   subject,
                   body):
        gmail_user = self.user
        gmail_pwd = self.pwd
        FROM = self.user
        TO = recipient if type(recipient) is list else [recipient]
        SUBJECT = subject
        TEXT = body

        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP(self.server,
                                  self.port)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            logging.info('successfully sent the mail')
        except:
            logging.info("failed to send mail")
