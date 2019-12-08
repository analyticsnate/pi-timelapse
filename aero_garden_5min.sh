#!/bin/bash
SHELL=/bin/sh
PATH=/bin:/sbin:/usr/bin:/usr/sbin
now=$(date +%s)

python3 ~/Projects/pi-timelapse/quick_capture.py $now
