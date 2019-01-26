from datetime import datetime
import time

class Clock:

    def getCurrentTime(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def show(self):
        while True :
            print (self.getCurrentTime(), end="\r")
            time.sleep(1)

x = Clock()
x.show()