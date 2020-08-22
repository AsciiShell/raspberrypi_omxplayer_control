# raspberrypi_omxplayer_control

Web remote control for raspberrypi omxplayer

# Features

- Play media from a file or YouTube
- Pause / continue, stop viewing media
- Set the media position
- Turning off the device

# Install

You can find the latest package at [releases](https://github.com/AsciiShell/raspberrypi_omxplayer_control/releases/latest) page.

Put config into `venv/var/raspberrypi_omxplayer_control-instance/config.cfg`:
```shell script
SECRET_KEY = 'RANDOM SECRET KEY'
MEDIA_DIR = '/path/to/media/files'
JSON_AS_ASCII = False
```

Run command:
```shell script
export FLASK_APP="raspberrypi_omxplayer_control"
python -m flask run --host 0.0.0.0 --port 8888
```

Open browser at `<raspberry_ip>:8888` 

# License
MIT License

Copyright (c) 2020 AsciiShell