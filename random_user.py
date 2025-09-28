import random
import string


def generate_random_valid_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(['gmail.com', 'yahoo.com', 'test.com'])
    return f"{username}@{domain}"

def generate_invalid_unique_email(length=2):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_random_password(length=6):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password