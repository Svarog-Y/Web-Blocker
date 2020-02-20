import ctypes
import sys
import os
import multiprocessing
import time
from datetime import datetime as dt
from win10toast import ToastNotifier

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

os.system('ipconfig/flushdns') #flush DNS

#definitions
hosts_file = r"C:\Windows\System32\drivers\etc\hosts"
ip_example = "127.0.0.1"
sites_list = ["www.facebook.com", "facebook.com", "facebook.com/", "www.facebook.com/", "fb.com", "m.facebook.com", "www.youtube.com", "youtube.com", "www.youtube.com/", "m.youtube.com", "youtube.com/", "www.9gag.com", "9gag.com", "www.reddit.com", "reddit.com"]

def hour(h):
    hours = int(h) 
    if 0 <= hours <= 24:
        return dt(dt.now().year, dt.now().month, dt.now().day, hours)
    elif hours < 0:
        return dt(dt.now().year, dt.now().month, dt.now().day, 0)
    else: return dt(dt.now().year, dt.now().month, dt.now().day, 24)

def work_time():
    if hour(0) < dt.now() < hour(20): 
        return True
    else:
        return False 

def notify(body):
    toaster = ToastNotifier()
    toaster.show_toast("Hosts file changed", body, duration=10, threaded=True)

def reset_hosts():
    with open(hosts_file, "r+") as file:
        content_old = file.readlines()
        
        file.seek(0)
        for line in content_old:
            if not any(website in line for website in sites_list):
                file.write(line)
        file.truncate()
        
        file.seek(0)
        content_new = file.readlines()
        
        if not content_new == content_old:
            notify("Fun sites unlocked. Fun time!")

def block_sites():
    with open(hosts_file, "r+") as file:
        content_old = file.read()
        
        for website in sites_list:
            if website in content_old:
                pass
            else:
                file.write(ip_example + " " + website + "\n")
        
        file.seek(0)
        content_new = file.read()
        
        if not content_new == content_old:
            notify("Fun sites are locked. Grind time!")

while True:
    if work_time(): 
        block_sites()
    else: 
        reset_hosts()
    time.sleep(60)