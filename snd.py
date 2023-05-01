import pygame

class Snd:
  def __init__(self):
    pygame.mixer.init()
    pygame.mixer.music.load("snd/mg42a.wav")
  
  def play(self):
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
      continue
      
if __name__ == '__main__':
  snd = Snd()
  snd.play()

    