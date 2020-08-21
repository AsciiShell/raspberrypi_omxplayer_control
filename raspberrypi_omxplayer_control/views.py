import os

from flask import Blueprint, render_template, jsonify, request

from .media_controller import get_media_controller, MediaControllerPlayException
from .media_finder import get_media_finder
from .youtube_utils import get_video_url, filter_keys

bp = Blueprint('hello', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/files', methods=('GET',))
def files_view():
    files = get_media_finder()
    return jsonify(files.collection)


@bp.route('/play', methods=('POST',))
def play_view():
    files = get_media_finder()
    controller = get_media_controller()
    name = request.form['name']
    if name not in files.collection:
        return
    try:
        controller.play(name)
    except MediaControllerPlayException:
        return jsonify(False)
    return jsonify(True)


@bp.route('/play_youtube', methods=('POST',))
def play_youtube_view():
    controller = get_media_controller()
    url = request.form['youtube_url']
    play_info_filtered = {}
    try:
        play_info = get_video_url(url)
        play_info_filtered = filter_keys(play_info)
        controller.play(play_info['url'])
    except (MediaControllerPlayException, FileNotFoundError) as e:
        play_info_filtered['error'] = str(e)
        return jsonify(play_info_filtered)
    return jsonify(play_info_filtered)


@bp.route('/stop', methods=('POST',))
def stop_view():
    controller = get_media_controller()
    controller.stop()
    return jsonify(True)


@bp.route('/pause', methods=('POST',))
def pause_view():
    controller = get_media_controller()
    controller.pause()
    return jsonify(True)


@bp.route('/state', methods=('GET',))
def duration_view():
    controller = get_media_controller()
    return jsonify({'duration': controller.get_duration, 'position': controller.get_position})


@bp.route('/position', methods=('POST',))
def position_view():
    controller = get_media_controller()
    position = int(request.form['position'])
    controller.set_position(position)
    return jsonify(True)


@bp.route('/shutdown', methods=('POST',))
def shutdown_view():
    os.system('sudo shutdown now')
    return jsonify(True)
