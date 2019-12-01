from picamera import PiCamera
import sys

camera = PiCamera()
camera.capture(sys.argv[0])