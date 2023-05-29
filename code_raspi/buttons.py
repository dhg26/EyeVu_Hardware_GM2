import RPi.GPIO as GPIO
from camera_setting_functions import *
from initial_capture import *
from adafruit_motorkit import MotorKit
from time import sleep 
from picamera import PiCamera

#We will need to say that to know which mode we are in can just light up LEDs for each mode and that we should save the images to a usb drive

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the buttons
button1_pin = 1
button2_pin = 2
button3_pin = 3
button4_pin = 4
button5_pin = 5
button6_pin = 6
button7_pin = 7
button8_pin = 8

# Set the GPIO pins as inputs with pull-up resistors
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button4_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button5_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button6_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button7_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button8_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

resolution_array = [1,2,3,4,5,6]
exposure_array = ['auto','night'] #put more in
effect_array =['none', 'denoise'] # put more in

resolution_counter = 0
exposure_counter = 0
effect_counter = 0
image_counter = 0

kit = MotorKit()

# Define the callback functions for button presses
def button1_callback(channel):
    # Code to run when button 1 is pressed
    print("Button 1 pressed")
    resolution = resolution_array[resolution_counter % len(resolution_array)]
    set_res(resolution)
    resolution_counter += 1

def button2_callback(channel):
    # Code to run when button 2 is pressed
    print("Button 2 pressed")
    exposure = exposure_array[exposure_counter % len(exposure_array)]
    set_exp(exposure)
    exposure_counter += 1

def button3_callback(channel):
    # Code to run when button 3 is pressed
    print("Button 3 pressed")
    effect = effect_array[effect_counter % len(effect_array)]
    set_effect(effect)
    effect_counter += 1

def button4_callback(channel):
    # Code to run when button 4 is pressed
    print("Button 4 pressed")
    capture(image_counter)
    image_counter += 1

def button5_callback(channel):
    #rotate_clockwise()
    kit.stepper1.onestep(direction=MotorKit.FORWARD)

def button6_callback(channel):
    #rotate_counterclockwise()
    kit.stepper1.onestep(direction=MotorKit.BACKWARD)
        
def button7_callback(channel):
    #rotate_clockwise()
    kit.stepper2.onestep(direction=MotorKit.FORWARD, style=MotorKit.DOUBLE)

def button8_callback(channel):
    #rotate_counterclockwise()
    kit.stepper2.onestep(direction=MotorKit.BACKWARD, style=MotorKit.DOUBLE)



# Add event detection for button presses
GPIO.add_event_detect(button1_pin, GPIO.FALLING, callback=button1_callback, bouncetime=200)
GPIO.add_event_detect(button2_pin, GPIO.FALLING, callback=button2_callback, bouncetime=200)
GPIO.add_event_detect(button3_pin, GPIO.FALLING, callback=button3_callback, bouncetime=200)
GPIO.add_event_detect(button4_pin, GPIO.FALLING, callback=button4_callback, bouncetime=200)
GPIO.add_event_detect(button1_pin, GPIO.FALLING, callback=button5_callback, bouncetime=200)
GPIO.add_event_detect(button2_pin, GPIO.FALLING, callback=button6_callback, bouncetime=200)
GPIO.add_event_detect(button3_pin, GPIO.FALLING, callback=button7_callback, bouncetime=200)
GPIO.add_event_detect(button4_pin, GPIO.FALLING, callback=button8_callback, bouncetime=200)

# Main program loop (keep the script running)
try:
    while True:
        pass

except KeyboardInterrupt:
    GPIO.cleanup()