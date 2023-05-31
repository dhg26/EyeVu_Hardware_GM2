from picamera2 import Picamera2, Preview
from time import sleep

resolution_array = [1,2,3,4,5,6]
exposure_array = ['auto','night'] #put more in
effect_array =['none', 'denoise'] # put more in

resolution_counter = 0
exposure_counter = 0
effect_counter = 0


def set_res(resolution_setting):
  if resolution_setting == 6:
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    print("resolution set to 6")
  elif resolution_setting == 5:
    camera.resolution = (1920,1440)
    print("resolution set to 5")
  elif resolution_setting == 4:
    camera.resolution = (1600,1200)
    print("resolution set to 4")
  elif resolution_setting == 3:
    camera.resolution = (1024,768)
    print("resolution set to 3")
  elif resolution_setting ==  2:
    camera.resolution = (640,480)
    print("resolution set to 2")
  elif resolution_setting == 1:
    camera.resolution = (320,240)
    print("resolution set to 1")
  else:
    print('No such resolution')
  
def set_exp(exposure_setting):
  try:
    camera.exposure_mode = exposure_setting
    print('Exposure mode set to ' + exposure_setting)
  except: 
    print('Error: no such mode. Exposure mode set to auto')

def set_effect(effect_setting):
  try:
    camera.image_effect = effect_setting
    print('Effect setting set to ' + effect_setting)
  except: 
    print('Error: no such mode. Effect setting set to none')
