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
RED = (255, 77, 77)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (235, 227, 157)
GRAY = (200, 200, 200)



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
    pygame.draw.rect(screen, RED, [x, 250, w, 5])
    pygame.draw.rect(screen, RED, [x, 600, w, 5])
    for r in range(1,7):
        pygame.draw.rect(screen, GRAY, [x, 250+50*r, w, 1])

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


def schreibe_vokabel(v = "Salve", lernsprache="Latein", vorne=1, n_vok=0, total_vok=3):
    font1 = pygame.font.SysFont("arial", 24, False, False)
    if vorne==1:
        frage = f"Wie heißt das auf {lernsprache}?"
        anweisung = "Weiter mit <Enter>"
    elif vorne ==0:
        frage = f"Auf {lernsprache} heißt es:"
        anweisung = "Gewusst? < J > oder weiter mit <Enter>"
    
    nummer = f"Karte {n_vok+1} von {total_vok}"
    text = font1.render(frage, True, BLACK)
    nummer_text = font1.render(nummer, True, BLACK)
    anweisung_text = font1.render(anweisung, True, BLACK)
    screen.blit(text, [150, 200])
    screen.blit(nummer_text, [725, 610])
    screen.blit(anweisung_text, [125, 610])

    font2 = pygame.font.SysFont("bradleyhanditc", 24, True, False)
    vok = v.split(";")
    for i, w in enumerate(vok):
        text = font2.render(w.strip(" "), True, BLUE)
        screen.blit(text, [150, 300+i*30])


def get_vok(df = df, n_vok = 173, sprache = "Deutsch"):
    return df[sprache].values[n_vok]


# Loop
def lernen(a = "Deutsch", b = "Latein", total_vok = 3):
    # immer gleiche Startwerte
    trigger, back = False, False
    x, w = 100, 800
    running = True
    vorne = 1
    n_vok = 0
    sprache = a
    # Startwerte, die übergeben werden müssen
    while running:
        clock.tick(FPS)

        # Process Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    trigger = 1
                    if vorne == 1:
                        sprache = b
                        vorne = 0
                    elif vorne == 0:
                        n_vok += 1
                        sprache = a
                        vorne = 1


                if event.key == pygame.K_j:
                    if vorne == 1:
                        pass
                    elif vorne == 0:
                        trigger=1
                        n_vok += 1
                        sprache = a
                        vorne = 1
        # Gamr Logik        
        if n_vok == total_vok:
            running = False
            break

        # Update & Draw
        screen.fill(BLACK)
        trigger, x, w = drehen(trigger, x, w)
        male_karte(x, w)

        if trigger == 0:
            schreibe_vokabel(get_vok(df = df, n_vok = n_vok, sprache = sprache), lernsprache=b, vorne=vorne, n_vok=n_vok, total_vok=total_vok)
        
        # *after* drawing everything
        pygame.display.flip()




lernen()
pygame.quit()

df.drop(columns="random", inplace=True)
df.sort_index(inplace=True)
print(df.head())
