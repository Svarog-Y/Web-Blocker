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
    sites_list = ["www.facebook.com*", "www.youtube.com*", "www.9gag.com", "www.reddit.com*"]

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

    n = 0
    os.system('ipconfig/flushdns')
    while True:
        n = n + 1
        try:
            if dt(dt.now().year, dt.now().month, dt.now().day, 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23): block_sites()
            else: reset_hosts()
            
            if n < 5: print("Re-checking hosts...")
            time.sleep(2.5)
        
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