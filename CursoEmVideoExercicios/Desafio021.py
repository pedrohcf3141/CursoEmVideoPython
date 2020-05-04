

# Desafio 21

import pygame

musica = 'Motorbreath.mp3'
pygame.init()
pygame.mixer.music.load(musica)
pygame.mixer.music.play()
pygame.event.wait()


