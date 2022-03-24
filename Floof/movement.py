from sense_hat import SenseHat
import time
import threading

sense = SenseHat()

red=(255,0,0)
pastFiveReadings = []

def RecordMovement():

    while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x=abs(x)
        y=abs(y)
        z=abs(z)

        if x>1 or y>1 or z>1:
            print("x: {0}, y: {1}, z: {2}".format(x,y,z))
            #return True
        else:
            #sense.clear()
            #return False
            print("false")

        # if (x >= y) and (x >= z):
        #     largest = x
        # elif (y >= x) and (y >= z):
        #     largest = y
        # else:
        #     largest = z

        # pastFiveReadings.append(largest)
        # if len(pastFiveReadings) > 5:
        #     pastFiveReadings.pop(0)

        # #if x>2 or y>2 or z>2:
        # print(pastFiveReadings)

        time.sleep(1)

def IsMoving():
    if any(i > 1 for i in pastFiveReadings):
        ClearRecord()
        print("Accelerometer readings: " + str(pastFiveReadings))
        #sense.show_letter("!", red)
        return True
    else:
        #sense.clear()
        return False
        #print("false")

def ClearRecord():
    pastFiveReadings = []


# lock = threading.Lock()
# th = threading.Thread(target = RecordMovement)
# with lock:
#     th.start()

# while True:
#     time.sleep(5)
#     print("ismoving")
#     IsMoving()

#RecordMovement()

th = threading.Thread(target = RecordMovement)
th.start()