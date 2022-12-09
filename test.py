# Pygame template - skeleton for a new pygame project
import pygame
import pandas as pd
import numpy as np
from os import path
import time

# Konstante # Startwerte 
WIDTH = 1000
HEIGHT = 800
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 77, 77)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (235, 227, 157)
GRAY = (200, 200, 200)
MAGENTA = (255, 0, 255)
AQUA = (0, 255, 255)


falsch = [1,22, 33, 545]
df = pd.read_csv("vokabeln.csv")

print(df.iloc[falsch,:])

def get_vok(df, n_vok = 173, sprache = "Deutsch"):
    return df[sprache].values[n_vok]

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Salve!")
clock = pygame.time.Clock()

a = "Deutsch"
b = "Latein"

def wiederholung(df, a="Deutsch", b="Latein"):
    font = pygame.font.SysFont("arial", 24, False, False)
    # OUTPUT
    for f in falsch:
        screen.fill(BLACK)
        pygame.draw.rect(screen, YELLOW, [50, 400, 900, 5])
        sprache_a = a
        sprache_b = b
        anweisung = "Weiter mit <ENTER>"
        text_a = font.render(sprache_a, True, MAGENTA)
        text_b = font.render(sprache_b, True, AQUA)
        text_anweisung = font.render(anweisung, True, GRAY)
        screen.blit(text_a, [50,50])
        screen.blit(text_b, [50,450])
        screen.blit(text_anweisung, [700,750])

        v_a = get_vok(df, n_vok=f, sprache=a)
        v_b = get_vok(df, n_vok=f, sprache=b)
        vok_a = font.render(v_a, True, MAGENTA)
        vok_b = font.render(v_b, True, AQUA)
        screen.blit(vok_a, [50,100])
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
        screen.blit(vok_b, [50,500])
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
    




 


pygame.quit()