import pygame
import sys
import random

class set_up:

    #initing the main variabgle we will need
    def main():

        #init rng
        random.seed()

        #initing clock and pygame
        pygame.init()
        clock = pygame.time.Clocck()

        #setting fps, size of screen and backround color
        fps = 60
        size = [600,600]
        bg = [0,0,0]

        #init screen
        screen = pygame.display.set_mode(size)

        #init drone
        drone = pygame.Rect(20,20,0,0)

        #init target and random loc from 0,600 (size of screen)
        target = pygame.Rect(5,5,random.randint(0,600), random.randint(0,600))


        #loop that runs game
        while True:
            
            #if something breaks then we out
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
                    return False


            #set up actual "game"
            screen.fill(bg)

            #draws drone and target
            pygame.draw.rect(screen, [255,0,0], drone)
            pygame.draw.rect(screen, [0,0,255], target)
           
           
            pygame.display.update()
            clock.tick(fps)

if __name__ == '__main__':
    set_up.main()