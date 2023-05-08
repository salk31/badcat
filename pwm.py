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
      
if __name__ == '__main__':
  pwm = Pwm(18)
  pwm.set(0)
  time.sleep(10)
  pwm.set(1)
  time.sleep(10)
  pwm.set(0)
  time.sleep(10)
  pwm.set(1)
  

