from sense_hat import SenseHat

sense = SenseHat()

red=(255,0,0)

def IsMoving():

    while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x=abs(x)
        y=abs(y)
        z=abs(z)

        if x>1 or y>1 or z>1:
            #print("{0}, {1}, {2}".format(x,y,z))
            #sense.show_letter("!", red)
            return True
        else:
            #sense.clear()
            return False
