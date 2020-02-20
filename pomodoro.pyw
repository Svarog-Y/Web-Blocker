import sys
import os
import multiprocessing
import time
from flask import Flask, render_template
from datetime import datetime as dt

def localhost():
    name = multiprocessing.current_process().name
    print(name, ' Starting')

    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template('index.html')

    if __name__ == '__mp_main__':
        app.run(use_reloader=False, debug=True, host="0.0.0.0", port=80)

def weblock():
    name = multiprocessing.current_process().name
    print(name, ' Starting')

    #definitions
    hosts_file = r"C:\Windows\System32\drivers\etc\hosts"
    ip_example = "127.0.0.1"
    sites_list = ["www.facebook.com", "facebook.com", "facebook.com/", "www.facebook.com/", "fb.com", "m.facebook.com", "www.youtube.com", "youtube.com", "www.youtube.com/", "m.youtube.com", "youtube.com/", "www.9gag.com", "9gag.com", "www.reddit.com", "reddit.com"]

    def today_hour(h):
        hours = int(h) 
        if 0 <= hours <= 24:
            return dt(dt.now().year, dt.now().month, dt.now().day, hours)
        elif hours < 0:
            return dt(dt.now().year, dt.now().month, dt.now().day, 0)
        else: return dt(dt.now().year, dt.now().month, dt.now().day, 24)

    def reset_hosts():
        with open(hosts_file, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in sites_list):
                    file.write(line)
            file.truncate()
        print('Hosts file successfully reset.')
    
    def block_sites():
        with open(hosts_file, "r+") as file:
            content = file.read()
            for website in sites_list:
                if website in content:
                    pass
                else:
                    file.write(ip_example + " " + website + "\n")

    os.system('ipconfig/flushdns')
    while True:
        try:
            if today_hour(8) < dt.now() < today_hour(20): block_sites()
            else: reset_hosts()
            
            time.sleep(10)
        
        except KeyboardInterrupt: 
            reset_hosts()
            print("Exiting program...")
            break

if __name__ == '__main__':
    lh_service = multiprocessing.Process(
        name = 'ServerHost',
        target = localhost,
    )

    wl_service = multiprocessing.Process(
        name = 'Weblocker',
        target = weblock,
    )

    lh_service.start()
    wl_service.start()