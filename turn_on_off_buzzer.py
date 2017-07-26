#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32

GPIO.setup(buzz_pin, GPIO.OUT)

Buzz= GPIO.PWM(buzz_pin, 3000)

Buzz.start(99)

time.sleep(1)
Buzz.stop()

GPIO.cleanup()
