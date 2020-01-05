from picamera import PiCamera
import sys

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

# print(f'picture captured and saved as {picture_name}.jpg')
