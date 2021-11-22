from django.conf import settings
from django.core.mail import send_mail


def email_generated_code(code, email):
    send_mail("Account Verification Code",
              "Verification Code: {}".format(code),
              settings.EMAIL_HOST_USER,
              [email],
              fail_silently=False)

