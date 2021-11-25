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
              "Username: {} \n Investor Number: {}\n Control Number:{}  Thank you.".format(user.username, up.investor_num,
                                                                                           up.control_num),
              settings.EMAIL_HOST_USER,
              [user.email],
              fail_silently=False)