from datetime import datetime
import time

class Clock:
    #Init clock with a previous set alarm
    def __init__(self, datetime):
        self.alarm = datetime

    #returns current time in string
    def getCurrentTime(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    #prints current time in string format every second
    def show(self):
        while True :
            print (self.getCurrentTime(), end="\r")
            time.sleep(1)

    def alarm(self):
        self.alarm = self.alarm.strftime("%d-%m-%Y %H:%M:%S")

    def showAlarm(self):
        print (self.alarm)


alarm = datetime(2019, 1, 26, 18, 5, 00, 00)
x = Clock(alarm)
x.showAlarm()
