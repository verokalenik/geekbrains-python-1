import time


class TrafficLight:

    def __init__(self):
        self.color = "red"

    def running(self):
        if self.color == "red":
            print("Red light for 7 seconds")
            time.sleep(7)
            self.color = "yellow"
        elif self.color == "yellow":
            print("Yellow light for 2 seconds")
            time.sleep(2)
            self.color = "green"
        elif self.color == "green":
            print("Green light for 5 seconds")
            time.sleep(5)
            self.color = "red"


trafic_light = TrafficLight() # creating an instance of class

while True:
    trafic_light.running()