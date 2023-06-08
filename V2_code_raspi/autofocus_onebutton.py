from time import sleep 
from picamera2 import PiCamera2, Preview
import RPi.GPIO as GPIO
from adafruit_motorkit import MotorKit

button1_pin = 17

kit = MotorKit()
# Set up GPIO pins for buttons
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.OUT)
GPIO.setwarnings(False)

camera = PiCamera2()
camera.resolution = (2592, 1944)
print("image saved")

def button1_callback(channel):
    #rotate_clockwise()
    camera.preview()
    GPIO.output(18,GPIO.HIGH)
    for i in range(100):
        kit.stepper1.onestep(direction=MotorKit.FORWARD)
        camera.start_and_capture_file('image'+ str(i)+ '.jpg')
        sleep(0.01)
    GPIO.output(18,GPIO.LOW)
        

GPIO.add_event_detect(button1_pin, GPIO.FALLING, callback=button1_callback, bouncetime=200)

# Main program loop (keep the script running)
try:
    while True:
        pass

except KeyboardInterrupt:
    GPIO.cleanup()

