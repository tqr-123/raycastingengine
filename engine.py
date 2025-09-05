import pygame
from pygame.locals import *

import math

gameMap = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
        ]


def main():
    
    startX = 2
    startY = 2

    angleOfPlayer = 0

   
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Raycasting Engine')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    
    
    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        if angleOfPlayer < 0:
            angleOfPlayer += (math.pi * 2)
        
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                angleOfPlayer += (math.pi / 64)
            elif event.key == K_RIGHT:
                angleOfPlayer = angleOfPlayer - (math.pi / 64)
            elif event.key == K_UP:
                startY += 0.01 * math.sin(angleOfPlayer) * -1
                startX += 0.01 * math.cos(angleOfPlayer) * -1
            elif event.key == K_DOWN:
                startY += 0.01 * math.sin(angleOfPlayer) 
                startX += 0.01 * math.cos(angleOfPlayer)
                
        if angleOfPlayer < 0:
            angleOfPlayer += (math.pi * 2)
       
        screen.fill((0, 0, 0))
        for x in range(0, 16):
            angleOfRay = angleOfPlayer - ((math.pi / 2) + (x / 16) * math.pi)
            directionVectorX = math.cos(angleOfRay)
            directionVectorY = math.sin(angleOfRay)
            step = 0.001
            distance = 0
            isHit = False 
            rayPosX = startX 
            rayPosY = startY
            while (distance <= 5 and isHit != True):
                if(rayPosX > 4 or rayPosY > 4):
                    isHit = False # may be redunant
                    break
                if(gameMap[int(rayPosX)][int(rayPosY)] == 1):
                    isHit = True
                else:
                    rayPosX = rayPosX + directionVectorX * step 
                    rayPosY = rayPosY + directionVectorX * step 
                    distance = distance + step
            fixedDistance = distance * math.cos(angleOfRay - angleOfPlayer)

            if (isHit == True):
                height = 100 / fixedDistance
                startPos = 320 - height/2
                endPos = 320 + height/2
                pygame.draw.line(screen, (255, 0, 0), (0+(x*40), startPos), (0+(x*40), endPos), 40)




                   
        pygame.display.update()
        
        
           
            

      

if __name__ == '__main__': main()
