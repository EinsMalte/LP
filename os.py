import time
import RPi.GPIO as GPIO

print("OS Start")
print("Willkommen")

running = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
while(running == True):
    GPIO.output(18, GPIO.HIGH)
    print("LED ON")
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
    print("LED OFF")
