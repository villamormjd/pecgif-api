import random, string


def generate_string():
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    print(x.upper())
    return x.upper()

def mask_email(email):
    email = email.split('@')
    mask_email = len(email[0][:-4]) * "*" + email[0][-4:]
    email[0] = mask_email
    email = '@'.join(email)

    return email

def generate_code():
    return random.randint(111111,999999)
