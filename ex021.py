# Programa em Python que abra e reproduza o áudio de um arquivo MP3
import time
import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('ex021a.mp3')
pygame.mixer.music.play()
time.sleep(10)  # tempo em segundos para parar a musica

# input()
#print('Acabou!')
#pygame.event.wait()
#pygame.mixer.music.stop()

'''
from pygame import mixer

#file name
file='ex021.mp3'

mixer.init()

#to load a music file
mixer.music.load(file)

#to play a music file
mixer.music.play()
'''