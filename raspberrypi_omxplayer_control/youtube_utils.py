import logging

import yt_dlp

logger = logging.getLogger(__name__)


def get_video_url(url):
    options = {
        'format': 'best',
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        logger.info('video {} info:\n{}', url, info_dict)
        return info_dict


def filter_keys(dictionary: dict) -> dict:
    keys = ('uploader', 'title', 'description', 'tags')
    return {k: dictionary.get(k) for k in keys}
