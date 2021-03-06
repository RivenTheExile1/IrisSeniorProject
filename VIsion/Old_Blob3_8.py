import time
import pygame, sys

from pygame.constants import GL_ACCUM_ALPHA_SIZE
import picamera
import picamera.array

#Width and height of screen
width = 700
height = 500

#resolution of camera
resolution = (70, 50)

#calculate the scale of pixels on canvas
w, h = resolution
scaleW = width/w
scaleH = height/h

#setup sht
pygame.init()

display = pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption("Blob Tracker")

camera = picamera.PiCamera()
stream = picamera.arrary.PiRGBArray(camera)

camera.resolution = resolution
camera.vflip = True

def close():
    pygame.quit()
    sys.exit()

while True:
    x_pix = 0
    y_pix = 0
    l = 0

    display.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close()
            break

    #caspture a rbg picture to the stream
    camera.capture(stream, 'rgb', use_video_port=True)


    #somehow makes us process. lack luster docs....
    stream.seek(0)

    #iterate over all pix
    for y in range(h):
        for x in range(w):
            
            #get pixs
            r_vals = stream.array[y,x,0]
            g_vals = stream.array[y,x,1]
            b_vals = stream.array[y,x,2]

            if r_vals > g_vals and r_vals > b_vals:
                 x_pix += x 
                 y_pix += y

                 l += 1
            else:
                display.set_at((x,y), (0,0,0))


    if l > 0:
        #calc the mean 
        x_pix/=l
        y_pix/=l

        pygame.draw.circle(display, (0, 0, 255), (int(x_pix), int(y_pix)), 5, 0)
            
    else:
        print("nothing to report sir")

    stream.seek(0)
    stream.turncate()

    pygame.display.update()
