from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import threading
import time


class EmailThread(threading.Thread):
    def __init__(self, subject, body, from_email, recipient_list, fail_silently, html):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.html = html
        threading.Thread.__init__(self)

    def run(self):
        print('Email content =-=-=-=-=-=')
        print(self.subject)
        print(self.recipient_list)

        msg = EmailMultiAlternatives(
            self.subject, self.body, self.from_email, self.recipient_list)
        if self.html:
            msg.attach_alternative(self.html, "text/html")
        print("now it's time to msg.send ----- ")
        try:
            msg.send(self.fail_silently)
        except Exception as e:
            print(f"Error sending email: {e}")


def send_mail(subject, recipient_list, body='', from_email='nearcafe@naver.com', fail_silently=False, html=None, *args, **kwargs):
    print("trying to send the mail with send_mail method...")
    print(" --- please checking all of infomations are matching --- ")
    print(subject)
    print(recipient_list)

    thread = EmailThread(subject, body, from_email,
                         recipient_list, fail_silently, html)
    thread.start()
    time.sleep(1)
