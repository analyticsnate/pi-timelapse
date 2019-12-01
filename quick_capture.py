from picamera import PiCamera
import sys

picture_name = sys.argv[0]
print(picture_name)

camera = PiCamera()
camera.capture(picture_name)