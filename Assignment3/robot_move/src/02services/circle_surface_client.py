#!/usr/bin/env python

import rospy
import sys
from robot_move.srv import circle_surface,circle_surfaceRequest,circle_surfaceResponse

# create a client node to send data and receiving the answer
def area_circle_client(radius):
    try:
        #intialize the client node with 
        # 1. same server topic (area_circle_service)
        # 2. same message server (circle_surfeace)
        area_cricle = rospy.ServiceProxy('area_cicle_service',circle_surface)
        # send the data to server and asign the result in area 
        area = area_cricle(radius)
        #return back the area to use it in printing 
        return area.area
    # if there is any error from the service send a message    
    except rospy.ServiceException as e:
        print(f"Service Call failed : {e}")

# check that the input data contain the value of the radius         
if len(sys.argv) == 2 :
    radius = int(sys.argv[1])
else:
    sys.exit("error input")

# printing the receiving data from the user
print(f"The radius of the circle is {radius}")

#printing the result the came from server (area of the circle)
print(f"The area of the circle = {area_circle_client(radius)}")