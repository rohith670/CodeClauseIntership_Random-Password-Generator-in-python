import random
import string

def generate_pas(length=12):
    char = string.ascii_letters + string.digits
    pas = ''.join(random.choice(char) for i in range(length))
    return pas
pas = generate_pas(12)
print("Try this Random password:", pas)