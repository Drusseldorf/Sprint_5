import random
import string


class RandomCreds:

    @staticmethod
    def email():
        local_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(9))
        subdomain = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        email = local_name + '@' + subdomain + '.com'
        return email

    @staticmethod
    def password():
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(10))
        return password
