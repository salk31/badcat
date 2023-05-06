import subprocess

# for simple commands
subprocess.run(["ls", "-l"]) 

#import pygame

class Snd:
  def __init__(self):
    #pygame.mixer.init()
    #pygame.mixer.music.load("snd/mg42a.wav")
    print("snd")
  
  def play(self):
    #pygame.mixer.music.play()
    #while pygame.mixer.music.get_busy() == True:
    #  continue
    subprocess.run(["aplay", "snd/mg42a.wav"]) 
      
if __name__ == '__main__':
  snd = Snd()
  snd.play()
