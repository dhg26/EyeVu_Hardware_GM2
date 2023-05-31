########################################################################
# This is the main script that is used to capture multiple images in a 
# quick and automated manner. This version is for automated control

# main_auto.py is for automated capture for the motorised system 
# main.py is for manual jig movements
########################################################################

# SETUP 
from time import sleep 
from picamera2 import Picamera2, Preview
from os import listdir
from datetime import datetime
from adafruit_motorkit import MotorKit
import cam_set
import motor_control

# Counter to record user behaviour and systems state
image_counter = 0


help_message = """Script to capture multiple images with the PiCamera (WITH motorised control)
         The following commands are valid (in lower_case). Write them as seen in the message below. 
         - capture : capture a single image (with the configured settings)
         - preview : preview the image being captured (press ENTER to close preview)
         - exit : exit the program
         - help : display this message
         - list : list the images that have already been captured
         - exposure : set an exposure mode for camera
         - effect : set an image effect for camera
         - """
    
        
# Resolution help message not needed - it cannot be changed at runtime 
#         - resolution : set a resolution value from 1-6 (6 highest resolution)
#                --> 1 = (2592, 1944)
#                --> 2 = (1920,1440)
#                --> 3 = (1600,1200)
#                --> 4 = (1024,768)
#                --> 5 = (640,480)
#                --> 6 = (320,240)


print(help_message)
# Flag to tell program to quit
exit = False
# Counts the total number of images taken to give each image a unique name
img_total = 0


# Setup the camera
camera = PiCamera2()

# Set default mode for high-res stills before other settings are applied later 
still_config = picam2.create_still_configuration(



# MAIN LOOP
def main_loop(img_total):
    user_input = input("Enter a command: ")
    if user_input == "capture":
        img_name = str(input("Name your image: (or press Enter for default naming)"))
        camera.start_preview()
        sleep(3)

        if img_name == "":
            now = datetime.now() 
            current_time = now.strftime("%H:%M:%S")
            img_name = "image_" + str(img_total) + "_" + current_time + ".jpg"
    
        camera.capture(img_name)
        camera.stop_preview()
        img_total += 1

    elif user_input == "preview":
        camera.start_preview()
        sleep(5) 
        camera.stop_preview()

    elif user_input == "help":
        print(help_message)

    elif user_input == "list":
        print("List of images")
        print("--------------")
        for i in os.listdir():
            if i.endswith(".jpg"):
                print(i)

    elif user_input == "exit":
        exit == True
    
    # elif user_input == "resolution":
        # Method is not useful as here as resolution cannot be changed at runtime. 
        
        # res_input = input("Enter resolution from 1-6: ")
        # set_res(res_input)
        # sleep(2)
    
    elif user_input == "exposure":
        exp_input = input("Enter exposure mode: ")
        set_exp(exp_input)
        sleep(2)
    
    elif user_input == "effect":
        effect_input = input("Enter efect setting: ")
        set_effect(effect_input)
    
    else: 
        print("Invalid command, please try again")
        print(help_message)
    
    elif user_input == "clockwise1":
        #rotate_clockwise()
        kit.stepper1.onestep(direction=MotorKit.FORWARD)

    elif user_input == "counterclockwise1":
        #rotate_counterclockwise()
        kit.stepper1.onestep(direction=MotorKit.BACKWARD)
        
    elif user_input == "clockwise2":
        #rotate_clockwise()
        kit.stepper2.onestep(direction=MotorKit.FORWARD, style=MotorKit.DOUBLE)

    elif user_input == "counterclockwise2":
        #rotate_counterclockwise()
        kit.stepper2.onestep(direction=MotorKit.BACKWARD, style=MotorKit.DOUBLE)

while exit == False:    
    img_total = main_loop(img_total)




# ----- No need for this currently - this code is for when autofocus is implemented in the final product, and buttons are required. 
#We will need to say that to know which mode we are in can just light up LEDs for each mode and that we should save the images to a usb drive

# # Define the GPIO pins for the buttons
# button1_pin = 1
# button2_pin = 2
# button3_pin = 3
# button4_pin = 4
# button5_pin = 5
# button6_pin = 6
# button7_pin = 13
# button8_pin = 19

# # Set the GPIO pins as inputs with pull-up resistors
# GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(button3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(button4_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(button5_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(button6_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(button7_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(button8_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Set the GPIO mode to BCM
# GPIO.setmode(GPIO.BCM)

