import os

from flask import g, current_app

from .utils import Singleton


class MediaFinder(metaclass=Singleton):
    def __init__(self, path):
        self.path = path
        self._collection = []
        for root, dirs, files in os.walk(path):
            for name in files:
                fname = os.path.abspath(os.path.join(root, name))
                size = os.stat(fname).st_size
                self._collection.append({'name': fname, 'size': size})

        self._collection.sort(key=lambda x: x['name'])
        self._collection = {x['name']: x['size'] for x in self._collection}

    @property
    def collection(self):
        return self._collection


def get_media_finder():
    if 'media_finder' not in g:
        g.media_finder = MediaFinder(current_app.config['MEDIA_DIR'])
    return g.media_finder
