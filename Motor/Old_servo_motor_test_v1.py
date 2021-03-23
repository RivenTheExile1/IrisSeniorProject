#pip3 install keyboard type this in before you run
#connect the red wire to pin 1, Black to pin 6, and white to pin 11 (GPIO170
#THIS CODE IS NOT TESTED. MY PI BROKE IN THE TRANSPORTATION TO SAN ANTONIO.

#Purpose:
    # 1) To set up the pi so that when we press the 'd' key the servo will turn 90 degrees
    # 1.1) It doesn't matter which way it turns with the current design of one motor.
    #2) Let's hope this works.
import RPi.GPIO as GPIO
import time
import keyboard


servoPIN = 17
GPIO.setmode(GPIO.BOARD)

GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)

p.start(7.5)


while True: #making the loop to constantly detect the keyboard
    try: #error catcher
        if keyboard.is_pressed('d'): #our dropping key
            p.ChangeDutyCycle(5)
            time.sleep(1)
            break
        else:
            pass # look up documentation this
    except:
        break #incase another key is pressed goes out side of the except loop
