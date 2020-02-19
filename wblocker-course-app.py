import time
from datetime import datetime as dt

#definitions
hosts_file = r"C:\Windows\System32\drivers\etc\hosts"
ip_example = "127.0.0.1"
sites_list = ["www.facebook.com", "www.youtube.com", "www.9gag.com", "www.reddit.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("Within time...")
        with open(hosts_file, "r+") as file:
            content = file.read()
            for website in sites_list:
                if website in content:
                    pass
                else:
                    file.write(ip_example + " " + website + "\n")
    else:
        with open(hosts_file, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in sites_list):
                    file.write(line)
            file.truncate()
    time.sleep(2.5)