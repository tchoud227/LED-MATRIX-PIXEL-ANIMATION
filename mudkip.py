#Tanim Choudhury

#Interfaced Raspberry Pi with an 8x8 LED matrix from a Sense HAT.
#Objective is to have a system that wakes mudkip after the middle button is pressed.
#Otherwise, mudkip blinks and slolwy closes his eyes again.
#After 3 middle button presses, the  8x8 LED matrix will clearn screen then exit program



#libraries for senseHat and time functions
from sense_hat import SenseHat
import time

#refrencing SenseHat with sense
# As well as clearing 8x8 led matrix 
sense = SenseHat()
sense.clear()

#color declarations to make array patterns visually simpler
#As well as changing color values only once
g = (0, 153, 0) #green
b = (51, 153, 255) #blue
o = (255, 153, 51) # orange
w = (230, 242, 255) #white-blue
e = (0, 0, 0) #black

#pattern for eyes wide awake
mudkip1 = [
    g, g, g ,g, g, g, g, g,
    g, g, g ,b, b, g, g, g,
    g, g, g ,b, b, g, g, g,
    g, g, g ,b, b, g, g, g,
    g, b, b ,b, b, b, b, g,
    o, b, e ,b, b, e, b, o,
    o, b, e ,b, b, e, b, o,
    g, w, w ,w, w, w, w, g
    ]

#pattern for eyes slighty open
mudkip2 = [
    g, g, g ,g, g, g, g, g,
    g, g, g ,b, b, g, g, g,
    g, g, g ,b, b, g, g, g,
    g, g, g ,b, b, g, g, g,
    g, b, b ,b, b, b, b, g,
    o, b, b ,b, b, b, b, o,
    o, b, e ,b, b, e, b, o,
    g, w, w ,w, w, w, w, g
    ]

#pattern for eyes closed
mudkip3 = [
    g, g, g ,g, g, g, g, g,
    g, g, g ,b, b, g, g, g,
    g, g, g ,b, b, g, g, g,
    g, g, g ,b, b, g, g, g,
    g, b, b ,b, b, b, b, g,
    o, b, b ,b, b, b, b, o,
    o, b, b ,b, b, b, b, o,
    g, w, w ,w, w, w, w, g
    ]

#dim for drak environment
sense.low_light = True

#mudkip's eyes blink for 
def blink():
    for i in range(2):
        time.sleep(0.5)
        sense.set_pixels(mudkip3)
        sense.set_pixels(mudkip1)
        time.sleep(0.5)
        sense.set_pixels(mudkip3)
        time.sleep(0.5)
        sense.set_pixels(mudkip1)
    time.sleep(2)
    sense.set_pixels(mudkip2)
    time.sleep(0.5)
    
#clear and exit
def end():
    sense.clear()
    exit()

#counter initilized to 0
count = 0

#mudkip wakes his eyes for 2 seconds when the middle button is pressed.
#8x8 by LED matrix turns off and exits after middle button is pressed 3 times.
#All other joystick inputs will make mudkip blink then slowly close his eyes.
while True:
    #clear and exit program when counter is 3
    if count == 3:
        end()
    
    #default mudkip is asleep
    sense.set_pixels(mudkip3)
    time.sleep(0.5)
    #joystick events
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            #any direction makes mudkip blink besides middle
            if event.direction == 'up':
                blink()
            elif event.direction == 'down':
                blink()
            elif event.direction == 'left':
                blink()
            elif event.direction == 'right':
                blink()
            #wakes mudkip for 1 second and end counter by 1
            elif event.direction == 'middle':
                sense.set_pixels(mudkip1)
                time.sleep(2)
                count += 1
                


