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

pygame.mixer.init()
player = pygame.mixer.music

# on/off
# toggle noises
# volume

TRACKSLOCATION = 'tracks/'
# volume from 0.0 to 1.0
MAX_VOLUME = 1.0

TRACKS = [
    'IrishCoast.mp3',
    'LakeLife.mp3',
    'PrimevalForest.mp3',
    'UnrealOcean.mp3'
]

class Sleeper:

    def __init__(self):
        self.now = datetime.datetime.now()
        self.volume_interval = MAX_VOLUME / 10
        self.currently_playing = None
        self.number_of_songs = len(TRACKS)
        self.init_buttons()
        self.start()

    def start(self):
        try:
            self.play_next_song()
        except:
            logger.error('An unhandled error occured')


    def init_button():
        GPIO.setup(pin_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pin_next_button, GPIO.FALLING, callback=next_pressed)
        GPIO.add_event_detect(pin_volume_up_button, GPIO.FALLING, callback=volume_up_button)

    def next_pressed(channel):
        self.play_next_song()

    def next_pressed(channel):
        self.play_next_song()

    def next_pressed(channel):
        self.play_next_song()

    # def init_GPIO(self):
    #     GPIO.setmode(GPIO.BCM)
    #     GPIO.setup(POWER_SWITCH_CHANNEL, GPIO.IN)
    #     GPIO.setup(LCD_CHANNEL, GPIO.OUT)

    # def clear_display(self):
    #     lcddisplay.lcd_clear()

    # def display(self, message, line):
    #     self.clear_display()
    #     lcddisplay.lcd_display_string(message, line)

    # def play_with_omxplayer(self, filename):
    #     if self.play_process:
    #         self.stop()
    #     full_path = TRACKLOCATION + filename
    #     logger.info('Starting track - filename={}'.format(filename))
    #     self.play_process = subprocess.Popen(['omxplayer', full_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

    # def stop_with_omxplayer(self):
    #     logger.info('Stopping player')
    #     self.play_process.stdin.write('q')

    def play(self, filename):
        path = 'tracks/{}'.format(filename)
        player.load(path)
        player.play(loops=-1)
        self.currently_playing = filename
        logger.info('Playing song - filename={}'.format(filename))

    def play_next_song(self):
        if self.currently_playing:
            current_index = TRACKS.index(self.currently_playing)
            next_index = current_index + 1
            if next_index < self.number_of_songs:
                next_song = TRACKS[next_index]
                self.play(next_song)
                return
        next_song = TRACKS[0]
        self.play(next_song)

    def volume_up(self):
        new_volume = player.get_volume() + self.volume_interval
        player.set_volume(new_volume)
        logger.info('Volume set to {}%'.format(new_volume*100))

    def volume_down(self):
        new_volume = player.get_volume() - self.volume_interval
        player.set_volume(new_volume)
        logger.info('Volume set to {}%'.format(new_volume*100))

    def reset_volume()
        default_volume = MAX_VOLUME / 2
        player.set_volume(default_volume)
        logger.info('Volume set to {}%'.format(default_volume*100))

    def stop(self):
        player.stop()
        logger.info('Stopping player')

if __name__ == '__main__':
    logger.info('Starting sleepyboi')
    Sleeper()
