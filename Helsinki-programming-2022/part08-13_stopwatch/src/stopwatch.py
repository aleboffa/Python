# Write your solution here:
from re import M

class Stopwatch:
    def __init__(self):
        self.seconds = 50
        self.minutes = 59

    def tick(self):
        if self.minutes <= 59:
            if self.seconds < 59:
                self.seconds += 1
            else:
                self.minutes += 1
                self.seconds = 0
        else:
            self.minutes = 0
            self.seconds = 0
    
    # This method returns the state of the object in string format
    def __str__(self):
        from datetime import datetime

        min = self.minutes
        sec = self.seconds

        return f"{min:2}:{sec:2}"


if __name__ == "__main__":

    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()

#       print(x.strftime("%B"))
#  datetime.strptime("2018-01-31", "%Y-%m-%d")
 
# dateString = "Monday, July 16, 2018 20:01:56"
# dateFormatter = "%A, %B %d, %Y %H:%M:%S"
# datetime.strptime(dateString, dateFormatter)