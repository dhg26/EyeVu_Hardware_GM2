# Basic test to see if PiCam 3 is configured correctly, and all relevant drivers/
# libraries are installed and configured 

from picamera2 import Picamera2, Preview
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
cam = Picamera2()

GPIO.setup(18,GPIO.OUT)

GPIO.output(18,GPIO.HIGH)

cam.start_and_capture_file("test3.jpg", delay=300)
GPIO.output(18,GPIO.LOW)