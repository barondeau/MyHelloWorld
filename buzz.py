#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
buzz_pin = 32
GPIO.setup(buzz_pin, GPIO.OUT)
Buzz= GPIO.PWM(buzz_pin, 1000)
def buzz(freq,seconds):
    Buzz.start(50)
    Buzz.ChangeFrequency(freq)
    time.sleep(seconds)
    Buzz.stop()

buzz(440,1)
buzz(880,1)
buzz(220,1.5)
buzz(1100,1)
buzz(1320,1)


GPIO.cleanup()
