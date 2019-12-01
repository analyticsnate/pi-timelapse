from picamera import PiCamera
import sys

picture_name = sys.argv[1]

camera = PiCamera()
camera.capture(picture_name)

print(f'picture captured and saved as {picture_name}')