import random
import string

def GeneratePassword():
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    #the folowing line is from https://pynative.com/python-generate-random-string/
    password += string.ascii_letters + string.digits + string.punctuation

    size = random.randint(6, 12)
    return ''.join(random.choice(password) for i in range(size))
print("The password is : ",GeneratePassword())


