# Setup 
from time import sleep 
from picamera import PiCamera
from os import listdir
from datetime import datetime


help_message = """Script to capture multiple images with the PiCamera (no motorised control)
         The following commands are valid (in lower_case)
         - capture: capture a single image
         - preview: preview the image being captured
         - exit: exit the program
         - help: display this message
         - list: list the images that have already been captured
         - """
        

print(help_message)
# Flag to tell program to quit
exit = False
# Counts the total number of images taken to give each image a unique name
img_total = 0

# Setup the camera
camera = PiCamera()
camera.resolution = (1024, 768)
# WEZ - add a sleep to allow the camera to warm up, + exposure, focus and other settings to be set


# Main loop that is stored continuously in memory
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
    
    else: 
        print("Invalid command, please try again")
        print(help_message)

while exit == False:    
    img_total = main_loop(img_total)
