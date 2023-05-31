# Basic test to see if PiCam 3 is configured correctly, and all relevant drivers/
# libraries are installed and configured 

from picamera2 import Picamera2
picam2 = Picamera2()
picam2.start_and_record_video("test.mp4", duration=5)
