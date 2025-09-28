import random

class Random:
    @staticmethod
    def generate_random_valid_email():
        valid_email = f'Qwerty{random.randint(100,999)}@yandex.ru'
        return valid_email

    @staticmethod
    def valid_password():
        valid_password = f'Qwerty{random.randint(100,999)}'
        return valid_password

    def generate_random_invalid_email(length=8):
        invalid_email= f'Qwe{random.randint(100,999)}yandex.ru'
        return invalid_email
