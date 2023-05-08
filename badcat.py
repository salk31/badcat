#!/usr/local/bin/python3.9
"""label_image for tflite."""

import core
import pwm
import glob
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):

  def __init__(self):
    self.core = core.Core()
    self.pwm = pwm.Pwm(18)
    self.pwm.set(0)
    time.sleep(3)
    self.pwm.off()
    self.fire = 0
    self.last_created = ''

  #def on_any_event(self, event):
  #  print(event.event_type, event.src_path)

  def on_created(self, event):
    #print("on_created", event.src_path)
    self.last_created = event.src_path

  def on_closed(self, event):
    #print("on_closed", event.src_path)
    #print(event.src_path.strip())
   
    if (event.src_path == self.last_created):
      # still getting UnidentifiedImageError
      self.last_created = ''
      
      try:
        self.process_image(event.src_path)
      except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")

  def process_image(self, image):
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
      self.pwm.set(1)
      time.sleep(2)
      self.pwm.set(0)
      time.sleep(2)
      self.pwm.off()
      print("tried to scare the bad cat!")


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
    time.sleep(10 * 60)
