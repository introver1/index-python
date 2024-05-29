import random
import string
CharValues = string.digits + string.ascii_letters + string.punctuation
password_len = 14
password = ""
# print(CharValues)
# print(random.choice(CharValues))
for loop in range(password_len):
    password += random.choice(CharValues)
print("Password is ", password)    