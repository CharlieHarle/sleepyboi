from os import listdir
import time
import datetime
import logging
import pygame
import RPi.GPIO as GPIO

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('/home/sleepy/projects/sleepyboi/output.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

pygame.mixer.init()
player = pygame.mixer.music

GPIO.setmode(GPIO.BCM)
NEXT_PIN = 20
VOL_UP_PIN = 19
VOL_DOWN_PIN = 12
GPIO.setup(NEXT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(VOL_UP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(VOL_DOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# volume from 0.0 to 1.0
MAX_VOLUME = 1.0

TRACKS = listdir("tracks/")

# TRACKS = [
#     'IrishCoast.mp3',
#     'LakeLife.mp3',
#     'PrimevalForest.mp3',
#     'UnrealOcean.mp3'
# ]

class Sleeper:

    def __init__(self):
        self.now = datetime.datetime.now()
        self.init_buttons()
        self.volume_interval = MAX_VOLUME / 10
        self.currently_playing = None
        self.number_of_songs = len(TRACKS)
        self.start()

    def start(self):
        try:
            player.set_volume(1)
            self.play_next_song()
            while True:
                pygame.time.Clock().tick(10)
                # while player.get_busy():
        except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
            self.stop()
            logger.info('Play Stopped by user')
        except Exception:
            logger.error('Oops, an unhandled error occurred! Bye')
            self.stop()

    def next_pressed(self, channel):
        logger.info('Skip to next song')
        self.play_next_song()

    def init_buttons(self):
        logger.info('Initialising buttons ')
        GPIO.add_event_detect(NEXT_PIN, GPIO.FALLING, callback=self.next_pressed, bouncetime=200)
        GPIO.add_event_detect(VOL_UP_PIN, GPIO.FALLING, callback=self.volume_up, bouncetime=200)
        GPIO.add_event_detect(VOL_DOWN_PIN, GPIO.FALLING, callback=self.volume_down, bouncetime=200)
        logger.info('Buttons initialised')

    def play(self, filename):
        path = 'tracks/{}'.format(filename)
        player.load(path)
        player.play(-1)
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

    def volume_up(self, channel):
        new_volume = player.get_volume() + self.volume_interval
        rounded_new_volume = round(new_volume, 1)
        if 0.0 <= rounded_new_volume <= MAX_VOLUME:
            player.set_volume(new_volume)
            logger.info('Volume set to {}%'.format(rounded_new_volume*100))
        else:
        logger.info('Volume already at {}%'.format(rounded_new_volume*100))

    def volume_down(self, channel):
        new_volume = player.get_volume() - self.volume_interval
        rounded_new_volume = round(new_volume, 1)
        if 0.0 <= rounded_new_volume <= MAX_VOLUME:
            player.set_volume(new_volume)
            logger.info('Volume set to {}%'.format(rounded_new_volume*100))
        else:
        logger.info('Volume already at {}%'.format(rounded_new_volume*100))

    def reset_volume(self):
        default_volume = MAX_VOLUME / 2
        player.set_volume(default_volume)
        logger.info('Volume set to {}%'.format(default_volume*100))

    def stop(self):
        GPIO.cleanup()
        player.stop()
        logger.info('Stopping player')

if __name__ == '__main__':
    logger.info('Starting sleepyboi')
    Sleeper()
