import string as s
from random import SystemRandom as sr

secret_key = ''.join(sr().choices(s.ascii_letters + s.punctuation, k=64))

print(secret_key)