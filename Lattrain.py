# Pygame template - skeleton for a new pygame project
import pygame
import random
import pandas as pd
import numpy as np
from os import path

# Konstante # Startwerte 
WIDTH = 1000
HEIGHT = 800
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (235, 227, 157)

x, w = 100, 800

## Pandas
df = pd.read_csv("vokabeln.csv")
df["random"] = np.random.randn(df.shape[0])
df.sort_values(["Kartei", "random"], ascending=False, inplace=True )
print(df.head())



# System und Funktionen
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Salve!")
clock = pygame.time.Clock()

def male_karte(x = 100, w = 800):
    pygame.draw.rect(screen, YELLOW, [x, 150, w, 500])

def drehen(trigger = 0, x = 100, w = 800):
    if trigger == 1 and w > 10:   
            x += 30
            w -= 60
    elif trigger == 1 and w <= 10:
            trigger = 2
    elif trigger == 2 and w < 800:
        x -= 30
        w += 60
    else:
        trigger = 0 
    return  trigger, x, w


def schreibe_vokabel(v = "Salve"):
    
    font1 = pygame.font.SysFont("arial", 24, False, False)
    frage = "Wie heißt das auf Latein?"
    text = font1.render(frage, True, BLACK)
    screen.blit(text, [150, 200])

    font2 = pygame.font.SysFont("arial", 24, False, False)
    vok = v
    text = font2.render(vok, True, BLUE)
    screen.blit(text, [150, 350])



def check_win(r, money):
    if r[0].seq[15] == r[1].seq[0] == r[2].seq[15]:
        money += 100000
    elif r[0].seq[15] == r[1].seq[0]:
        money += 100
    elif r[0].seq[15] == r[2].seq[15]:
        money += 100
    elif r[1].seq[0] == r[2].seq[15]:
        money += 100
    return money, True


def new_game():
    reels = [Reel(0), Reel(1), Reel(2)]
    return reels



# Game Loop
trigger, back = False, False

running = True
while running:
    clock.tick(FPS)

    # Process Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                trigger = 1
            if event.key == pygame.K_q:
                pass

    # Update & Draw
    screen.fill(BLACK)
    trigger, x, w = drehen(trigger, x, w)
    male_karte(x, w)

    if trigger == 0:
        schreibe_vokabel()
    
    



    # *after* drawing everything
    pygame.display.flip()

pygame.quit()

df.drop(columns="random", inplace=True)
df.sort_index(inplace=True)
print(df.head())
