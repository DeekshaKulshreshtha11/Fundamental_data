import time
import datetime
import winsound
from plyer import notification

if __name__ == '__main__':
    # Here you have to fetch date from database
    date = datetime.date(2022, 4, 2)
    days = datetime.timedelta(days=7)
    new_date = date - days
    while True:
        if new_date == datetime.date.today():
            frequancy = 2500
            duration = 1000
            winsound.Beep(frequancy, duration)
            notification.notify(
                title="Please Drink Water Now!!",
                message="Kindly take the water",
                app_icon="C:\\Users\\hp\\PycharmProjects\\pythonProject\\waterimage.ico",
                timeout=5
            )
        time.sleep(5)
