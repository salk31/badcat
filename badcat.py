#!/usr/local/bin/python3.9
"""label_image for tflite."""

import core
import snd
import glob
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
  def on_any_event(self, event):
    print(event.event_type, event.src_path)

  def on_created(self, event):
    print("on_created", event.src_path)
    print(event.src_path.strip())
    
    res = core.process(event.src_path)
    detections = res.detections(0.8)
    
    if (len(detections) == 0):
      fire = 0
    else:
      got = detections[0]
      if (got[0] == 'bad'):
        fire += 1
      else:
        fire = 0
        
    print(f'{image} -> {detections} -> {fire}')
    if (fire > 30):
      fire = 0
      snd.play()


if __name__ == '__main__':

  core = core.Core()
  snd = snd.Snd()
  fire = 0
  
  root = '/var/lib/motioneye/' # Camera1/2023-04-20/'
  
  event_handler = MyHandler()
  observer = Observer()
  observer.schedule(event_handler, path = root, recursive = True)
  observer.start()

  #root = '/var/lib/motioneye/Camera1/2023-04-20/'
  #images = sorted(glob.glob(root + '/*.jpg'))


  while True:
    print('sleeping')
    time.sleep(60)
    
