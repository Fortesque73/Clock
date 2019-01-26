from datetime import datetime
import time

class Clock:
    #Init clock with a previous set alarm
    def __init__(self, alarmTime):
        self.currentTime =  datetime.now()
        self.cuerrentTime = self.currentTime.strftime("%d-%m-%Y %H:%M:%S")
        self.alarm = alarmTime
        self.alarm = self.alarm.strftime("%d-%m-%Y %H:%M:%S")

    #updates current time in string
    def updateCurrentTime(self):
        self.currentTime = datetime.now()
        self.cuerrentTime = self.currentTime.strftime("%d-%m-%Y %H:%M:%S")

    #prints current time in string format every second
    def show(self):
        self.updateCurrentTime()
        print (self.currrentTime end="\r")


    #If current time and alarm time are equal return true
    def alarmSound(self):
        if self.currentTime is self.alarm :
            return True

alarm = datetime(2019, 1, 26, 18, 28, 15, 00)
currentTime = datetime.now()
clock = Clock(alarm, currentTime)
exit = False
while exit is False:
    clock.show()
    if clock.alarmSound() is True:
        exit = True
        
    time.sleep(1)
print("Pasa algo")
