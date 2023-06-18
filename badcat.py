#!/usr/local/bin/python3.9
"""label_image for tflite."""

import glob
import time
import random
import datetime as dt

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import core
import out

class MyHandler(FileSystemEventHandler):

  def __init__(self):
    self.core = core.Core()
    self.light = out.Out(18)
    self.light.set(1)
    
    self.fire = 0
    self.last_created = ''
    
  def tick(self):
    if 9 < dt.datetime.now().hour < 21:
      print("light off")
      self.light.set(0)
    else:
      print("light on")
      self.light.set(1)

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
    detections = res.detections(0.9)
    
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
      self.fire -= random.randint(0, 5)
      #self.pwm.set(1)
      #time.sleep(2)
      #self.pwm.set(0)
      #time.sleep(0.1)
      #self.pwm.off()
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
    observer.tick()
