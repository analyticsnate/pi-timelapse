from picamera import PiCamera
import sys

picture_name = sys.argv[1]

camera = PiCamera()
camera.capture(f'aero_garden_5min/{picture_name}.jpg')

# print(f'picture captured and saved as {picture_name}.jpg')
