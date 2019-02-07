from datetime import datetime
import time
import vlc


class Alarm:
    def __init__(self, alarmTime, ringtone):
        self.time=alarmTime
        self.timeNoMilis = alarmTime.strftime("%d-%m-%Y %H:%M:%S") #time in string
        if(len(ringtone)>0):
            self.ringtone=ringtone
        else:
            self.ringtone='default'

    def play(self):
        #here some code that makes the alarm sound
        track=vlc.MediaPlayer('./media/%s.mp3' % (self.ringtone))

        #some thread management here
        track.play()

class Clock:
    #alarmTime=datetime, currentTime=datetime
    def __init__(self, currentTime):
        self.currentTime =  datetime.now()
        self.cuerrentTime = self.currentTime.strftime("%d-%m-%Y %H:%M:%S")
        self.alarms = []
        self.numalarms=0

    #set an alarm manually
    def setalarm(self):
        hour=raw_input("introduce alarm's hour: ")
        minute=raw_input("introduce minute: ")
        addalarm(hour, minute)

    #add the alarm to the list hour=int, minute=int
    def addalarm(self, hour, minute):
        curr=datetime.now()
        hour%=24
        minute%=60
        self.alarms.append(Alarm(datetime(curr.year, curr.month, curr.day, hour, minute, 00, 00)))
        self.numalarms+=1

    #add alarms for debugging, newalarm=Alarm
    def quickalarm(self, newalarm):
        self.alarms.append(newalarm)
        self.numalarms+=1

    #updates current time in string
    def updateCurrentTime(self):
        self.currentTime = datetime.now()
        self.currentTimeNoMilis = self.currentTime.strftime("%d-%m-%Y %H:%M:%S")

    #prints current time in string format every second
    def show(self):
        self.updateCurrentTime()
        print (self.currentTimeNoMilis, end="\r")

    #If current time and any alarm time are equal return true
    def checkAlarms(self):
        i=0
        while (i<self.numalarms) :
            if self.currentTimeNoMilis == self.alarms[i].timeNoMilis:
                return i
            i+=1
        return -1

    def showAlarms(self):
        i=0
        while (i<self.numalarms):
            print('Alarm %d: %s ' % (i, self.alarms[i].timeNoMilis))
            i+=1


def main():
    #First create a clock instance
    currentTime = datetime.now()
    clock=Clock(currentTime)
    #create some alarms
    alarmtime = datetime(2019, 2, 3, 1, 56, 20, 00)
    alarm=Alarm(alarmtime, "")

    if(currentTime.second>=50):
        alarm2=Alarm(datetime(
            currentTime.year, currentTime.month, currentTime.day,
            currentTime.hour, currentTime.minute+1, 0, 0 ), "")
    else:
        alarm2=Alarm(datetime(
            currentTime.year, currentTime.month, currentTime.day, currentTime.hour, currentTime.minute, currentTime.second+5, 0
        ), "")

    #add the alarms to the clock
    clock.quickalarm(alarm)
    clock.quickalarm(alarm2)

    #show the added alarms
    clock.showAlarms()

    while 1:
        clock.show()
        sound=clock.checkAlarms()#sound=int with the alarms' id that will sound
        if sound >= 0:
            clock.alarms[sound].play()
            print('sonido pa tu culo')
            print(sound)
        time.sleep(1)


if __name__ == "__main__" :
    main()

