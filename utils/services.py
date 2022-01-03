from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
import time
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
    img_src1 = "<img src='https://lh3.googleusercontent.com/VDmCKxwWW0N-ainbbqKFQKN8hcP7kYswwiDzXYP2O5g6V4swI2XVo-uvyZat-bBuZSl1lUCbaCm2zUxOJ3NC1KLkruVuW1boDdy9-wkn8ciAHZN5ac2xDEcTW3AEVrGho9c1oAthCUQdil6w8Ktuargt4kQhyUioz3v3wpp72Sx_WDaIaMhUrLuiFGHivYclGJXs-wrQbjE9iV-SlipSI07K9EVuUpAz53qh4DtqSLx6cEi7j16igCjr5awnUJaxH5ZbHIO0jmftv9KLac33L-DBW4NItS2gjqGnMwZIUX6NMxaRvriR4sGuz59Wb1jLG5B1ElDm8pbsBoQAnnXpjD1q9aoL5JTgOmJxcvJ4ePM4q9YBVrgla06GGdo8HYR3I9fnMrSXND-2A8aJcrc26gmeyHZ6Uk5SzcA8XxKxi2PM9mAFPYHargkartUrQl4Bolx3kKPekaSvHeXfhb7unDA1MhEogyKvol7gfh3HjQwiyc6j-r_A5jQhEX71I5g9Ifoa_YZjxmqNdOwsqSNMCD2AbCflkF7S0E0mi6Wt5sqp7Id58a0wWyqn6kixhNBoJ1CP4uI2QwP68Wm76FiTWb2NNe-EKzz76_LMywxgv_kPBLpRTAfGy_fiD207howGfof8G7gpLPXJZJP92Iy5JZW_mRNyQdTu2L6-J43Q-RBG0QIIloiHU4gbxNHgUmq4wmyu-ippGzOZnRfkJq72S2Lt=w535-h943-no?authuser=0'>"

    img_src2 = "<img src='https://lh3.googleusercontent.com/wPGiR9u6jrbyB91mrlyJPbjpTAXuA3g5vgy22CIn-LtOxjTe3_-qSU3tDYHzYG0TekTZB-zMjDqX40YdnAWqRcN1MbvSmycM-ocy0eWDeJp3PX41AWmZQzQ8BKmE-ukT06AYSdLJflJffm7RiJuu_t9zSaK43jiL04QnNOmIAvoNUd-qPYgWoGLMLpfWBQJ_lmA4VoIGDFVMevfZoMysTR827m1NWk4tztN-LTrKL-6ahuIV9lHnFGmD0bx12yAn91OZrxzgUOCUpvrz6f7w5agFWl5VVuzEx9XkaNZ3Z82RZo5SCO_pjrfYSoyfW4ATkwJ5XbL40RxqM-W6LuKBENAHYzzhp-uLVAhGbn1lYC8WC7ihx6tJTFDmFzNFluBoDLpAl5zbrFdG23WmgqtxfH30cyK1fmbqq5whm8Ds1JA7H36j5CZAaTSCWLfK7eRAalpW6jU9a4lAWtp5RrwaJfSHrWpsZKDIqO4Ai2tQaiaZbdj09_DzBKZe1cbpaOqBBcqUPUjKmRUo1KbRC7etmgdSb2fglRw4zK7XNYnUkewBluM4OC5ECeJNz7GVDbhi-HsbQxsJJDyICAp54oeJNWvM1CWh9sqWZpUqtb4r7teQCyCcFAT3nJIoxJEcwmf0i0AOFxsTGvsrAvDGLtVMaOowdExPhIk0kfwfk3xrWDvzRV9PwYTKPxS3QW_JuAX0byvpD3kmoC64UdDpcSoNlAOt=w538-h943-no?authuser=0'>"

    img_src3 = "<img src='https://lh3.googleusercontent.com/gCui5kl2J4bpBnSTiIYi2VhsBIbblyboTZHkEzzWhOlktQaq3t3dNB6uP5CoC3FhT3Theqdr5PDZog2j5NsKEe7sq2uX5yTXqrsP2h_DAZHifvRU1aNn_jmBSnW2kAgL0r9_HKvh54WNW4bY_NHoxgda7T8G2Zi5C5RV_NJcbNp_SpMllj6DzNfZaEw78RVP33CeQsfY-JIkAIvf9Ji6siTJ_eJRePISZ1JAvIWuCjuRty9d8rh5uSuzh-z-Mg1DiRi_2uedfFJrauNhCbnloTDU90RMdJKZLNAjYvbhEzzlpqqHnEkKO8pgejoWOoIRBEKd5-g1go40pEOsWq-aanbmBmkGKVpmhJutUweiJUKvfkEr-FuI0ZGzRB1AOja4-aR-XOKcvPcz06A2che1fQmeiUYaB0UUvCbGw5ul8zLT-IIQuzefkrQmwLYp7-GkUb0Sg8kbVr88G24xLkRn-l7B6vwmMlcJpqELo_oPOVfPDFVIzMKHrizFrGSglQ6q5-sPxgc1zIm1KwCizLjrTFbDxsS0esrgc1ZAa75zf67_aJzOQq71oF4o0K_KWwS8ZK2EXgKErv4yyjLNk1S8qxYibxUexMYNM0UTF47lZ0GPwkxY4HRh2gUEpwtdQbbjRxiM18BwysFJerGFpEzQh332ED5xmSXS0bABiD9HtRv1oB6YvBdumYr5AUuAvt4doByGlA2rL6x7yuYKu6GaDqXI=w543-h943-no?authuser=0'>"
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
    print("SENT!", user.email)
    time.sleep(3)


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