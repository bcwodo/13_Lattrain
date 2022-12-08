# Pygame template - skeleton for a new pygame project
import pygame
import random
from os import path

WIDTH = 4*20 + 3*128
HEIGHT = 2*20 + 128 + 30
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

img_folder = path.join(path.dirname(__file__), "img")

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LAS VEGAS")
clock = pygame.time.Clock()

money = 100

class Reel():
    def __init__(self, slot):
        self.slot = slot
        self.x = 20 + slot * 148
        self.y = 20
        self.dy = -30
        self.color = RED
        self.counter = 48*(self.slot+1)
        self.bilder = []
        self.seq = list(range(22))
        random.shuffle(self.seq)
        for i in self.seq:
            dat = ".".join((str(i),"png"))
            bild = pygame.image.load(path.join(img_folder, dat)).convert()
            self.bilder.append(bild)

    def draw(self):
        for i in range(22):
            screen.blit(self.bilder[i], [self.x, self.y + 148*i])

    def update(self):
        self.counter -= 1
        self.y += self.dy
        if self.y <= -128-148*20:
            self.y = 20
        if self.counter <=0 and (self.y % 148) ==20:
            self.dy = 0


def draw_score():
    pygame.draw.rect(screen, BLUE, [0, HEIGHT-30, WIDTH, 30])
    font = pygame.font.SysFont("arial", 20, True, False)
    score = "{0} $".format(money)
    text = font.render(score, False, YELLOW)
    screen.blit(text, [WIDTH-50, HEIGHT-25])


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


reels = new_game()
checked = False

# Game Loop
running = True
while running:
    clock.tick(FPS)

    # Process Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and rotation == 0:
                reels = new_game()
                checked = False
                money -= 1
            if event.key == pygame.K_q and rotation == 0:
                running = False

    # Update & Draw
    rotation = 0
    screen.fill(BLACK)
    for r in reels:
        rotation += r.dy
        r.update()
        r.draw()

    if rotation == 0 and checked == False:
        money, checked = check_win(reels, money)

    draw_score()
    # *after* drawing everything
    pygame.display.flip()

pygame.quit()