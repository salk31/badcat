#!/usr/local/bin/python3.9
"""label_image for tflite."""

import core
import snd
import glob






if __name__ == '__main__':

  core = core.Core()
  snd = snd.Snd()
  
  root = '/var/lib/motioneye/Camera1/2023-04-07/'
  images = sorted(glob.glob(root + '/*.jpg'))
  
  fire = 0
  for image in images:
    #print(image)
    res = core.process(image)
    detections = res.detections(0.8)
    
    if (len(detections) == 0):
      fire = 0
    else:
      got = detections[0]
      if (got[0] == 'bad'):
        fire++
      else:
        fire = 0
        
    print(f'{image} -> {detections} -> {fire}')
