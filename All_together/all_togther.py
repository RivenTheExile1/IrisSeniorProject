#Just psuedo code atm
#3/28/21

import pygame, sys
import pygame.camera
from pygame.constants import GL_ACCUM_ALPHA_SIZE
import picamera
import picamera.array

global leg_num
leg_num = 0

#drone start up~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print "Start simulator (SITL)"
import dronekit_sitl
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

# Import DroneKit-Python
from dronekit import  connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket

# Connect to the Vehicle.

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
     
width_search = input("Width of the area you wanna search: ")
length_search = input("lenght of the area you wanna search: ")

print "Arming motors"
# Copter should arm in GUIDED mode
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True    
# Confirm vehicle armed before attempting to take off
while not vehicle.armed:      
    print " Waiting for arming..."
    time.sleep(1)
print "Taking off!"

aTargetAltitude = 10
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
    
    go_to_func() #will create this in future
else:
    print("nothing to report sir")
    foward_backward_search_func(vehicle, width_search, length_search) #will create this in the future.

stream.seek(0)
stream.truncate()

pygame.display.update()



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


