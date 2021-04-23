import time
import pygame, sys
import pygame.camera
from pygame.constants import GL_ACCUM_ALPHA_SIZE
import picamera
import picamera.array

#Width and height of screen
width = 350 
height = 250

#resolution of camera
resolution = (350, 250)

#calculate the scale of pixels on canvas
w, h = resolution
scaleW = width/w
scaleH = height/h

#setup sht
pygame.init()
pygame.camera.init()

#set up for main video

pygame.display.set_caption("Blob Tracker")



#set up for picamerai
camera = picamera.PiCamera()
stream = picamera.array.PiRGBArray(camera)
camera.resolution = resolution
camera.vflip = True

#preview so we can see whats beeing seen.


def close():
    pygame.quit()
    sys.exit()

while True:
    x_pix = 0
    y_pix = 0
    l = 0




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

            if b_vals > g_vals and b_vals > r_vals and b_vals > 175:
                 x_pix += x 
                 y_pix += y 

                 l += 1



    if l > 0:
        #calc the mean 
        x_pix/=l
        y_pix/=l
        print('x', x_pix)
        print('y', y_pix)

        
            
    else:
        print("nothing to report sir")

    stream.seek(0)
    stream.truncate()


