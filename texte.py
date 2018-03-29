import pygame
from pygame.locals import *
 
pygame.init()
 
window = pygame.display.set_mode((300, 300))
 
font=pygame.font.Font(None, 24) #Second is height of letter
text = font.render(str(1+5),1,(255,255,255)) #First is text, third is the color

 
def test():
  continuer = 1
  while continuer:
   
      for event in pygame.event.get():
          if event.type == QUIT:
              continuer = 0
 
      window.blit(text, (0, 0))
 
      pygame.display.flip()
 
  pygame.quit()

test()

#window.blit(pygame.font.Font(None, 24).render(str(1+5),1,(255,255,255)), (0, 0))
#1er le texte,3 la couleur, 4 l'emplacement
