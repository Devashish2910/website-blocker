import time
from datetime import datetime as dt

host_temp = "hosts"
host_path = '/private/etc/hosts'
redirect = "127.0.0.1"
block_list = ["www.facebook.com", "facebook.com"]

while True:
    # During working hours
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print("Working Hours..🧐")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in block_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    # After working hours
    else:
        print("Have fun!!🤪")
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in block_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)
