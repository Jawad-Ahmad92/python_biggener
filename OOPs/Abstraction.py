# Abstraction ---> hiding implemataion proccess to user only shoe essential (important) step
# hiding what actul do in reall to user


class car:
    def __init__(self):
        self.accelator = False  # false --> not press
        self.brek = False
        self.cluch = False

    def start_car(self):
        self.accelator = True  # true --> press the acc
        self.cluch = True
        print("Car start")


c1 = car()
c1.start_car()


# output-->"Car start"  --they hide the actual data and process they only show user important details/info
