from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

def email_generated_code(code, email):
    send_mail("Account Verification Code",
              "Your Account Verification Code: {}".format(code),
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

    subject, from_email, to = 'Account Activation Success', settings.EMAIL_HOST_USER, user.email
    text_content = 'Account Activation Success'
    html_content = f'<p>Good Day, <strong>{user.first_name} {user.last_name}</strong>!</p><br/>' \
                   f'<p>Your account has been activated. You may now login using your username and password.</p>' \
                   f'<p>Here are you account details.</p><br/>' \
                   f'<p> <strong> Username </strong>: {user.username}  </p>' \
                   f'<p> <strong> Investor Number </strong>: {up.investor_num} </p>' \
                   f'<p> <strong> Control Number </strong>: {up.control_num} </p><br/>' \
                   f'If you have questions, please do not hesitate to contact us at clientcare@pecapital.org</p><br/>' \
                   f'<p>Sincerely, </p>' \
                   f'<p><strong> P/E Capital Green Innovation Fund </strong></p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print("SENT!")


def send_email_notifications(users, subject, body):
    emails = [u.email for u in users]
    send_mail(subject, body, settings.EMAIL_HOST_USER, emails, fail_silently=False)


def send_prelaunch_email(user, up):
    send_mail("P/E Capital Investments Account Activation Details",
              "Good day!\nYou may activate your account using information above, in this link: https://pecgif-web.herokuapp.com/\n\n"
              "Username: {}\nInvestor Number: {}\n\n"
              "Thank you,\n P/E Capital Investment Green Innovation Fund.".format(user.username, up.investor_num),
              settings.EMAIL_HOST_USER,
              [user.email],
              fail_silently=False)




def send_email_multi(user, up):
    img_src1 = "<img src='https://lh3.googleusercontent.com/EvLHeQnRS-2CBg7ppuAZtLN4pjGHoqc-1WDqlQyZ_Slh_pCLRlUw8SD03JdDLYNxXYTw2o3Z1SVJoklnN2eUyQVVawsuPYRjMmgt7Dd3u9sRoP9Eky0WiflHCemLDDW2RlQgK8BhwnfJnIFfYAwENjaEuHcirGoyYyYiXd9NXnaIhx5-3L39azC5zlzwbNWeRkCJtNJpdmq53Z1lWp98BWLOYWxD4TFdSWPjsGMPc3XrNSf6pfbvRKpfJUaTNJlky2506-bBF-o2c768CYY3PMk5Ql41OMCyQ4YnnQwM_k0fLdUVsP9Bxg3pOviM8WmzOmiWW5C5APlJ-lt85qAYpLbXiBFDyLAzlZ_93pUnf_gA085OeesoZ5WC2lC857BluP8XIZoNqwaMAIMIAZzrSJQg3OrRgq9L7BbIWrXEjFJ9jsYoJy2ltXhIxRtYUTg9BfUBZNbKCUec06gr_jVrKLfhrwEkOxZMseYRpariG8LzhlKoG-TQ0FNNfFsO6kQCXZj7B5rKOM1n14rg1SVQQBul1VQeK4V2kKrPCzj7SE5qVXfR0LiG8Dd7uf90764XC4V086xR5siXjtH-LFDgWJ-_gkYhcGUw4-wTJyZ8Fe9ElrCMAc3_yQWsM_ckhUqMeugqdG1kr5AVekV6FyWjZY3n62-TJrzQ88uOIEvAt0w2qzTO-5u-uDfe9-tQHYfHdE1ABelRfiEjcgFthLuOgiY2=w535-h943-no?authuser=0'>"

    img_src2 = "<img src='https://lh3.googleusercontent.com/v-QCf3IyQRq5-Odsh9tL8areJYft8186BW-WRbkD1MLQ-UcNTx-7QBtS7m04oIIs4oUzZLRqkLhY8Y8FBe5Ayn2bCthqjFQOfIY7MBtMzvEZU-wP0nEu9B0mIiSUu220uqkeqdTre0N8eHdgKXstqUTgQdaIOZd_1XuxyTxAAMShO-Pagx6rLgpVWCOfhEXqdMXbBoHP2wKm18TZI6qDpStNswycxHnokhS9MxNzKtf4J4UVHguJgl-nNBv7q2LHtJz9mUTcnEuqEo_2XOPCmoZfuCbzMtDVFBGSYAgavBDF5cCNm2l1tkjmm6YRQogdq5fBv2Sle7genxPVNrT93lrFgF7zTxB1CwscYGRnBo0ftncL9oLwjWhg1Y8Gs_BeeZClfZssJosSa5QcHuuXy681FrXXvaxusu79HoQM1SMtJ7Fwv4lojckNxHRskKUC4myVOIqA_QvSaY-EgcgmVgixMeDUDzl0OyirQNzBxznkJQBxpOVa6CbU1wyidwYxYPin9zc0BJMVC7sVxI8v5Aqgbfn1ioJLiwMQQ09TXasoSEQ0Hx07W5TaKyjY8wccrJ6aGORYc5qcxKbN1PoV89C_f6VBYAIUBuTwfbCyK2c33IvMIyvMFYD1uIwyhAqcksWVxU9wfju1nwY5n7djguCjomkwQCUq1mOlfDpsKyJ4D7a1AZ5N9FBusAybBwbrIxda1YkJaumsXGUQIynSkCGa=w538-h943-no?authuser=0'>"

    img_src3 = "<img src='https://lh3.googleusercontent.com/QUl25VeMCtO8cQYPBrUT3nWGN5cRMWVfkJcrjKTAz2L2t9UzZA4ACeAoDfoTNHS2MlVmTFr-Z5fqVo4emZ7Dr8DmMphVZSfrnmLkYtmQiVwHUxNPWRyI-K7IvZXdnHpnKMqd-ucQ3XLSPkGkxiuwWtXcdnf5SdCM5vQ50CCP3y5vtM3X5XcaXUAS-9N6wt2U0DGcR0Tc_xn4sw27xNdDauFokiH7Hhu32JfSQBDkGSzkTdJw-1Kmh4JeCVxZNHjwB56MC3A_3SvolM4k9e0MwRgNEqWGIEphRPMyTVRgcQ-OXLxJBUVn7Lp1qv8-EHKoReqloz52ESchb7bQMM2991fnWOCz4lBzJZrSnzJnXMAMejT5cj-x-18XS9l71Nupteoefu0SkDKDOeViMkVMl5oCV0BpsVAY1uNKYTkUihQdl5oy2eAYf_dQ0dsbqBSz5U3A-0MtEixA0oeb2AnvsPjltbQX2zXExWK7ZIN6QHP5XptsRD2XEUDyalNtNNfFGVfC8iGa4TpoYt2uLLDT3eBl4BXX-7Qly0_UQGriDyiS2gqKy40csyCkniRDFrWZ8K37CjvyzRnpFwZLHoN7WGdQCZv3z9sgxefYqPfn2G1TJOFMD7TIpkR228YJUJC2BcihZ4dgZ2Ru2t9hmNl-0jUdIjmAUA8DGx30LsN1P0kRtQhAVWKknAvGTsJORuCdGvailuWxo6lUJe639nRXbwtU=w543-h943-no?authuser=0'>"
    subject, from_email, to = 'P/E Capital Green Innovation Fund Account Activation Details', settings.EMAIL_HOST_USER, user.email
    text_content = 'P/E Capital Green Innovation Fund Account Activation Details'
    html_content = f'<p>Good Day, <strong>{user.first_name} {user.last_name}</strong>!</p>' \
                   f'<p>To activate your account, kindly use your <strong> INVESTOR NUMBER </strong> below. </p>' \
                   f'<strong> INVESTOR NUMBER </strong>: <strong style="color: red;"> {up.investor_num} </strong>' \
                   f'<p>Here are the instructions on how to access your account. </p><br/>' \
                   f'<ol> ' \
                   f'<li> Go to Investor Portal (<a href="http://www.pecgif.org/"> http://www.pecgif.org/ </a>)</li>' \
                   f'<li> Click Activate account <strong style="color: red;"> HERE </strong><br/>. {img_src1}</li>' \
                   f'<li> Provide your  <strong> INVESTOR NUMBER </strong> and desire <strong> PASSWORD </strong><br/>. {img_src2}</li>' \
                   f'<li> Check you registered email, a <strong> VERIFICATION CODE </strong> will be sent from clientcare@pecapital.org.</li>' \
                   f'<li> Provide the verification code and click <strong style="color: red;"> VERIFY </strong><br/> {img_src3}</li>' \
                   f'<li> You may now login your account with <strong> USERNAME </strong> and <strong> PASSWORD </strong>. </li>' \
                   f'</ol><br/>' \
                   f'<p> If you need further assistance, please do not hesitate to email us at clientcare@pecapital.org. Thank you and stay safe! </p><br/><br/><br/>' \
                   f'<p>Sincerely, </p>' \
                   f'<p><strong> P/E Capital Green Innovation Fund </strong></p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print("SENT!")


def pre_launch_email_multi(bcc_emails):
    subject, from_email, to = 'P/E Capital Green Innovation Fund App Launching', settings.EMAIL_HOST_USER, "info@pecapital.org"
    text_content = 'P/E Capital Green Innovation Fund App Launching'
    html_content = f'<p>Dear  <strong>Friends and Investors</strong>, </p>' \
                   f'<p>We wish you a happy and healthy holiday season! </p>' \
                   f'<p>We are excited to announce that the P/E Capital Investment Green Innovation Fund app is now live. In the last few months, we have been tirelessly working to improve our service and we believe this will help you enjoy your experience even more. </p>' \
                   f'<p>For security purposes, you will receive a separate email with instructions on how to access your account via the mobile app.</p>' \
                   f'<p>If you have questions, please do not hesitate to contact us at clientcare@pecapital.org</p><br/>' \
                   f'<p>Sincerely, </p>' \
                   f'<p><strong> P/E Capital Green Innovation Fund </strong></p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to], bcc=bcc_emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print("SENT!")