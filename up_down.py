#code to get iris to run updown. 
#ToDo: get it to work
#started 2/10/21

import exceptions
import math
connection_string = "/dev/ttyAMA0"


from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket


# Connect to the Vehicle.
global currentlocation

print("Connecting to vehicle on: %s" % (connection_string,))
#testtt
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
vehicle.airspeed = 3


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
