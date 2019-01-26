from datetime import datetime
import time

class Clock:
    #Init clock with a previous set alarm
    def __init__(self, datetime):
        self.alarm = datetime
        self.alarm = self.alarm.strftime("%d-%m-%Y %H:%M:%S")

    #returns current time in string
    def getCurrentTime(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    #prints current time in string format every second
    def show(self):
        print (self.getCurrentTime(), type(self.getCurrentTime), end="\r")
        time.sleep(1)

    #If current time and alarm time are equal return true
    def alarmSound(self):
        if self.getCurrentTime == self.alarm :
            return True

    def showAlarm(self):
        print (self.alarm)


alarm = datetime(2019, 1, 26, 18, 28, 15, 00)
clock = Clock(alarm)
exit = False
while exit is False:
    clock.show()
    if clock.alarmSound() is True:
        exit = True
print("Pasa algo")
