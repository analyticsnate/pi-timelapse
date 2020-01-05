import PiCamera
import sys

picture_name = sys.argv[1]

camera = PiCamera()

# change camera settings
camera.iso = 800
camera.exposure_mode = 'sports'

camera.capture(f'aero_garden_1hour/{picture_name}.jpg')