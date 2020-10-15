from picamera import PiCamera
from nolesmuth_aws_s3 import upload_file
import sys

picture_name = sys.argv[1]

camera = PiCamera()

# change camera settings
camera.iso = 800
camera.exposure_mode = 'sports'

camera.capture(f'{picture_name}.jpg')

upload_file(f'{picture_name}.jpg')