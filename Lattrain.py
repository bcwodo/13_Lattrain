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

# System und Funktionen
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Salve!")
clock = pygame.time.Clock()


## Pandas
def get_df():
    df = pd.read_csv("vokabeln.csv")
    df["random"] = np.random.randn(df.shape[0])
    df.sort_values(["Kartei", "random"], ascending=True, inplace=True )
    return df

def save_df(df):
    df.drop(columns="random", inplace=True)
    df.sort_index(inplace=True)
    df.to_csv("vokabeln.csv", index=False)

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


def get_vok(df, n_vok = 173, sprache = "Deutsch"):
    return df[sprache].values[n_vok]

def scoring(richtig, df):
    for i in richtig:
        df.iloc[i, 2] += 1
    return df

def start():
    startbild = pygame.image.load("kasten_2.jpg").convert()
    screen.blit(startbild, [0,0])
    font = pygame.font.SysFont("bradleyhanditc", 48, True, True)
    titel = "Mein Latein-Karteikasten"
    text = font.render(titel, True, GRAY)
    screen.blit(text, [10,10])
    pygame.display.flip()
    time.sleep(3)

def salve(df):
    done = False
    font = pygame.font.SysFont("arial", 32, True, False)
    font2 = pygame.font.SysFont("arial", 24, False, False)
    while not done:
    # INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
    
    # TEXT
        screen.fill(BLACK)
        gruss = "Salve! Willkommen beim Vokabel-Trainer"
        text = font.render(gruss, True, MAGENTA)
        screen.blit(text, [100,10])

        anzahl = df.shape[0]
        fach, anz_fach = np.unique(df["Kartei"].values, return_counts = True)
        gruss2 = (f"Es sind {anzahl} Vokabeln in der Kartei.")        
        text2 = font2.render(gruss2, True, MAGENTA)
        screen.blit(text2, [100,80])
        
        for i in range(len(fach)):
            gruss3 = f"{anz_fach[i]} Karten sind in Fach {fach[i]}."
            text3 = font2.render(gruss3, True, MAGENTA)
            screen.blit(text3, [100,130+i*30])
        
        gruss4 = "Weiter mit <ENTER>"    
        text4 = font2.render(gruss4, True, GRAY)
        screen.blit(text4, [800,700])   
        pygame.display.flip()

        clock.tick(FPS)

def menu_1():
    done = False
    font = pygame.font.SysFont("arial", 32, True, False)
    font2 = pygame.font.SysFont("arial", 24, False, False)
    while not done:
    # INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
                    total_vok = 100
                elif event.key == pygame.K_1:
                    done = True
                    total_vok = 10
                elif event.key == pygame.K_2:
                    done = True
                    total_vok = 20
                elif event.key == pygame.K_3:
                    done = True
                    total_vok = 30
                elif event.key == pygame.K_4:
                    done = True
                    total_vok = 40
                elif event.key == pygame.K_5:
                    done = True
                    total_vok = 50
                elif event.key == pygame.K_6:
                    done = True
                    total_vok = 60
                elif event.key == pygame.K_7:
                    done = True
                    total_vok = 70
                elif event.key == pygame.K_8:
                    done = True
                    total_vok = 80
                elif event.key == pygame.K_9:
                    done = True
                    total_vok = 90
                elif event.key == pygame.K_x:
                    done = True
                    total_vok = 3


    # TEXT
        screen.fill(BLACK)
        gruss = "Wie viele Worte möchtest Du Lernen?"
        text = font.render(gruss, True, MAGENTA)
        screen.blit(text, [100,10])

        for i in range(1,10):
            gruss3 = f"Drücke {i} für {10* i} Vokablen"
            text3 = font2.render(gruss3, True, MAGENTA)
            screen.blit(text3, [100,130+i*30])
        
        gruss3 = f"Oder <ENTER> für 100 Vokablen"
        text3 = font2.render(gruss3, True, MAGENTA)
        screen.blit(text3, [100,500])

        pygame.display.flip()

        clock.tick(FPS)
    return total_vok

def menu_2():
    done = False
    font = pygame.font.SysFont("arial", 32, True, False)
    font2 = pygame.font.SysFont("arial", 24, False, False)
    while not done:
    # INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    done = True
                    a, b = "Deutsch", "Latein"
                elif event.key == pygame.K_l:
                    done = True
                    a, b = "Latein", "Deutsch"


    # TEXT
        screen.fill(BLACK)
        gruss = "In welcher Sprache sollen die Lernworte gezeigt werden?"
        text = font.render(gruss, True, MAGENTA)
        screen.blit(text, [100,10])

        gruss1 = f"Drücke < d >  für Deutsch"
        gruss2 = f"Drücke < l >  für Lateil"
        text1 = font2.render(gruss1, True, MAGENTA)
        text2 = font2.render(gruss2, True, MAGENTA)
        screen.blit(text1, [100,130])
        screen.blit(text2, [100,170])

        pygame.display.flip()

        clock.tick(FPS)
    return a, b

def wdh_titel():
    screen.fill(BLUE)
    startbild = pygame.image.load("fanti.jpg").convert()
    screen.blit(startbild, [0,200])
    font = pygame.font.SysFont("bradleyhanditc", 32, True, True)
    titel = "Diese Worte sollten wir nochmal anschauen..."
    text = font.render(titel, True, GRAY)
    screen.blit(text, [10,600])
    pygame.display.flip()
    time.sleep(4)

def wiederholung(df, falsch, a="Deutsch", b="Latein"):
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
 
def lernen(df, a = "Deutsch", b = "Latein", total_vok = 3):
    # immer gleiche Startwerte
    trigger, back = False, False
    x, w = 100, 800
    running = True
    vorne = 1
    n_vok = 0
    sprache = a
    richtig = []
    falsch = []
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
                        falsch.append(n_vok)
                        sprache = a
                        vorne = 1
                        n_vok += 1

                if event.key == pygame.K_j:
                    if vorne == 1:
                        pass
                    elif vorne == 0:
                        richtig.append(n_vok)
                        trigger=1
                        sprache = a
                        vorne = 1
                        n_vok += 1
                        
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
    return richtig, falsch

def training():
    df = get_df()
    total_vok = menu_1()
    a,b = menu_2()
    richtig, falsch = lernen(df=df, total_vok=total_vok, a = a, b = b)
    df = scoring(richtig, df=df)
    if len(falsch) > 0:
        wdh_titel()
        wiederholung(df=df, falsch=falsch, a=a, b=b)
    save_df(df=df)

######## SPIEL
# Startsequenz
start()
df = get_df()
salve(df = df)
training()
# Wiederholung?

done = False
font = pygame.font.SysFont("arial", 32, True, False)
font2 = pygame.font.SysFont("arial", 24, False, False)
while not done:

    # INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
            elif event.key == pygame.K_w:
                training()
    # OUTPUT
    screen.fill(BLACK)
    gruss = "Möchtest Du nochmal Trainieren?"
    text = font.render(gruss, True, MAGENTA)
    screen.blit(text, [100,10])
    gruss1 = f"Drücke < q >,  um aufzuhören"
    gruss2 = f"Drücke < w >,  um nochmal zu trainieren"
    text1 = font2.render(gruss1, True, MAGENTA)
    text2 = font2.render(gruss2, True, MAGENTA)
    screen.blit(text1, [100,130])
    screen.blit(text2, [100,170])

    pygame.display.flip()
    # Next
    clock.tick(FPS)


pygame.quit()
