#Just psuedo code atm
#3/28/21
print "Start simulator (SITL)"
import dronekit_sitl
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()
import exceptions

# Import DroneKit-Python
from dronekit import  connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket
import pygame, sys
import pygame.camera
from pygame.constants import GL_ACCUM_ALPHA_SIZE
import picamera
import picamera.array

global leg_num
leg_num = 0

#functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``

#func that tells the drone to go foward back
def foward_backward_search_func(stream, vehicle, width_search, length_search):


    #code that sets up the goin to of a location.

    currentlocation = vehicle.location.global_relative_frame
    launch_loc = currentlocation
    x = 0
    y = length_search
    z = aTargetAltitude
    print "Searching"
    print "Starting loc:", launch_loc
    xfactor=1/298171.5253016029
    yfactor=1/363999.33433628065
    x2=(x*xfactor)+currentlocation.lon
    y2=(y*yfactor)+currentlocation.lat
    coords=LocationGlobalRelative(y2, x2, z)
    print "Going to: ", (coords.lon-launchloc.lon)/xfactor, ", ", (coords.lat-launchloc.lat)/yfactor, ", ", coords.alt-launchloc.alt


    #will go to cords untill it spots blue
    while True:
        
        vehicle.simple_goto(coords)
        time.sleep(.5)

        #blue_seach() looks for blue on the stream and if it finds it then we go to it and break out of the while
        if True == blue_search(stream):

            #we found blue and go to it, break after we go to it just incase
            print "found blue"
            go_to_func(stream, vehicle)
            break

        else:
            
            #we havent found blue and keep goin
            print "current location in lon, lat:", currentlocation.lon, currentlocation.lat

            #if we are at our desitnation
            if (coords.lon, coords.lat, coords.alt)*.9 < coords < 1.1*(coords.lon, coords.lat, coords.alt):

                #inc leg num at end of leg
                leg_num = leg_num + 1
                print "didn't find blue on the way up, going to next loc"

                # we didn't find any blue and we have reached the final leg so we switch the left and right value.
                if leg_num == 3:
                    width_search = width_search * -1
                side_search_func(stream, vehicle, width_search, length_search)
                
        


#func that tells the drone to go left right  
def side_search_func(stream, vehicle, width_search, length_search):


    #code that sets up the goin to of a location.
    currentlocation = vehicle.location.global_relative_frame
    launch_loc = currentlocation
    
    x = width_search
    y = 0
    z = aTargetAltitude
    print "Searching"
    print "Starting loc:", launch_loc
    xfactor=1/298171.5253016029
    yfactor=1/363999.33433628065
    x2=(x*xfactor)+currentlocation.lon
    y2=(y*yfactor)+currentlocation.lat
    coords=LocationGlobalRelative(y2, x2, z)
    print "Going to: ", (coords.lon-launchloc.lon)/xfactor, ", ", (coords.lat-launchloc.lat)/yfactor, ", ", coords.alt-launchloc.alt


    #will go to cords untill it spots blue
    while True:

        vehicle.simple_goto(coords)
        time.sleep(.5)

        #blue_seach() looks for blue on the stream and if it finds it then we go to it and break out of the while
        if True == blue_search(stream):
            print "found blue"
            go_to_func(stream, vehicle)
            break

        #if we don't find blue
        else:

            #print where we are
            print "current location in lon, lat:", currentlocation.lon, currentlocation.lat

            #test to see if we are at our final location
            if (coords.lon, coords.lat, coords.alt)*.9 < coords < 1.1*(coords.lon, coords.lat, coords.alt):

                
                #update what leg of the trip we are on. 1 is up, 2 is right, 3 is back, 4 is left
                leg_num = leg_num + 1
                print "didn't find blue on the way to the side , going to next loc"

                #if we have done a full loop
                if leg_num == 4:
                    print "didn't find any blue at all. landing"
                    landing_func(vehicle)
                    
                else:

                    #we pass the neg value of length_search because we know we are going backwards by callin it from here
                    foward_backward_search_func(stream, vehicle, width_search, -length_search)


            


#the function that tells the drone to go to blue that it has found on the screen
def go_to_func(vehicle, stream):

    x_pix, y_pix = pix_loc(stream)
    print "x_pix location", x_pix "y_pix location", y_pix
    over = False
    while over == False:

        # math time
        # this camera has an angular fov of 53 hoz and 41 vert. We take these degrees and put them in here
        # linearFOV = 2 x tan(angularFOV/2) x height 
        # so this means that for 1m height our fov is .95m wide and .74m tall (can be changed to feat given our height is what is giving our units and the rest are just constant angles) 
        width_linear_fov = .95
        length_linear_fov = .74

        #this should give us how big of an area we can see with the camera
        width_linear_fov_at_target_alititude = width_linear_fov * aTargetAltitude
        length_linear_fov_at_target_altitude = length_linear_fov * aTargetAltitude
        
        #we know resolution is 700 x 500 so devide how much space we see by how many pixel to see how much space is in a pixel
        width_ft_ppx = width_linear_fov_at_target_alititude/700
        length_ft_ppx = length_linear_fov_at_target_altitude/500

        #update x_pix and y_pix loc just incase and everytime
        x_pix, y_pix = pix_loc(stream)

        #get the physical location by taking how wide the screen is in ft/ppx x px giving us feet away
        location_x = width_ft_ppx * x_pix
        location_y = length_ft_ppx * y_pix 


        #go to the change in x
        currentlocation = vehicle.location.global_relative_frame
        launch_loc = currentlocation
        x = location_x
        y = 0
        z = aTargetAltitude
        print "Searching"
        print "Starting loc:", launch_loc
        xfactor=1/298171.5253016029
        yfactor=1/363999.33433628065
        x2=(x*xfactor)+currentlocation.lon
        y2=(y*yfactor)+currentlocation.lat
        coords=LocationGlobalRelative(y2, x2, z)
        print "Going to: ", (coords.lon-launchloc.lon)/xfactor, ", ", (coords.lat-launchloc.lat)/yfactor, ", ", coords.alt-launchloc.alt
        vehicle.simple_goto(coords)
        i = 0
        while i<10:
            time.sleep(0.5)
            currentlocation = vehicle.location.global_relative_frame
            print "Location: ", currentlocation.lon, " ", currentlocation.lat, " ", currentlocation.alt, " Rloc: ", (currentlocation.lon-launchloc.lon)/xfactor, ", ", (currentlocation.lat-launchloc.lat)/yfactor, ", ", currentlocation.alt-launchloc.alt
            i=i+1

        #go to the change in y
        currentlocation = vehicle.location.global_relative_frame
        x = 0
        y = location_y
        z = aTargetAltitude
        print "Searching"
        print "Starting loc:", launch_loc
        xfactor=1/298171.5253016029
        yfactor=1/363999.33433628065
        x2=(x*xfactor)+currentlocation.lon
        y2=(y*yfactor)+currentlocation.lat
        coords=LocationGlobalRelative(y2, x2, z)
        print "Going to: ", (coords.lon-launchloc.lon)/xfactor, ", ", (coords.lat-launchloc.lat)/yfactor, ", ", coords.alt-launchloc.alt
        vehicle.simple_goto(coords)
        i = 0
        while i<10:
            time.sleep(0.5)
            currentlocation = vehicle.location.global_relative_frame
            print "Location: ", currentlocation.lon, " ", currentlocation.lat, " ", currentlocation.alt, " Rloc: ", (currentlocation.lon-launchloc.lon)/xfactor, ", ", (currentlocation.lat-launchloc.lat)/yfactor, ", ", currentlocation.alt-launchloc.alt
            i=i+1

        over = over_blue(vehicle, stream)

    landing_func(vehicle)







#returns (x,y) of blue on screen.
def pix_loc(stream):
    w = 700
    h = 500
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
        return(x_pix, y_pix)






#returns tf if over blue 
def over_blue(vehicle, stream):
    x_pix, y_pix, = pix_loc(stream)

    if 325 < x_pix < 375 and 225 < y_pix < 275:
        return True

    else:
        return False




#returns tf if there is blue/not
def blue_search(stream):

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
        return True
    else:
        return False

        




def landing_func(vehicle):
    print "Landing"
    vehicle.mode = VehicleMode("LAND")
    xfactor=1/298171.5253016029
    yfactor=1/363999.33433628065
    while i<18:
        time.sleep(0.5)
        currentlocation = vehicle.location.global_relative_frame
        print "Location: ", currentlocation.lon, " ", currentlocation.lat, " ", currentlocation.alt, " Rloc: ", (currentlocation.lon-launchloc.lon)/xfactor, ", ", (currentlocation.lat-launchloc.lat)/yfactor, ", ", currentlocation.alt-launchloc.alt
        i=i+1
    vehicle.close()





def close():
    pygame.quit()
    sys.exit()



#drone start up/main~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Connect to the Vehicle.

connection_string = "/dev/ttyAMA0"


print("Connecting to vehicle on: %s" % (connection_string,))
try:
    vehicle = connect(connection_string, baud=115200, wait_ready=True)

# Bad TCP connection
except socket.error:
    print 'No server exists!'

# Bad TTY connection
except exceptions.OSError as e:
    print 'No serial exists!'

# API Error
except APIException:
    print 'Timeout!'

# Other error
except:
    print 'Some other error!'


# Get some vehicle attributes (state)
print "Get some vehicle attribute values:"
print " GPS: %s" % vehicle.gps_0
print " Battery: %s" % vehicle.battery
print " Last Heartbeat: %s" % vehicle.last_heartbeat
print " Is Armable?: %s" % vehicle.is_armable
print " System status: %s" % vehicle.system_status.state
print " Mode: %s" % vehicle.mode.name    # settable


print "Basic pre-arm checks"
# Don't try to arm until autopilot is ready
while not vehicle.is_armable:
    print " Waiting for vehicle to initialise..."
    time.sleep(1)

#how far in feet we are gonna move
width_search = input("Width of the area you wanna search: ")
length_search = input("length of the area you wanna search: ")

print "Arming motors"
# Copter should arm in GUIDED mode
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True    
# Confirm vehicle armed before attempting to take off
while not vehicle.armed:      
    print " Waiting for arming..."
    time.sleep(1)
print "Taking off!"
global aTargetAltitude
aTargetAltitude = 3
vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude
# Wait until the vehicle reaches a safe height
i = 0
while i < 20:
    i += 1
    print " Altitude: ", vehicle.location.global_relative_frame.alt 
    #Break and return from function just below target altitude.        
    if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
        print "Reached target altitude"
        break
    time.sleep(1)

currentlocation = vehicle.location.global_relative_frame
# store location at launch to output locations relative to it later
launchloc=currentlocation
print "Location: ", currentlocation.lon, " ", currentlocation.lat, " ", currentlocation.alt
# set speed
print "Set default/target airspeed to 10"
vehicle.airspeed = 10


#start of vision ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#width and height of the screen
width = 700
height = 500

resolution = (700,500)

#get the ft/px which will help with getting where the blue is


w, h = resolution
scaleW = width/w
scaleH = height/h

#setup sht
pygame.init()
pygame.camera.init()

#set up for main video
display = pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption("Blob Tracker")



#set up for picamerai
camera = picamera.PiCamera()
stream = picamera.array.PiRGBArray(camera)
camera.resolution = resolution
camera.vflip = True

#preview so we can see whats beeing seen.
camera.start_preview(fullscreen=False, window=(100,20, 640, 480))


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

    pygame.draw.circle(display, (255, 0, 0), (int(x_pix), int(y_pix)), 5, 0)
    print "We found some blue"
    go_to_func(vehicle, stream) 
else:
    print("nothing to report sir")
    print "going to search"
    foward_backward_search_func(stream, vehicle, width_search, length_search)

stream.seek(0)
stream.truncate()

pygame.display.update()

<<<<<<< HEAD
=======


def foward_backward_search_func(stream, vehicle, width_search, length_search):

    currentlocation = vehicle.location.global_relative_frame
    launch_loc = currentlocation
    x = width_search
    y = 0
    print "Searching"
    print "Starting loc:", launch_loc
    xfactor=1/298171.5253016029
    yfactor=1/363999.33433628065
    x2=(x*xfactor)+currentlocation.lon
    y2=(y*yfactor)+currentlocation.lat
    coords=LocationGlobalRelative(y2, x2, z)
    print "Going to: ", (coords.lon-launchloc.lon)/xfactor, ", ", (coords.lat-launchloc.lat)/yfactor, ", ", coords.alt-launchloc.alt


    #will go to cords untill it spots blue
    while True:
        vehicle.simple_goto(coords)
        if True == blue_search(stream):
            go_to_func(stream, vehicle)
            print "found blue"
            break
        print "current location in lon, lat:", currentlocation.lon, currentlocation.lat
        if coords == ((coords.lon-launchloc.lon)/xfactor,  (coords.lat-launchloc.lat)/yfactor, coords.alt-launchloc.alt)):
            leg_num = leg_num + 1
            print "didn't find blue on the way up, going to next loc"

            side_search_func(stream, vehicle, length_search)
            
        time.sleep(.5)

        
def side_search_func(stream, vehicle, width_search, length_search):

    currentlocation = vehicle.location.global_relative_frame
    launch_loc = currentlocation
    x = width_search
    y = 0
    print "Searching"
    print "Starting loc:", launch_loc
    xfactor=1/298171.5253016029
    yfactor=1/363999.33433628065
    x2=(x*xfactor)+currentlocation.lon
    y2=(y*yfactor)+currentlocation.lat
    coords=LocationGlobalRelative(y2, x2, z)
    print "Going to: ", (coords.lon-launchloc.lon)/xfactor, ", ", (coords.lat-launchloc.lat)/yfactor, ", ", coords.alt-launchloc.alt


    #will go to cords untill it spots blue
    while True:
        vehicle.simple_goto(coords)
        if True == blue_search(stream):
            go_to_func(stream, vehicle)
            print "found blue"
            break
        print "current location in lon, lat:", currentlocation.lon, currentlocation.lat
        if coords == ((coords.lon-launchloc.lon)/xfactor,  (coords.lat-launchloc.lat)/yfactor, coords.alt-launchloc.alt)):
            leg_num = leg_num + 1
            print "didn't find blue on the way to the side , going to next loc"
            if leg_num == 4:
                landing_func(vehicle)
            foward_backward_search_func(stream, vehicle, length_search)


            
        time.sleep(.5)

            # 
    
def landing_func(vehicle):
    print "Landing"
    vehicle.mode = VehicleMode("LAND")
    while i<18:
        time.sleep(0.5)
        currentlocation = vehicle.location.global_relative_frame
        print "Location: ", currentlocation.lon, " ", currentlocation.lat, " ", currentlocation.alt, " Rloc: ", (currentlocation.lon-launchloc.lon)/xfactor, ", ", (currentlocation.lat-launchloc.lat)/yfactor, ", ", currentlocation.alt-launchloc.alt
        i=i+1
    vehicle.close()


def blue_search(stream):

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
        return True
    else:
        return False

        


def close():
    pygame.quit()
    sys.exit()


>>>>>>> 08e41f8... no update
