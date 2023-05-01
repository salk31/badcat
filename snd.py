import pygame


if __name__ == '__main__':
  pygame.mixer.init()
  pygame.mixer.music.load("m34short.wav")
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy() == True:
    continue
    