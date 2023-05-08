import pigpio
import time


class Pwm:
  def __init__(self, pin):
    self.pin = pin
    self.pi = pigpio.pi() 
    self.pi.set_mode(self.pin, pigpio.OUTPUT)
    self.pi.set_PWM_frequency(self.pin, 50)
  
  def set(self, v):
    self.pi.set_servo_pulsewidth(self.pin, v)
      
if __name__ == '__main__':
  pwm = Pwm(18)
  pwm.set(10)
  time.sleep(10)
  pwm.set(2500)
  time.sleep(10)
  pwm.set(500)
  time.sleep(10)
  pwm.set(2500)
  

