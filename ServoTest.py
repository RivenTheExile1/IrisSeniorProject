#cant get servo to stop turning. but i got it turning.

import RPi.GPIO as GPIO
import time
import keyboard

GPIO.setwarnings(False)
servoPIN = 17 #pin i chose
GPIO.setmode(GPIO.BCM) #sets to read off of board

GPIO.setup(servoPIN, GPIO.OUT) #sets up GPIO pin?
servo = GPIO.PWM(servoPIN, 50) #what pin and the frequency of use
angle = 90 #this doesnt get use but i can

servo.start(0) #start pWM runing, but with a value of 0 (pusle off)

#PMW can only go from 2.5 to 12.5

#eq1 for degree in to time sleep
#1 deg ~ .0029 time sleep 
"""
servo.ChangeDutyCycle(5) # '5' turns the motor counter clock wise '10' turns clockwise
time.sleep(.522) #closest to 180 deg that i care to get

servo.ChangeDutyCycle(0) #i choose '0' as my duty cycle cause no turn on zero
time.sleep(5) #needs an interim step to stop motor turrning 

servo.ChangeDutyCycle(5)
time.sleep(.261) #90 deg
"""

while True: #making the loop to constantly detect the keyboard
    try: #error catcher
        imp = input("how far do you want to go? ")
        if (imp == "90"): #angle desired
            servo.ChangeDutyCycle(5) #counter clock wise
            time.sleep(.261) #should go 90 based of eq1 above
            servo.ChangeDutyCycle(0) #i choose '0' as my duty cycle cause no turn on zero
            time.sleep(.01) #needs an interim step to stop motor turrning 
        elif (imp == "180"):
            servo.ChangeDutyCycle(5)
            time.sleep(.522) #180
            servo.ChangeDutyCycle(0) #i choose '0' as my duty cycle cause no turn on zero
            time.sleep(.01) #needs an interim step to stop motor turrning 
        elif (imp == "270"):
            servo.ChangeDutyCycle(5)
            time.sleep(.783) #270
            servo.ChangeDutyCycle(0) #i choose '0' as my duty cycle cause no turn on zero
            time.sleep(.01) #needs an interim step to stop motor turrning 
        elif (imp == "360"):
            servo.ChangeDutyCycle(5)
            time.sleep(1.044) #360#
            servo.ChangeDutyCycle(0) #i choose '0' as my duty cycle cause no turn on zero
            time.sleep(.01) #needs an interim step to stop motor turrning 
        elif (imp == "quit"):
            print("fine")
            break
    except:
        break #incase another key is pressed goes out side of the except loop

servo.stop()
GPIO.cleanup()
    
