import pigpio
import time


class Out:
  def __init__(self, pin):
    self.pin = pin
    self.pi = pigpio.pi() 
    self.pi.set_mode(self.pin, pigpio.OUTPUT)
  
  def set(self, v):
    self.pi.write(self.pin, v)

  
if __name__ == '__main__':
  pwm = Out(18)
  pwm.calib()
  print("full")
  pwm.set(1)
  time.sleep(1)
  
  print("zero")
  pwm.set(0)
  time.sleep(1)
  
  print("off")
  pwm.off()
  time.sleep(1)
  
  print("full")
  pwm.set(1)
  time.sleep(1)
  
  print("zero")
  pwm.set(0)
  time.sleep(1)
  
  print("off")
  pwm.off()
  

