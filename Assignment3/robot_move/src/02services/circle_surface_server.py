#!/usr/bin/env python
import math,time
import rospy
from robot_move.srv import circle_surfaceResponse ,circle_surface 

def calculate_area(message):
    # printing that receving data 
    print(f"Receiving Message Radius {message.radius}")
    # calculate the area and assign to var area
    area = (message.radius)**2*math.pi
    # delay for 5 sec
    time.sleep(5)
    # return the answer to Response
    print(f"The area of circle whose radius equal {message.radius} is {area}")
    return circle_surfaceResponse(area)

#declare a node with name circle_surface
rospy.init_node("Circle_surface")
#declare a service
# 1- server topic "area_circle_service"
# 2- type of message service circle_surface
# 3- do function calculate the area of circle 
server = rospy.Service("area_cicle_service",circle_surface,calculate_area)
# Make sure that code working by printing data 
print("Ready to receive data to calculate the Area \n")
# keep your code wake up untill the service is shutdown
rospy.spin()
