import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the buttons
button1_pin = 5
button2_pin = 6
button3_pin = 13
button4_pin = 19

# Set up GPIO pins for buttons
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button4_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define stepper motor step delay (adjust as needed)
step_delay = 0.001

# Function to rotate stepper motor clockwise
def rotate_clockwise():
    GPIO.output(dir_pin, GPIO.HIGH)  # Set direction pin HIGH for clockwise rotation
    for _ in range(200):  # Adjust this value according to your motor steps per revolution
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(step_delay)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(step_delay)

# Function to rotate stepper motor counterclockwise
def rotate_counterclockwise():
    GPIO.output(dir_pin, GPIO.LOW)  # Set direction pin LOW for counterclockwise rotation
    for _ in range(200):  # Adjust this value according to your motor steps per revolution
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(step_delay)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(step_delay)

# Set up GPIO pins for A4988 driver circuit
dir_pin = 17  # Change this pin according to your setup
step_pin = 27  # Change this pin according to your setup

GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)

# Main loop
try:
    while True:
        # Check button states
        button1_state = GPIO.input(button1_pin)
        button2_state = GPIO.input(button2_pin)
        button3_state = GPIO.input(button3_pin)
        button4_state = GPIO.input(button4_pin)

        # Drive motor 1 based on button states
        if button1_state == GPIO.LOW:
            rotate_clockwise()
        elif button2_state == GPIO.LOW:
            rotate_counterclockwise()

        # Drive motor 2 based on button states
        if button3_state == GPIO.LOW:
            rotate_clockwise()
        elif button4_state == GPIO.LOW:
            rotate_counterclockwise()

except KeyboardInterrupt:
    pass

# Clean up GPIO pins
GPIO.cleanup()
