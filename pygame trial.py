import pygame
pygame.init()
width=800
height=600
screen=pygame.display.set_mode((width,height))
player=pygame.Rect((300,350,50,50))

run=True
while run:
    pygame.draw.rect(screen,(255,0,0),player)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()

pygame.quit()