from django.conf import settings
from django.core.mail import send_mail


def email_generated_code(code, email):
    send_mail("Account Verification Code",
              "Verification Code: {}".format(code),
              settings.EMAIL_HOST_USER,
              [email],
              fail_silently=False)


def email_activation(user, up):
    send_mail("Account Activation Success",
              "Your account has been activated. \n\n "
              "Username: {} \n Investor Number: {}\n Control Number: {}\n\n  Thank you.".format(user.username, up.investor_num,
                                                                                           up.control_num),
              settings.EMAIL_HOST_USER,
              [user.email],
              fail_silently=False)


def send_email_notifications(users, subject, body):
    emails = [u.email for u in users]
    send_mail(subject, body, settings.EMAIL_HOST_USER, emails, fail_silently=False)


def send_prelaunch_email(user, up):
    send_mail("P/E Capital Investments Account Activation Details",
              "Good day!\nYou may activate your account using information above.\n\n"
              "Username: {}\nInvestor Number: {}\n\n"
              "Thank you,\n P/E Capital Investment Green Innovation Fund.".format(user.username, up.investor_num),
              settings.EMAIL_HOST_USER,
              [user.email],
              fail_silently=False)


from django.contrib.auth.models import User
from api.models import *
from utils.services import *

subject = "P/E Capital Investment Green Innovation Fund App Launching"
body = "Good day, Investors!\n" \
       "This is to announce that our P/E Capital Investment Green Innovation Fund Application is now live." \
       "You are going to recieved an email with your account details to activate your account.\n\nThank you,\n" \
       "P/E Capital Investment Green Innovation Fund"