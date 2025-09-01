import pygame
from pygame.locals import *

import math

gameMap = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
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
    background.fill((250, 250, 250))
    
    
    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return


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




                   
        
        pygame.display.flip()
        
           
            

      

if __name__ == '__main__': main()
