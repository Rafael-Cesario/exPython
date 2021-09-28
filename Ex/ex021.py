#tocando musica no python
import pygame
pygame.init()
pygame.mixer.music.load('../arquivos/songs/ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()
