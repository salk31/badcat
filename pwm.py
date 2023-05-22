import pigpio
import time


class Pwm:
  def __init__(self, pin):
    self.pin = pin
    self.pi = pigpio.pi() 
    self.pi.set_mode(self.pin, pigpio.OUTPUT)
    self.pi.set_PWM_frequency(self.pin, 50)
  
  def set(self, v):
    pwm = 500 + 1800 * v
    self.pi.set_servo_pulsewidth(self.pin, pwm)
    print(f"{v=}, {pwm=}")
    
  def off(self):
    self.pi.set_servo_pulsewidth(self.pin, 0)
  
  def calib(self):
    self.set(0)
    time.sleep(0.1)
    self.set(1)
    time.sleep(0.1)
    self.set(0)
    time.sleep(0.1)
    self.off()
  
if __name__ == '__main__':
  pwm = Pwm(18)
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
  
  print("zero then off")
  pwm.set(0)
  pwm.off()
  

