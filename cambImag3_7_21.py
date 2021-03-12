#cambridge blob detection

from imgproc import *

#create camera
cam = Camera(320, 240)

#use the camera's width and height to set the viewer size
view = Viewer(cam.width, cam.height, "Blob finding")

while True:
    #x and y position accumlators
    acc_x = 0
    acc_y = 0
    
    #number of pixels accumlated
    acc_count = 0
    
    
    #get image from cam
    image = cam.grabImage()
    
    #put rest of code here
    
    #iterate over exery pixel
    for x in range(0, image.width):
        for y in range (0, image.height):
            #get val of current pix
            red, green, blue = image[x,y]
            
            #check if the blue intesitiy is greater than the green and red
            if blue > green and blue > red:
                #color pixels which pass the test black
                #add the x and y of the found pixel to accumulators
                acc_x += x
                acc_y += y
                
                #increment the accumlated pixels' count
                acc_count += 1
            else: 
                # make it black
                image [x, y] = 0,0,0
    
    if acc_count > 0:
        #calc the mean x and y
        mean_x = acc_x / acc_count
        mean_y = acc_y / acc_count
        
        image[mean_x + 0, mean_y - 1] = 255,0,0
        image[mean_x - 1, mean_y + 0] = 255,0,0
        image[mean_x + 0, mean_y + 0] = 255,0,0
        image[mean_x + 1, mean_y + 0] = 255,0,0
        image[mean_x + 0, mean_y + 1] = 255,0,0



    
    #display the image
    view.displayImage(image)