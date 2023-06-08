from time import sleep 
from picamera import PiCamera

def capture(counter):
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    sleep(2)
    camera.capture('image' + str(counter)+ '.jpg')
    print("image saved")

capture(0)

