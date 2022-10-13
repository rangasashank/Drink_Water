import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "PLEASE DRINK WATER!",
            message = "You need to drink 3 litres of water everyday",
            app_icon = "/Users/sashi/Desktop/Projects/Iconsmind-Outline-Glass-Water.ico",
            timeout = 5)
        time.sleep(60*60)
