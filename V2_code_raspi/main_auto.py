########################################################################
# This is the main script that is used to capture multiple images in a 
# quick and automated manner. This version is for automated control

# main_auto.py is for automated capture for the motorised system 
# main.py is for manual jig movements

# User sets configuration at runtime, and it cannot be changed after. 
# Whilst slightly inconvenient, this method is much easier to implement
# than allowing changes at runtime.
########################################################################


# SETUP 
from time import sleep 
from picamera2 import Picamera2, Preview
from os import listdir
from datetime import datetime

# Counter to record user behaviour and systems state
image_counter = 0


help_message_input = """
         Now, configure the camera's settings. Press enter if unsure/want defaults.
			- resolution : set a resolution value
				--> 2592, 1944
				--> 1920,1440
				--> 1600,1200
				--> 1024,768
				--> 640,480
				--> 320,240
				
			- brightness : float from -1 [very dark] --> 1[bright]
			- exposuretime: consult documentation for camera being used
			- sharpness : float from 0 [no sharpening], 1 [default/normal] --> 16"
         """
         
help_message = """This is a script to capture multiple images with the PiCamera (WITH motorised control)
         
         The following commands are valid (in lower_case). Write them as seen in the message below. 
         
         - capture : capture a single image (with the configured settings)
         - preview : preview the image being captured (press ENTER to close preview)
         - exit : exit the program
         - help : display this message
         - list : list the images that have already been captured
         - stateconfig : states the camera's current configuration. This can only be configured at the start. 
         """

print(help_message_input)
print(help_message)
# Flag to tell program to quit
exit = False
# Counts the total number of images taken to give each image a unique name
img_total = 0
user_config = {}
now = datetime.now() 
current_time = now.strftime("%H:%M:%S")


res_width = input("res_width")
res_height = input("res_height")
Brightness = input("brightness") 
ExposureTime = input("exposure time")
Sharpness = input("sharpness")

	 

# Setup the camera
cam = Picamera2()
still_config = cam.create_still_configuration()

if res_width != "" and res_height != "":
	resolution = tuple([int(res_width), int(res_height)])
	still_config["size"] = resolution
	
if Brightness != "": 
	still_config["controls"]["Brightness"] = float(Brightness)
	
if ExposureTime != "":
	still_config["controls"]["ExposureTime"] = ExposureTime
	
if Sharpness != "":
	still_config["controls"]["Sharpness"] = Sharpness 
	
cam.configure(still_config)


def main_loop(img_total):
    user_input = input("Enter a command: ")
    
    if user_input == "capture":
        img_name = str(input("Name your image: (or press Enter for default naming)"))
        if img_name == "":
            img_name = "image_" + str(img_total) + "_" + current_time + ".jpg"
            
        # Default setting for the rest of the capture parameters should be sufficent    
        cam.start_and_capture_file(img_name, delay=3)
        img_total += 1
        print("img_total:", img_total)

    # elif user_input == "preview":
        # cam.start_preview()
        # sleep(5) 
        # cam.stop_preview()

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
        
    return img_total

while exit == False:    
    main_loop(img_total)




























