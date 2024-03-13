import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)

for i in range(5):
    print("Turn on!")
    GPIO.output(2, True)
    sleep(0.5)
    print("Turn off!")
    GPIO.output(2, False)
    sleep(0.5)

print("Done!")

GPIO.cleanup()