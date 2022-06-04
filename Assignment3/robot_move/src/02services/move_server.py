#!/usr/bin/env python

import rospy
from robot_move.srv import robot_move , robot_moveResponse
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import sqrt
x = 0 
y = 0
def pose_call_back(message):
    global x ,y 
    x = message.x
    y = message.y


def move(message):
    global x ,y
    x0 = x
    y0 = y
    print("Recieving data \n")
    twist = message.speed
    duration = message.duration
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rate =rospy.Rate(1)
    counter = 0
    #pose = Pose()
    #pose.x = x
    #pose.y = y
    try:
        while counter < duration:
            counter +=1 
            velocity_publisher.publish(twist)
            rate.sleep()
        print("Mission sucess")
        distance_x = x-x0
        distance_y = y-y0
        distance = sqrt(abs(distance_x)**2+abs(distance_y)**2)
        print(f"The intial distance in x position : {x0}\n The final distance in x position :{x}")
        print(f"The intial distance in y position : {y0}\n The final distance in y position :{y}")
        print(f"The length of straight between the inital point and final point : {distance}")
        return(robot_moveResponse(True,"Mission completed with sucess",distance))
    except:
        return(robot_moveResponse(False,"data_validation error",0))

rospy.init_node("robot_move_server")
rospy.Subscriber('/turtle1/pose',Pose,pose_call_back)
server = rospy.Service("robot_move_server",robot_move,move)
print("Ready to receive date to move the robot")
rospy.spin()
