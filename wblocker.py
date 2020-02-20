import time
from datetime import datetime as dt

#definitions
hosts_file = r"C:\Windows\System32\drivers\etc\hosts"
ip_example = "127.0.0.1"
sites_list = ["www.facebook.com", "facebook.com", "youtube.com", "youtube.rs", \
"www.youtube.com", "www.9gag.com", "www.reddit.com", "9gag.com", "reddit.com"]

n = 0
while True:
    n = n + 1
    if dt(dt.now().year, dt.now().month, dt.now().day, 12) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 21):
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
    if n < 5: print("Re-checking hosts...")
    time.sleep(2.5)

