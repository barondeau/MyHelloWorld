#!/usr/bin/env python
import random 
import RPi.GPIO as GPIO
import time
x =0
#generate a random number from 1 to 10

y=random.randint(1,10)
counter=0
b = True
c=1
#while loop infinte till b = False
while b == True:
    if b==True:
        x=raw_input("Enter a number 1-10 ")
        counter=counter+c
    if int(x)>int(y):
        print "Your guess is too high "
    elif int(x)<int(y):
        print "Your guess is too low"
    else:
        print "You got the number ", y
        print "It took you", counter, "many guesses"
        b=False
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        led_pin = 11
        GPIO.setup(led_pin, GPIO.OUT)
        GPIO.output(led_pin, True)
        time.sleep(2)
        GPIO.output(led_pin,False)
        GPIO.cleanup()
        break
        
    
