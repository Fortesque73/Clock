from datetime import datetime
import time



class Clock:
    #alarmTime=datetime, currentTime=datetime
    def __init__(self, alarmTime, currentTime):
        self.currentTime =  datetime.now()
        self.cuerrentTime = self.currentTime.strftime("%d-%m-%Y %H:%M:%S")
        self.alarm = alarmTime
        self.alarmNoMilis = self.alarm.strftime("%d-%m-%Y %H:%M:%S")

    #updates current time in string
    def updateCurrentTime(self):
        self.currentTime = datetime.now()
        self.currentTimeNoMilis = self.currentTime.strftime("%d-%m-%Y %H:%M:%S")

    #prints current time in string format every second
    def show(self):
        self.updateCurrentTime()
        print (self.currentTimeNoMilis, end="\r")
        


    #If current time and alarm time are equal return true
    def alarmSound(self):
        if self.currentTimeNoMilis == self.alarmNoMilis:
            return True
        else:
            return False

currentTime = datetime.now()
alarm = datetime(2019, 1, 28, 16, 47, 32, 00)
clock = Clock(alarm, currentTime)
exit = False
print ("alarm "+clock.alarmNoMilis)
while exit is False:
    clock.show()
    if clock.alarmSound() == True:
        exit = True
        
    time.sleep(1)
print("Pasa algo")
