from django.conf import settings
from django.core.mail import send_mail


def email_generated_code(code, email):
    send_mail("Account Verification Code",
              "Verification Code: {}".format(code),
              settings.EMAIL_HOST_USER,
              [email],
              fail_silently=False)


def email_activation(user):
    send_mail("Account Activation",
              "Your accoutn has been activated.\n Username: {} \n\n Thank you.".format(user.username),
              settings.EMAIL_HOST_USER,
              [user.email],
              fail_silently=False)