from picamera import PiCamera
import sys
import time

picture_name = sys.argv[1]

iso = [
    100,
    200,
    300,
    400,
    500,
    600,
    700,
    800
]

exposure = [
    'night',
    'backlight',
    'spotlight',
    'sports',
    'snow',
    'beach',
    'fireworks'
]

camera = PiCamera()

for i in iso:
    for e in exposure:
        camera.iso = i
        camera.exposure_mode = e
        camera.capture(f'camera_testing/{picture_name}_{i}_{e}.jpg')
        time.sleep(1)
        print(f'iso {i} exposure {e} picture captured and saved')
