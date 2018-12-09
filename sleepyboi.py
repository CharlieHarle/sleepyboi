import os
import time
import datetime
import logging
from pytz import timezone
import subprocess
# import RPi.GPIO as GPIO
# import lcddriver

# POWER_SWITCH_CHANNEL = 1
# NEXT_SOUND_CHANNEL = 2
# LCD_CHANNEL = 3

# GPIO pins

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('/home/pi/projects/sleepyboi/output.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# lcddisplay = lcddriver.lcd()

# pygame.mixer.init()

# on/off
# toggle noises
# volume

TRACKLOCATION = 'tracks/'

TRACK_NAMES = {

}

TRACKS = [
    {
        'name': 'Irish Coast',
        'filename':  'IrishCoast.mp3',
    },
    {
        'name': 'Lake Life',
        'filename':  'LakeLife.mp3',
    },
    {
        'name': 'Primeval Forest',
        'filename':  'PrimevalForest.mp3',
    },
    {
        'name': 'Unreal Ocean',
        'filename':  'UnrealOcean.mp3',
    }
]

class Sleeper:

    def __init__(self):
        self.now = datetime.datetime.now()
        self.play('PrimevalForest.mp3')

    # def init_GPIO(self):
    #     GPIO.setmode(GPIO.BCM)
    #     GPIO.setup(POWER_SWITCH_CHANNEL, GPIO.IN)
    #     GPIO.setup(LCD_CHANNEL, GPIO.OUT)

    # def clear_display(self):
    #     lcddisplay.lcd_clear()

    # def display(self, message, line):
    #     self.clear_display()
    #     lcddisplay.lcd_display_string(message, line)

    def play(self, filename):
        full_path = TRACKLOCATION + filename
        print('starting track')
        play_process = subprocess.Popen(['omxplayer', '--no-keys', full_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        print('playing track - pid={}'.format(play_process))

    # def play_with_pygame(self, filename):
    #     full_path = TRACKLOCATION + filename
    #     pygame.mixer.music.load(full_path)
    #     pygame.mixer.music.play()
    #     while pygame.mixer.music.get_busy() == True:
    #         continue


if __name__ == '__main__':
    logger.info('Starting sleepyboi')
    Sleeper()
