# Basic test to see if PiCam 3 is configured correctly, and all relevant drivers/
# libraries are installed and configured 

# Import the relevant libraries
from picamera2 import Picamera2, Preview
import RPi.GPIO as GPIO
from time import sleep

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
cam = Picamera2()

# Set up the camera
GPIO.setup(18,GPIO.OUT)

# Take a picture
GPIO.output(18,GPIO.HIGH)

# Preview the picture
cam.start_and_capture_file("test3.jpg", delay=300)
GPIO.output(18,GPIO.LOW)