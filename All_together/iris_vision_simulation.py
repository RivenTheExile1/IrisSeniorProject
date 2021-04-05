import pygame
import sys
import time
import random
import math




def search(screen, drone, target):
    #search func
    
    #iniate at start but will update
    x = 10
    y = -10
    next_x = x
    next_y = y

    #search nearby area
    for i in range(0,600,20): #y 
        print("nedt y", next_y)
        print("next x", next_x)     



        # if and for loop handling going forward
        if next_x == 10:
            next_y = next_y + 20
            for j in range(20,600,20): #x 

                #gets the blue val at the next pixel                
                next_x = x + j 
                pixel_col = pygame.Surface.get_at(screen, (next_x, next_y))
                print (pixel_col)

                #if the value is blue print it out
                if pixel_col == (0,0,255,255):
                    print ("!!!!!!!!!!!!!!!!found blue at ", next_x, next_y)
                else:
                        print ("no blue at ", next_x, next_y)

                #moves drone over if not at 600, or next line if at 600 (doesn't work!!!)
                if next_x == 600:
                    pygame.Rect.move(drone, 0,next_y + 20)
                else: 
                    pygame.Rect.move(drone, (next_x, next_y))

                time.sleep(.25)
                screen.blit()
                pygame.display.update()

        # if and for loop that will handle the coming back
        if next_x == 590:
            print("CHECKKDFOFJDFOLFJSDOLF")
            next_y = next_y + 20
            for j in range(580,-10,-20): #x 
                
                #gets the blue val at the next pixel
                next_x = x + j

                
                pixel_col = pygame.Surface.get_at(screen, (next_x, next_y))
                print (pixel_col)

                #if the value is blue print it out
                if pixel_col == (0,0,255,255):
                    print ("!!!!!!!!!!!!!!!!found blue at ", next_x, next_y)
                else:
                        print ("no blue at ", next_x, next_y)

                #moves drone over if not at 600, or next line if at 600 (doesn't work!!!)
                if next_x == 600:
                    pygame.Rect.move(drone, 0,next_y + 20)
                else: 
                    pygame.Rect.move(drone, (next_x, next_y))

                time.sleep(.25)
                screen.blit()
                pygame.display.update()

            
        

            

#initing the main variabgle we will need
def set_up():

    #init rng
    random.seed()

    #initing clock and pygame
    pygame.init()
    clock = pygame.time.Clock()

    #setting fps, size of screen and backround color
    fps = 60
    size = [600,600]
    bg = [255,255,255]

    #init screen
    screen = pygame.display.set_mode(size)

    #init drone
    drone = pygame.Rect(0,0,20,20)

    #init target and random loc from 0,600 (size of screen)
    target_x = random.randint(0,600)
    target_y = random.randint(0,600)
    print("target loc", target_x, target_y)
    target = pygame.Rect(target_x,target_y,20,20)


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

        
        #update screen
        pygame.display.update()
        clock.tick(fps)
        search(screen, drone, target)
        

set_up()     
