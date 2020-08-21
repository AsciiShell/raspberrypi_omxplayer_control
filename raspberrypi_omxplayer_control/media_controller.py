import enum

from flask import g
from omxplayer.player import OMXPlayer, OMXPlayerDeadError

from .utils import Singleton


class State(enum.Enum):
    wait = 1
    play = 2


class MediaControllerPlayException(Exception):
    pass


class MediaController(metaclass=Singleton):
    def __init__(self):
        self.state = State.wait
        self.player = None

    def play(self, path):
        if self.state == State.play:
            raise MediaControllerPlayException('already working')
        self.player = OMXPlayer(path)
        self.state = State.play

    def stop(self):
        try:
            self.player.stop()
        except MediaControllerPlayException:
            pass
        self.state = State.wait

    def pause(self):
        if self.state == State.wait:
            return
        self.player.play_pause()

    @property
    def get_position(self):
        if self.state == State.wait:
            return 0
        try:
            return self.player.position()
        except OMXPlayerDeadError:
            self.state = State.wait
        return 0

    @property
    def get_duration(self):
        if self.state == State.wait:
            return 0
        try:
            return self.player.duration()
        except OMXPlayerDeadError:
            self.state = State.wait
            return 0

    def set_position(self, position):
        if self.state == State.wait:
            return
        assert 0 <= position <= self.get_duration, 'Position out of range'
        diff = position - self.get_position
        self.player.seek(diff)


def get_media_controller():
    if 'media_controller' not in g:
        g.media_controller = MediaController()
    return g.media_controller
