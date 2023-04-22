#!/usr/local/bin/python3.9
"""label_image for tflite."""

import core

import glob






if __name__ == '__main__':

  core = core.Core()
  
  root = '/var/lib/motioneye/Camera1/2023-04-20/'
  images = glob.glob(root + '/*.jpg')
  
  for image in images:
    print(image)
    res = core.process(image)
    print(str(res.detections()))
