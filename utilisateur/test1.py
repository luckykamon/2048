import time
import pygame
from pygame.locals import *
from random import randint
import copy

pygame.init()
fenetre = pygame.display.set_mode((648,604), RESIZABLE)
depart = pygame.image.load("depart.png").convert()
fenetre.blit(depart, (0,0))
pygame.display.flip()

def help():
  help = pygame.image.load("help.png").convert()
  fenetre.blit(help, (0,0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type==KEYDOWN:
        initialisation()
      if event.type==MOUSEBUTTONDOWN:
        if event.button == 1:
          initialisation()

def initialisation():
  depart = pygame.image.load("depart.png").convert()
  fenetre.blit(depart, (0,0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type==MOUSEBUTTONDOWN:
        if event.button == 1:
          if 488<event.pos[1]:
            help()
      if event.type==KEYDOWN:
        demille()

def demille():
  fond = pygame.image.load("plateau2.png").convert()
  fenetre.blit(fond, (0,0))
  pygame.display.flip()
  background=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  n = randint(0,15)
  r = n % 4
  q = n / 4
  background[q][r] = 2 * randint(1,2)
  p = randint(0,15)
  c = n % 4
  v = n / 4
  while background[v][c] != 0:
    p = randint(0,15)
    c = p % 4
    v = p / 4
  background[v][c] = 2 * randint(1,2)
  affichage(background)
  while True:
    utilisateur=True
    choix=0
    while utilisateur:
      for event in pygame.event.get():
        if event.type==KEYDOWN:
          if event.key == K_LEFT:
            choix=1
            utilisateur=False
          if event.key == K_DOWN:
            choix=2
            utilisateur=False
          if event.key == K_RIGHT:
            choix=3
            utilisateur=False
          if event.key == K_UP:
            choix=4
            utilisateur=False
    verif=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for p in range(4):
      for q in range(4):
        verif[p][q]=background[p][q]
    background = transfo(background,choix)
    s = 0
    for d in range(4):
      for e in range(4):
        if background[d][e] == 0:
          s+=1
    if s == 0:
      score = 0
      for a in range(4):
        for b in range(4):
          if background[a][b] >= 4:
            score += 4
          if background[a][b] >= 8:
            score += 8
          if background[a][b] >= 16:
            score += 16
          if background[a][b] >= 32:
            score += 32
          if background[a][b] >= 64:
            score += 64
          if background[a][b] >= 128:
            score += 128
          if background[a][b] >= 256:
            score += 256
          if background[a][b] >= 512:
            score += 512
          if background[a][b] >= 1024:
            score += 1024
          if background[a][b] >= 2048:
            score += 2048
          if background[a][b] >= 4096:
            score += 4096
          if background[a][b] >= 8192:
            score += 8192
          if background[a][b] >= 16384:
            score += 16384
          if background[a][b] >= 32768:
            score += 32768
          if background[a][b] >= 65536: #In the best case if all blocks are filled
            score += 65536
      font=pygame.font.Font(None, 70)
      text = font.render(str("Score:"),1,(0,0,0))
      fenetre.blit(text, (170,0))
      font=pygame.font.Font(None, 70)
      text = font.render(str(score),1,(0,0,0))
      fenetre.blit(text, (330,0))
      pygame.display.flip()
      time.sleep(1.5)
      menu = pygame.image.load("menu.png").convert()
      fenetre.blit(menu, (190,250))
      pygame.display.flip()
      while True:
        for event in pygame.event.get():
          if event.type==KEYDOWN:
            if event.key == K_KP0:
              initialisation()
            if event.key == K_KP1:
              demille()
    if verif!=list(background):
      h = randint(0,s-1)
      for f in range(4):
        for g in range(4):
          if background[f][g] == 0:
            if h == 0:
              background[f][g] = 2 * randint(1,2)
            h-=1
    affichage(background)

def transfo(b,choix): #edit and display background
  if choix == 1:
    for k in range(4):
      t = []
      for j in range(4):
        if b[k][j] != 0:
          t.append(b[k][j])
      for m in range(4 - len(t)):
        t.append(0)
      b[k] = t
    for k in range(4):
      for j in range(3):
        if b[k][j] == b[k][j+1]:
          b[k][j] = b[k][j] + b[k][j+1]
          if j < 2:
            b[k][j+1] = b[k][j+2]
            if j < 1:
              b[k][j+2] = b[k][j+3]
          b[k][3] = 0
  if choix == 2:
    for j in range(4):
      t = []
      for k in range(4):
        if b[k][j] != 0:
          t.append(b[k][j])
      for m in range(4 - len(t)):
        t.append(0)
      for y in range(4):
        b[y][j] = t[y]
    for j in range(4):
      for k in range(3):
        if b[k][j] == b[k+1][j]:
          b[k][j] = b[k][j] + b[k+1][j]
          if k < 2:
            b[k+1][j] = b[k+2][j]
            if k < 1:
              b[k+2][j] = b[k+3][j]
          b[3][j] = 0
  if choix == 3:
    for k in range(4):
      t = []
      for j in range(4):
        if b[k][j] != 0:
          t.append(b[k][j])
      for m in range(4 - len(t)):
        t = [0] + t
      b[k] = t
    for k in range(4):
      for j in range(3):
        if b[k][-j-1] == b[k][-j-2]:
          b[k][-j-1] = b[k][-j-1] + b[k][-j-2]
          if j < 2:
            b[k][-j-2] = b[k][-j-3]
            if j < 1:
              b[k][-j-3] = b[k][-j-4]
          b[k][0] = 0
  if choix == 4:
    for j in range(4):
      t = []
      for k in range(4):
        if b[k][j] != 0:
          t.append(b[k][j])
      for m in range(4 - len(t)):
        t = [0] + t
      for y in range(4):
        b[y][j] = t[y]
    for j in range(4):
      for k in range(3):
        if b[-k-1][j] == b[-k-2][j]:
          b[-k-1][j] = b[-k-1][j] + b[-k-2][j]
          if k < 2:
            b[-k-2][j] = b[-k-3][j]
            if k < 1:
              b[-k-3][j] = b[-k-4][j]
          b[0][j] = 0
  return b
          
def affichage(b):
  fond = pygame.image.load("plateau2.png").convert()
  fenetre.blit(fond, (0,0))
  score = 0
  for a in range(4):
    for c in range(4):
      if b[a][c] >= 4:
        score += 4
      if b[a][c] >= 8:
        score += 8
      if b[a][c] >= 16:
        score += 16
      if b[a][c] >= 32:
        score += 32
      if b[a][c] >= 64:
        score += 64
      if b[a][c] >= 128:
        score += 128
      if b[a][c] >= 256:
        score += 256
      if b[a][c] >= 512:
        score += 512
      if b[a][c] >= 1024:
        score += 1024
      if b[a][c] >= 2048:
        score += 2048
      if b[a][c] >= 4096:
        score += 4096
      if b[a][c] >= 8192:
        score += 8192
      if b[a][c] >= 16384:
        score += 16384
      if b[a][c] >= 32768:
        score += 32768
      if b[a][c] >= 65536: #In the best case if all blocks are filled
        score += 65536
  font=pygame.font.Font(None, 70)
  text = font.render(str(score),1,(0,0,0))
  fenetre.blit(text, (482,544))
  for k in range(4):
    for j in range(4):
      if b[k][j] != 0:
        font=pygame.font.Font(None, 70)
        text = font.render(str(b[k][j]),1,(255,255,255))
        fenetre.blit(text, (60 + 8 + j * 158, 37 + 410 - k * 134))
        pygame.display.flip()



# A laisser a la fin
initialisation()

