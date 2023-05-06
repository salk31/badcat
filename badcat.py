#!/usr/local/bin/python3.9
"""label_image for tflite."""

import core
import snd
import glob
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):

  def __init__(self):
    self.core = core.Core()
    self.snd = snd.Snd()
    self.fire = 0

  #def on_any_event(self, event):
  #  print(event.event_type, event.src_path)

  def on_closed(self, event):
    print("on_closed", event.src_path)
    #print(event.src_path.strip())
    image = event.src_path
    res = self.core.process(image)
    detections = res.detections(0.8)
    
    if (len(detections) == 0):
      self.fire = 0
    else:
      got = detections[0]
      if (got[0] == 'bad'):
        self.fire += 1
      else:
        self.fire = 0
        
    print(f'{image} -> {detections} -> {self.fire}')
    if (self.fire > 30):
      self.fire = 0
      self.snd.play()


if __name__ == '__main__':


  
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
    
