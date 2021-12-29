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


body = "Good day, Investors!\n" \
       "This is to announce that our P/E Capital Investment Green Innovation Fund Application is now live." \
       "You are going to recieved an email with your account details to activate your account.\n\nThank you,\n" \
       "P/E Capital Investment Green Innovation Fund"



def send_email_multi(user, up):
    img_src1 = "<img src='https://lh3.googleusercontent.com/VqWWkZn54RGQvZgbbvgcfXLY36cBB0tneAd1v3aTT01QOgtKVQMpo7cTZblY8Lvgg5wN02Ldv0nozR_uBQCrgY2XmR9GcaWY7KQYlhIljReCYW3Ux7xjjLaBQI1kRzNmjUi40mwHwjA2VAbzQb1eiX8GD30k04UunnqrybyQaFMFDCuQJJCtAH6osDFY5cYraHvkWstcES4LI_unCm_eGe0lB4eqxmxr28Xfidd8VkLh7Y-vRD8kZCFEkKNqETIdvGYT_qDsaUXoio0M_0qQOXSVcz2HU6Brq_Cw32ale4H5gecHD7uSAxxNIMQj86DLIqF56pHQ0cpiLSmQEeTKs8qa1zfvGfyQu0eTuSmsOVetYNETPTHzf0VurBkwpuhAPNtB-0gkqdfpZ5WYVzmY_qfzIcWKVT4s-oPwVjUef7PBo5ZJN5NMyA981qpbzsm_uKJaU12sV8zK0hpGEmPdWK55GoUOxD5-oKk8ekqm5E8BTYxO6vORhBGDBGS6M56MyKyaFOi8xyYzjyTHZAuKWi8UROeGnlTa0kzD2AEqxH1AQZLD8gV6T0jrxwBlTP9VU4DtM-UyjvwrmnLH27RNR4eP8t2NCKOnMIQL2simgFBe35QIeWJWFOr1ng-O5FI5TixLKI_qxCq4N3z3OVcqp1IWrIsAZWIggMqRTKq32YhisFvdjUeJWNaM106SKUmFAoKccpAhMl6VBdGucRZhKdLx=w535-h943-no?authuser=0'>"

    img_src2 = "<img src='https://lh3.googleusercontent.com/SBw4cPMVx7Wsa0-yfbJPSIKGkAdZRYkSCXuyTKWBV35gIzlbIqTdKi9wNsjbgF0z7wt_RUBP9jge1wWmoIq0LbdnrWRLGxTMu0S6cWLhYR6fYXGFKFtnI0wNY_4w9UBV0I0c-fKwyq_vGkEwLoO-vARCddbCNdqUZr_sz5V0LfgOC2eMnGxlRoUET1F_TCIWnm7eb4ePGUrNDsGZRymfHh2X0sawy57a8tGDLynuygzvhJ1gJgWR0y8PMO-jm-f2vTpBObw3O-7hhws5xPdMDwu2lL768WnvFbgA99X30lv4TSPuAuPaf0aBIqEqoZODvNbhk7KzaHqrCMZcIbwREyItaYyvHEtGXpMn_nrGISogpBP-ZxjLj5PVynB0YH9SYbnmHeIZVzMlj1ulx1MKx4s1Niy58oZvIoITjO6Y9EjFpRwUVR3lfm0UorgYDUyZMke4T9IF2Yo6xLU9Gbl5QVSTMS7SPgwzqi0WJ5SCLbUwgi8EnbAG6KSza-OvBsMh8DiKEdvASEnASboBGUAndVSeJjvyCoop1ncB0YogJCMrl9SSe4CXz8AraGZeJOa4fJsQ-PWGidy6c0rHRbRia1iKhcPOnTYDpmmcX6QUqFvVtZAFnwUdSD_QCz_7hEStRmPE4mrkBeUgbU_e06rv4x3cqOd1V2I4I4yRheAvckM4H4aaLQd3xni18NoO44kQjmytj3odxMiQUAJnuoy4WMh6=w538-h943-no?authuser=0'>"

    img_src3 = "<img src='https://lh3.googleusercontent.com/T3qCcCaXVQ1r7xVx6korE-jFvAUcx5IV3VNYz1ci3zhOy4CcdbAkt2SsZknc-UvIYcxolLTsD5YAjedPHY74yh1IH2rpkTc9tinCHBIjgqnPHckIgBzrOc9F5G6upHA0ib6jO3vm9YrH9CqfgG2f04bX3Q0iSLpDoSAr1tg-s5jEkS8G9VpwcocV1oao710xqVTs3NyY-Nfzhmbuf6AuqQAO4OawUjB7w_6y5aFiv14oKBd4IIXzOx1m8nkRNczPSrjx_aMweESM9C2fn6F0Eq0zkEZ7j5dbHORdHs4G2KRXn81xi-tqvIVBg0pLPbv4TNCQQNAIGMHDN-UN6JdI1RqFI9Um3tePSJQyIkHl59VfceoYUYEgfh66-VWJOxo_NtChbW7-hOmkuwrjxVZbuB_0KMz_tXqW9tIhVnlGUQutkIezlLxoQI8eNM4K6nQu66I6bb2V09u3Z2LMzazjRzp5PMBrCi0OOBonAkarzrNtArUKQ_3hVOMFjAVbDUeP1U6hOgxS2Ypv8NUW5bvOtXnbVMoT5WsLfV24RK6IpQOXwGqFDHEuCVurnJ1GX5Zu50qnV42PQBfK9iywtHJOt83A0KjJzA_P-_sbc2_Z3U1V7uaHttK67bnW1zeeNrPx_qeDJDzUbo4JjLNIZ3wYkCrO2cp-WnR_iOZW48WL7yZ_qnocxcloRxzvNB1a-CDShVX0T2W4lt7go0HaIFkqCQmB=w543-h943-no?authuser=0'>"
    subject, from_email, to = 'P/E Capital Green Innovation Fund Account Activation Details', settings.EMAIL_HOST_USER, user.email
    text_content = 'P/E Capital Green Innovation Fund Account Activation Details'
    html_content = f'<p>Good Day, <strong>{user.first_name} {user.last_name}</strong>!</p><br/>' \
                   f'<p>To activate your account, kindly use your <strong> INVESTOR NUMBER </strong> below. </p>' \
                   f'<strong> INVESTOR NUMBER </strong>: <strong style="color: red;"> {up.investor_num} </strong>' \
                   f'<p>Here are the instructions on how to access your account. </p><br/>' \
                   f'<ol> ' \
                   f'<li> Go to Investor Portal (<a href="https://pecgif-web.herokuapp.com/"> https://pecgif-web.herokuapp.com/ </a>)</li>' \
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
    html_content = f'<p>Dear  <strong>Friends and Investors</strong>, </p><br/>' \
                   f'<p>We wish you a happy and healthy holiday season! </p><br/>' \
                   f'<p>We are excited to announce that the P/E Capital Investment Green Innovation Fund app is now live. In the last few months, we have been tirelessly working to improve our service and we believe this will help you enjoy your experience even more. </p><br/>' \
                   f'<p>For security purposes, you will receive a separate email with instructions on how to access your account via the mobile app.</p><br/>' \
                   f'<p>If you have questions, please do not hesitate to contact us at clientcare@pecapital.org</p><br/>' \
                   f'<p>Sincerely, </p>' \
                   f'<p><strong> P/E Capital Green Innovation Fund </strong></p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to], bcc=bcc_emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print("SENT!")