import hashlib

from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import PBKDF2PasswordHasher

class PasswordHasher(PBKDF2PasswordHasher):
    algorithm = "pbkdf2_sha256"
    iterations = 320000
    digest = hashlib.sha256

    def encode(self, password):
        salt = get_random_string(13)
        return super().encode(password, salt, 320000)