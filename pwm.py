import pigpio
import time

# for simple commands
#subprocess.run(["ls", "-l"]) 

#import pygame

class Snd:
  def __init__(self, pin):
    self.pin = pin
    self.pi = pigpio.pi() 
    self.pi.set_mode(self.pin, pigpio.OUTPUT)
    self.pi.set_PWM_frequency(self.pin, 50)
  
  def set(self, v):
    self.pi.set_servo_pulsewidth(self.pin, v)
      
if __name__ == '__main__':
  pwm = Pwm(18)
  pwm.set(1000)
  time.sleep(10)
  pwm.set(2000)
  

