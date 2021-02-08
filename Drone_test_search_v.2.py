# Code to run in a square. Connection string looks for a vehicle connected by serial port.
# To do: have pattern by snake like _|-|_|-|_
# Change xfactor and yfactor to metes instad of feet
#make code prettier with more functions

import exceptions
import math
connection_string = "/dev/ttyAMA0"

from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket


# Connect to the Vehicle.
global currentlocation

print("Connecting to vehicle on: %s" % (connection_string,))

try:
    vehicle = connect(connection_string, baud=115200, wait_ready=True, heartbeat_timeout=15)

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



direction_forward = raw_input("How far out would you like to go: ")
direction_horizontal = raw_input("How far to the left (positive value) or right (negative value) would you like to go: " )
direction_horizontal_total = raw_input("Whats the total distance horizontally do you want to cover: ")
int_direction_forward = int(direction_forward)
int_direction_horizontal = int(direction_horizontal)
int_direction_horizontal_total = int(direction_horizontal_total)
times_moved_horizontal =  int_direction_horizontal_total / int_direction_horizontal #how many whole numbers we need to move sideways
last_leg =  int_direction_horizontal_total % int_direction_horizontal # this final number will determine if the robot did not complete the width of the rectangle if != 0 and give us how long we have to fly
count = 0
forward_back_var = 1 # if var is 1 then robot will move foward if var is -1 then it will move backwards set to go foward
x_factor = (1/298171.5253016029) * 3.28084 # will covert global to feet to meters
y_factor = (1/363999.33433628065) * 3.28084

def forward(int_direction_foward, currentlocation):
    currentlocation
    x_factor
    y_factor
    print "Acquiring Coordinates..."
    z = currentlocation.alt
    x =  int_direction_forward
    y = 0
    print "Coordinates acquired: ", x, ", ", y, ", ", z
    x2 = (x * x_factor) + currentlocation.lon
    y2=  (y * y_factor) + currentlocation.lat
    print "Coordinates refactored: " , x2, ", ", y2, ", ", z, "; deploying"
    coords = LocationGlobalRelative(y2,x2,z)
    print "Going to: ", (coords.lon - launchloc.lon) / x_factor, ", ", (coords.lat - launchloc.lat) / y_factor, ", ", coords.alt - launchloc.alt
    currentlocation = vehicle.location.global_relative_frame
    # print location, first in global lat and lon, then in meters from drone
    print "Location: ", currentlocation.lon, " ", currentlocation.lat, " ", currentlocation.alt, " Rloc: ", (currentlocation.lon - launchloc.lon) / x_factor, ", ", (currentlocation.lat - launchloc.lat) / y_factor, ", ", currentlocation.alt - launchloc.alt

    # begin travelling to target
    vehicle.simple_goto(coords)
    # loop to output location to track progress
    i = 0
    while i < 10:
        time.sleep(0.5)
        currentlocation = vehicle.location.global_relative_frame
        print "Location: ", currentlocation.lon, " ", currentlocation.lat, " ", currentlocation.alt, " Rloc: ", (currentlocation.lon - launchloc.lon) / x_factor, ", ", (currentlocation.lat - launchloc.lat) / y_factor, ", ", currentlocation.alt - launchloc.alt
        i = i + 1


def horizontal(int_direction_horizontal, currentlocation):
    global x_factor
    global y_factor
    print "Acquiring Coordinates..."
    z = currentlocation.alt
    x =  0
    y = int_direction_horizontal
    print "Coordinates acquired: ", x, ", ", y, ", ", z
    #converting coordinates from feet relative to drone global lat and long

    x2 = (x * x_factor) + currentlocation.lon
    y2=  (y * y_factor) + currentlocation.lat
    print "Coordinates refactored: " , x2, ", ", y2, ", ", z, "; deploying"
    coords = LocationGlobalRelative(y2,x2,z)
    print "Going to: ", (coords.lon - launchloc.lon) / x_factor, ", ", (coords.lat - launchloc.lat) / y_factor, ", ", coords.alt - launchloc.alt
    currentlocation = vehicle.location.global_relative_frame
    # print location, first in global lat and lon, then in meters from drone
    print "Location: ", currentlocation.lon, " ", currentlocation.lat, " ", currentlocation.alt, " Rloc: ", (currentlocation.lon - launchloc.lon) / x_factor, ", ", (currentlocation.lat - launchloc.lat) / y_factor, ", ", currentlocation.alt - launchloc.alt

    # begin travelling to target
    vehicle.simple_goto(coords)
    # loop to output location to track progress
    i = 0
    while i < 10:
        time.sleep(0.5)
        currentlocation = vehicle.location.global_relative_frame


        print "Location: ", currentlocation.lon, " ", currentlocation.lat, " ", currentlocation.alt, " Rloc: ", (currentlocation.lon - launchloc.lon) / x_factor, ", ", (currentlocation.lat - launchloc.lat) / y_factor, ", ", currentlocation.alt - launchloc.alt
        i = i + 1



#loop that makes it search calls on functions above
while count <= times_moved_horizontal:
        forward(forward_back_var*int_direction_forward, currentlocation)
        time.sleep(10)
        horizontal(int_direction_horizontal, currentlocation)
        time.sleep(10)
        count = count + 1
        forward_back_var = forward_back_var * -1


if last_leg != 0:
    forward(forward_back_var*int_direction_forward, currentlocation)
    horizontal(last_leg, currentlocation)
    forward(forward_back_var*int_direction_forward, currentlocation)




# Last leg

print "Returning to Launch"

vehicle.parameters['RTL_ALT'] = 0
vehicle.mode = VehicleMode("RTL")
i=0
while i<10:
    time.sleep(0.5)
    currentlocation = vehicle.location.global_relative_frame
    print "Location: ", currentlocation.lon, " ", currentlocation.lat, " ", currentlocation.alt, " Rloc: ", (currentlocation.lon-launchloc.lon)/x_factor, ", ", (currentlocation.lat-launchloc.lat)/y_factor, ", ", currentlocation.alt-launchloc.alt
    i=i+1

# Land

print "Landing"
vehicle.mode = VehicleMode("LAND")
while i<18:
    time.sleep(0.5)
    currentlocation = vehicle.location.global_relative_frame
    print "Location: ", currentlocation.lon, " ", currentlocation.lat, " ", currentlocation.alt, " Rloc: ", (currentlocation.lon-launchloc.lon)/x_factor, ", ", (currentlocation.lat-launchloc.lat)/y_factor, ", ", currentlocation.alt-launchloc.alt
    i=i+1

# End Flight Code



# Close vehicle object before exiting script
vehicle.close()
