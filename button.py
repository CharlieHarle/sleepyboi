import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


PIN_NUMBER = 28

GPIO.setup(PIN_NUMBER, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(PIN_NUMBER)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
