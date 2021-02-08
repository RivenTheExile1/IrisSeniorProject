print "Start simulator (SITL)"
# import dronekit
# import socket
import exceptions
import dronekit_sitl
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# Connect to the Vehicle.
print("Connecting to vehicle on: %s" % (connection_string,))

try:
    vehicle = connect(connection_string, wait_ready=True, heartbeat_timeout=15)

# Bad TCP connection
except socket.error:
    print 'No server exists!'

# Bad TTY connection
except exceptions.OSError as e:
    print 'No serial exists!'

# API Error
except dronekit.APIException:
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



# Flight Code

# Takeoff Function

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

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
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command 
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt 
        #Break and return from function just below target altitude.        
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
            print "Reached target altitude"
            break
        time.sleep(1)

print "Set default/target airspeed to 3"
vehicle.airspeed = 3

while True:
    print "Searching for Targets"
    # check camera for targets
    # If a target is found, break
    if True:
        print "Target found!"
        break
    time.sleep(1)
# acquire target position from camera
print "Acquiring Coordinates..."
# targetpoint = camera.point
print "Coordinates acquired, deploying"
# vehicle.simple_goto(targetpoint)
time.sleep(10)
print "Deploying Ordnance"
# Drop Raisins
time.sleep(10)

print "Returning to Launch"
vehicle.mode = VehicleMode("RTL")

# End Flight Code



# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
sitl.stop()
print("Completed")
