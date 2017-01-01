import sys
import pygame
import GameEngine  # <--- use statements like this to import your modules to the 'main' module
import GameAssets  # <--- you will want to define different modules for each distinct function of the game,
                   # e.g., you will want a 'game engine' module for the physics, a 'characters' module for the sprite
                   # classes, and a 'main' module that pulls all the others together and loads them.as
                   # I left an example of how to create a python object in the 'Characters.py' file, the reason
                   # you want to do it like that is it makes your code easier to extend or maintain as time goes on.


pygame.init()

display_width = 1600
display_height = 900
height_max = 600     
height_min = 550
butt = (255,100,0)

bg = pygame.image.load('Outback_BG.png')


gameDisplay = pygame.display.set_mode((display_width,display_height))


pygame.display.set_caption('Dingo'+"'"+'s'+' March to the Sea')

clock = pygame.time.Clock()

abbott = pygame.image.load('Abbott (1).png')



def abbottChar(x,y):
    gameDisplay.blit(abbott,(x,y))

x = (display_width * 0.3)
y = (display_height * 0.7)
x_change = 0
y_change = 0


ded = False

while not ded:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ded = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -8
            elif event.key == pygame.K_RIGHT:
                x_change = 8

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_change = -5
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                 y_change = 5
                  
                  



    x += x_change
    y += y_change
    if y < height_min:
        y = height_min
    elif y > height_max:
        y = height_max

    gameDisplay.blit(bg, (0, 0))
    abbottChar(x,y)
    pygame.display.update()
    clock.tick(60)

    GameEngine.Abbott.spawn()
    GameEngine.Player.spawn()

    GameEngine.Abbott.killYour()

    GameEngine.Player.attack()

pygame.quit()
quit()

    
